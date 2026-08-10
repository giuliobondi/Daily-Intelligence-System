"""Tests for structured pipeline run summaries."""

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from daily_intelligence.collect import SourceCollectionResult
from daily_intelligence.deduplicate import (
    DeduplicationResult,
    DuplicateRecord,
)
from daily_intelligence.models import ArticleRecord
from daily_intelligence.run_summary import (
    build_run_summary,
    write_run_summary_json,
)
from daily_intelligence.validate import (
    InvalidRecord,
    ValidationResult,
)


STARTED_AT = datetime(
    2026,
    8,
    10,
    7,
    0,
    tzinfo=timezone.utc,
)

COMPLETED_AT = datetime(
    2026,
    8,
    10,
    7,
    1,
    tzinfo=timezone.utc,
)

WINDOW = (
    datetime(
        2026,
        8,
        9,
        7,
        0,
        tzinfo=timezone.utc,
    ),
    datetime(
        2026,
        8,
        10,
        7,
        0,
        tzinfo=timezone.utc,
    ),
)


def _record(
    *,
    title: str = "Sample Story",
) -> ArticleRecord:
    """Return a valid article record for summary tests."""

    return ArticleRecord(
        source_id="source_a",
        title=title,
        normalized_title=title.casefold(),
        article_url="https://example.com/article",
        normalized_url="https://example.com/article",
        published_at=STARTED_AT,
        retrieved_at=STARTED_AT,
        description="Sample description.",
        record_id=title.casefold().replace(" ", "-"),
    )


def _collection_result(
    *,
    source_id: str = "source_a",
    status: str = "success",
    items_received: int = 1,
    error_message: str | None = None,
) -> SourceCollectionResult:
    """Return a controlled source collection outcome."""

    return SourceCollectionResult(
        source_id=source_id,
        status=status,
        entries=(),
        items_received=items_received,
        error_type=(
            "CollectionError"
            if status == "failed"
            else None
        ),
        error_message=error_message,
        retrieved_at=STARTED_AT,
    )


def _validation_result(
    *,
    valid_records: tuple[ArticleRecord, ...] | None = None,
    invalid_records: tuple[InvalidRecord, ...] = (),
) -> ValidationResult:
    """Return controlled validation output."""

    if valid_records is None:
        valid_records = (_record(),)

    return ValidationResult(
        valid_records=valid_records,
        invalid_records=invalid_records,
    )


def _deduplication_result(
    *,
    unique_records: tuple[ArticleRecord, ...] | None = None,
    duplicate_records: tuple[DuplicateRecord, ...] = (),
) -> DeduplicationResult:
    """Return controlled deduplication output."""

    if unique_records is None:
        unique_records = (_record(),)

    return DeduplicationResult(
        unique_records=unique_records,
        duplicate_records=duplicate_records,
    )


def _build(
    *,
    collection_results: tuple[SourceCollectionResult, ...] | None = None,
    validation_result: ValidationResult | None = None,
    deduplication_result: DeduplicationResult | None = None,
    displayed_items: int = 1,
    critical_error: str | None = None,
):
    """Build a controlled run summary."""

    if collection_results is None:
        collection_results = (
            _collection_result(),
        )

    if validation_result is None:
        validation_result = _validation_result()

    if deduplication_result is None:
        deduplication_result = _deduplication_result()

    return build_run_summary(
        run_id="20260810T070000Z",
        started_at=STARTED_AT,
        completed_at=COMPLETED_AT,
        collection_window=WINDOW,
        collection_results=collection_results,
        validation_result=validation_result,
        deduplication_result=deduplication_result,
        displayed_items=displayed_items,
        critical_error=critical_error,
    )


def test_successful_run_summary_counts_pipeline_results() -> None:
    """A clean completed run receives success status."""

    summary = _build(
        collection_results=(
            _collection_result(
                source_id="source_a",
                status="success",
                items_received=2,
            ),
            _collection_result(
                source_id="source_b",
                status="empty",
                items_received=0,
            ),
        ),
    )

    assert summary.status == "success"
    assert summary.active_sources == 2
    assert summary.successful_sources == 1
    assert summary.empty_sources == 1
    assert summary.failed_sources == 0
    assert summary.raw_items == 2
    assert summary.valid_items == 1
    assert summary.invalid_items == 0
    assert summary.duplicate_items == 0
    assert summary.displayed_items == 1
    assert summary.warnings == ()


