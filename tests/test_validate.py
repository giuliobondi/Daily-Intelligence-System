"""Tests for deterministic ArticleRecord validation."""

from dataclasses import replace
from datetime import datetime, timezone

from daily_intelligence.models import ArticleRecord
from daily_intelligence.validate import (
    validate_record,
    validate_records,
)


def _valid_record() -> ArticleRecord:
    """Return a valid record that individual tests can modify."""

    return ArticleRecord(
        source_id="sample_source",
        title="Sample AI Release",
        normalized_title="sample ai release",
        article_url="https://example.com/articles/sample-ai-release",
        normalized_url="https://example.com/articles/sample-ai-release",
        published_at=datetime(
            2026,
            8,
            6,
            8,
            30,
            tzinfo=timezone.utc,
        ),
        retrieved_at=datetime(
            2026,
            8,
            6,
            9,
            0,
            tzinfo=timezone.utc,
        ),
        description="Sample description.",
    )


def test_valid_record_has_no_validation_errors() -> None:
    """A complete usable record passes validation."""

    assert validate_record(_valid_record()) == ()


def test_missing_publication_time_is_valid() -> None:
    """Publication time is optional and must not be invented."""

    record = replace(
        _valid_record(),
        published_at=None,
    )

    assert validate_record(record) == ()
    assert record.published_at is None


def test_missing_source_id_is_rejected() -> None:
    """A blank source identifier makes the record unusable."""

    record = replace(
        _valid_record(),
        source_id="   ",
    )

    assert validate_record(record) == (
        "source_id must be a non-empty string",
    )


def test_missing_title_is_rejected() -> None:
    """A blank article title makes the record unusable."""

    record = replace(
        _valid_record(),
        title="",
    )

    assert validate_record(record) == (
        "title must be a non-empty string",
    )


def test_unusable_article_url_is_rejected() -> None:
    """Article links must be absolute HTTP or HTTPS URLs."""

    record = replace(
        _valid_record(),
        article_url="example.com/article",
    )

    assert validate_record(record) == (
        "article_url must be an absolute HTTP or HTTPS URL",
    )


def test_missing_retrieval_timestamp_is_rejected() -> None:
    """Every usable record requires a retrieval timestamp."""

    record = replace(
        _valid_record(),
        retrieved_at=None,  # type: ignore[arg-type]
    )

    assert validate_record(record) == (
        "retrieved_at must be a datetime",
    )


def test_naive_retrieval_timestamp_is_rejected() -> None:
    """Retrieval timestamps must retain timezone information."""

    record = replace(
        _valid_record(),
        retrieved_at=datetime(2026, 8, 6, 9, 0),
    )

    assert validate_record(record) == (
        "retrieved_at must be timezone-aware",
    )


def test_multiple_validation_errors_are_preserved() -> None:
    """Validation reports all detected problems with one record."""

    record = replace(
        _valid_record(),
        source_id="",
        title=" ",
        article_url="not-a-url",
    )

    assert validate_record(record) == (
        "source_id must be a non-empty string",
        "title must be a non-empty string",
        "article_url must be an absolute HTTP or HTTPS URL",
    )


def test_invalid_record_does_not_stop_valid_records() -> None:
    """Batch validation isolates bad records while preserving good ones."""

    valid_record = _valid_record()
    invalid_record = replace(
        valid_record,
        title="",
    )

    result = validate_records(
        [
            valid_record,
            invalid_record,
        ]
    )

    assert result.valid_records == (valid_record,)
    assert len(result.invalid_records) == 1
    assert result.invalid_records[0].record == invalid_record
    assert result.invalid_records[0].reasons == (
        "title must be a non-empty string",
    )