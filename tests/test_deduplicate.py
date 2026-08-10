"""Tests for deterministic exact duplicate reduction."""

from dataclasses import replace
from datetime import datetime, timezone

from daily_intelligence.deduplicate import deduplicate_records
from daily_intelligence.models import ArticleRecord


def _record(
    *,
    source_id: str = "source_a",
    title: str = "Sample AI Release",
    normalized_title: str = "sample ai release",
    article_url: str = "https://example.com/article",
    normalized_url: str = "https://example.com/article",
) -> ArticleRecord:
    """Return a valid record that individual tests can customise."""

    return ArticleRecord(
        source_id=source_id,
        title=title,
        normalized_title=normalized_title,
        article_url=article_url,
        normalized_url=normalized_url,
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


def test_distinct_records_are_preserved() -> None:
    """Records with different normalised URLs and titles remain unique."""

    first = _record()

    second = _record(
        source_id="source_b",
        title="Different Story",
        normalized_title="different story",
        article_url="https://example.com/different",
        normalized_url="https://example.com/different",
    )

    result = deduplicate_records([first, second])

    assert result.unique_records == (first, second)
    assert result.duplicate_records == ()


def test_same_normalized_url_is_duplicate() -> None:
    """Records sharing a normalised URL are reduced to one primary record."""

    first = _record()

    duplicate = _record(
        source_id="source_b",
        title="Alternative Headline",
        normalized_title="alternative headline",
        article_url="https://example.com/article?tracking=value",
        normalized_url=first.normalized_url,
    )

    result = deduplicate_records([first, duplicate])

    assert result.unique_records == (first,)
    assert len(result.duplicate_records) == 1
    assert result.duplicate_records[0].record == duplicate
    assert result.duplicate_records[0].duplicate_of == first
    assert result.duplicate_records[0].reason == "normalized_url"


def test_same_normalized_title_is_duplicate() -> None:
    """Records sharing an exact normalised title are reduced."""

    first = _record()

    duplicate = _record(
        source_id="source_b",
        article_url="https://other.example.com/story",
        normalized_url="https://other.example.com/story",
    )

    result = deduplicate_records([first, duplicate])

    assert result.unique_records == (first,)
    assert len(result.duplicate_records) == 1
    assert result.duplicate_records[0].record == duplicate
    assert result.duplicate_records[0].duplicate_of == first
    assert result.duplicate_records[0].reason == "normalized_title"


def test_first_occurrence_is_preserved() -> None:
    """Exact duplicate reduction uses stable input order."""

    first = _record(source_id="source_a")

    second = replace(
        first,
        source_id="source_b",
    )

    result = deduplicate_records([first, second])

    assert result.unique_records == (first,)
    assert result.duplicate_records[0].duplicate_of == first


def test_multiple_duplicates_are_all_recorded() -> None:
    """Several duplicates can be suppressed without losing their metadata."""

    primary = _record()

    url_duplicate = _record(
        source_id="source_b",
        title="Different Headline",
        normalized_title="different headline",
    )

    title_duplicate = _record(
        source_id="source_c",
        article_url="https://third.example.com/article",
        normalized_url="https://third.example.com/article",
    )

    result = deduplicate_records(
        [
            primary,
            url_duplicate,
            title_duplicate,
        ]
    )

    assert result.unique_records == (primary,)
    assert len(result.duplicate_records) == 2

    assert result.duplicate_records[0].record == url_duplicate
    assert result.duplicate_records[0].reason == "normalized_url"

    assert result.duplicate_records[1].record == title_duplicate
    assert result.duplicate_records[1].reason == "normalized_title"


def test_empty_input_returns_empty_result() -> None:
    """An empty validated record collection is handled normally."""

    result = deduplicate_records([])

    assert result.unique_records == ()
    assert result.duplicate_records == ()