def test_source_failure_produces_degraded_status() -> None:
    """A partial source failure remains visible without false failure."""

    summary = _build(
        collection_results=(
            _collection_result(
                source_id="source_a",
            ),
            _collection_result(
                source_id="source_b",
                status="failed",
                items_received=0,
                error_message="Feed unavailable",
            ),
        ),
    )

    assert summary.status == "degraded"
    assert summary.failed_sources == 1
    assert summary.warnings == (
        "Source source_b failed: Feed unavailable",
    )


def test_invalid_record_produces_degraded_status() -> None:
    """Excluded invalid records make an otherwise completed run degraded."""

    invalid = InvalidRecord(
        record=_record(
            title="Invalid Story",
        ),
        reasons=("title must be a non-empty string",),
    )

    summary = _build(
        validation_result=_validation_result(
            invalid_records=(invalid,),
        )
    )

    assert summary.status == "degraded"
    assert summary.invalid_items == 1
    assert summary.warnings == (
        "1 invalid record(s) excluded",
    )


def test_all_sources_failed_produces_failed_status() -> None:
    """A run with no successful source is not presented as degraded success."""

    summary = _build(
        collection_results=(
            _collection_result(
                source_id="source_a",
                status="failed",
                items_received=0,
                error_message="Failure A",
            ),
            _collection_result(
                source_id="source_b",
                status="failed",
                items_received=0,
                error_message="Failure B",
            ),
        ),
        displayed_items=0,
    )

    assert summary.status == "failed"
    assert summary.failed_sources == 2


def test_critical_error_produces_failed_status() -> None:
    """A critical pipeline failure overrides otherwise successful results."""

    summary = _build(
        critical_error="Could not write report",
        displayed_items=0,
    )

    assert summary.status == "failed"
    assert summary.warnings == (
        "Critical failure: Could not write report",
    )


def test_duplicate_count_comes_from_deduplication_result() -> None:
    """Suppressed duplicates are visible in the run summary."""

    retained = _record(
        title="Retained Story",
    )
    duplicate = _record(
        title="Duplicate Story",
    )

    result = DeduplicationResult(
        unique_records=(retained,),
        duplicate_records=(
            DuplicateRecord(
                record=duplicate,
                duplicate_of=retained,
                reason="normalized_url",
            ),
        ),
    )

    summary = _build(
        deduplication_result=result,
    )

    assert summary.duplicate_items == 1


def test_run_summary_is_written_as_json(
    tmp_path: Path,
) -> None:
    """Persistent run summaries use readable machine-parseable JSON."""

    summary = _build()
    output_path = (
        tmp_path
        / "data"
        / "runs"
        / "summary.json"
    )

    write_run_summary_json(
        summary,
        output_path,
    )

    stored = json.loads(
        output_path.read_text(
            encoding="utf-8",
        )
    )

    assert stored["run_id"] == "20260810T070000Z"
    assert stored["status"] == "success"
    assert stored["started_at"] == (
        "2026-08-10T07:00:00+00:00"
    )
    assert stored["completed_at"] == (
        "2026-08-10T07:01:00+00:00"
    )
    assert stored["collection_window"] == [
        "2026-08-09T07:00:00+00:00",
        "2026-08-10T07:00:00+00:00",
    ]


def test_negative_displayed_count_is_rejected() -> None:
    """Run-summary counters cannot contain impossible negative values."""

    with pytest.raises(
        ValueError,
        match="displayed_items must be a non-negative integer",
    ):
        _build(
            displayed_items=-1,
        )


def test_naive_run_timestamp_is_rejected() -> None:
    """Run timestamps must remain timezone-aware."""

    naive_started_at = datetime(
        2026,
        8,
        10,
        7,
        0,
    )

    with pytest.raises(
        ValueError,
        match="started_at must be timezone-aware",
    ):
        build_run_summary(
            run_id="test-run",
            started_at=naive_started_at,
            completed_at=COMPLETED_AT,
            collection_window=WINDOW,
            collection_results=(
                _collection_result(),
            ),
            validation_result=_validation_result(),
            deduplication_result=_deduplication_result(),
            displayed_items=1,
        )