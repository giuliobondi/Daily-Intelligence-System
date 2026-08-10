"""Build and persist structured pipeline run summaries."""

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

from daily_intelligence.collect import SourceCollectionResult
from daily_intelligence.deduplicate import DeduplicationResult
from daily_intelligence.validate import ValidationResult


@dataclass(frozen=True)
class RunSummary:
    """Persistent operational summary for one pipeline run."""

    run_id: str
    started_at: datetime
    completed_at: datetime
    status: str
    collection_window: tuple[datetime, datetime]
    active_sources: int
    successful_sources: int
    empty_sources: int
    failed_sources: int
    raw_items: int
    valid_items: int
    invalid_items: int
    duplicate_items: int
    displayed_items: int
    warnings: tuple[str, ...]


def build_run_summary(
    *,
    run_id: str,
    started_at: datetime,
    completed_at: datetime,
    collection_window: tuple[datetime, datetime],
    collection_results: Iterable[SourceCollectionResult],
    validation_result: ValidationResult,
    deduplication_result: DeduplicationResult,
    displayed_items: int,
    critical_error: str | None = None,
) -> RunSummary:
    """Build a deterministic summary from completed pipeline results."""

    _require_aware_datetime(started_at, "started_at")
    _require_aware_datetime(completed_at, "completed_at")

    window_start, window_end = collection_window

    _require_aware_datetime(
        window_start,
        "collection_window start",
    )
    _require_aware_datetime(
        window_end,
        "collection_window end",
    )

    if not isinstance(run_id, str) or not run_id.strip():
        raise ValueError("run_id must be a non-empty string")

    if completed_at < started_at:
        raise ValueError(
            "completed_at must not be earlier than started_at"
        )

    if window_end < window_start:
        raise ValueError(
            "collection window end must not be earlier than start"
        )

    if (
        not isinstance(displayed_items, int)
        or isinstance(displayed_items, bool)
        or displayed_items < 0
    ):
        raise ValueError(
            "displayed_items must be a non-negative integer"
        )

    source_results = tuple(collection_results)

    successful_sources = sum(
        result.status == "success"
        for result in source_results
    )
    empty_sources = sum(
        result.status == "empty"
        for result in source_results
    )
    failed_sources = sum(
        result.status == "failed"
        for result in source_results
    )

    raw_items = sum(
        result.items_received
        for result in source_results
    )

    invalid_items = len(
        validation_result.invalid_records
    )

    duplicate_items = len(
        deduplication_result.duplicate_records
    )

    warnings = _build_warnings(
        source_results=source_results,
        invalid_items=invalid_items,
        critical_error=critical_error,
    )

    status = _determine_status(
        active_sources=len(source_results),
        failed_sources=failed_sources,
        invalid_items=invalid_items,
        critical_error=critical_error,
    )

    return RunSummary(
        run_id=run_id.strip(),
        started_at=started_at,
        completed_at=completed_at,
        status=status,
        collection_window=(
            window_start,
            window_end,
        ),
        active_sources=len(source_results),
        successful_sources=successful_sources,
        empty_sources=empty_sources,
        failed_sources=failed_sources,
        raw_items=raw_items,
        valid_items=len(
            validation_result.valid_records
        ),
        invalid_items=invalid_items,
        duplicate_items=duplicate_items,
        displayed_items=displayed_items,
        warnings=warnings,
    )


def write_run_summary_json(
    summary: RunSummary,
    path: str | Path,
) -> None:
    """Persist one run summary as readable JSON."""

    output_path = Path(path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    data = asdict(summary)

    data["started_at"] = summary.started_at.isoformat()
    data["completed_at"] = summary.completed_at.isoformat()
    data["collection_window"] = [
        value.isoformat()
        for value in summary.collection_window
    ]

    output_path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _determine_status(
    *,
    active_sources: int,
    failed_sources: int,
    invalid_items: int,
    critical_error: str | None,
) -> str:
    """Return success, degraded, or failed for one run."""

    if critical_error is not None:
        return "failed"

    if (
        active_sources > 0
        and failed_sources == active_sources
    ):
        return "failed"

    if failed_sources > 0 or invalid_items > 0:
        return "degraded"

    return "success"


def _build_warnings(
    *,
    source_results: tuple[SourceCollectionResult, ...],
    invalid_items: int,
    critical_error: str | None,
) -> tuple[str, ...]:
    """Build concise warnings for recoverable or critical failures."""

    warnings: list[str] = []

    for result in source_results:
        if result.status != "failed":
            continue

        warning = f"Source {result.source_id} failed"

        if result.error_message:
            warning = (
                f"{warning}: {result.error_message}"
            )

        warnings.append(warning)

    if invalid_items:
        warnings.append(
            f"{invalid_items} invalid record(s) excluded"
        )

    if critical_error is not None:
        warnings.append(
            f"Critical failure: {critical_error}"
        )

    return tuple(warnings)


def _require_aware_datetime(
    value: datetime,
    field: str,
) -> None:
    """Require a timezone-aware datetime."""

    if (
        not isinstance(value, datetime)
        or value.tzinfo is None
        or value.utcoffset() is None
    ):
        raise ValueError(
            f"{field} must be timezone-aware"
        )