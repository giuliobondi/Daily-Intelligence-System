"""Tests for deterministic collection-window filtering."""

from datetime import datetime, timezone

import pytest

from daily_intelligence.filter_window import (
    filter_records_by_window,
)
from daily_intelligence.models import ArticleRecord


WINDOW_START = datetime(
    2026,
    8,
    10,
    9,
    0,
    tzinfo=timezone.utc,
)

WINDOW_END = datetime(
    2026,
    8,
    11,
    9,
    0,
    tzinfo=timezone.utc,
)


def _record(
    *,
    title: str = "Sample Story",
    published_at: datetime | None = WINDOW_START,
) -> ArticleRecord:
    """Return a controlled article record."""

    return ArticleRecord(
        source_id="source_a",
        title=title,
        normalized_title=title.casefold(),
        article_url="https://example.com/article",
        normalized_url="https://example.com/article",
        published_at=published_at,
        retrieved_at=WINDOW_END,
        description="Sample description.",
        record_id=title.casefold().replace(" ", "-"),
    )


def test_record_inside_window_is_retained() -> None:
    """A publication inside the collection window remains eligible."""

    record = _record(
        published_at=datetime(
            2026,
            8,
            10,
            12,
            0,
            tzinfo=timezone.utc,
        )
    )

    result = filter_records_by_window(
        [record],
        (WINDOW_START, WINDOW_END),
    )

    assert result == (record,)


def test_record_before_window_is_excluded() -> None:
    """An older publication does not enter the current daily run."""

    record = _record(
        published_at=datetime(
            2026,
            8,
            6,
            8,
            30,
            tzinfo=timezone.utc,
        )
    )

    result = filter_records_by_window(
        [record],
        (WINDOW_START, WINDOW_END),
    )

    assert result == ()


def test_record_after_window_is_excluded() -> None:
    """A publication later than the window end is excluded."""

    record = _record(
        published_at=datetime(
            2026,
            8,
            11,
            10,
            0,
            tzinfo=timezone.utc,
        )
    )

    result = filter_records_by_window(
        [record],
        (WINDOW_START, WINDOW_END),
    )

    assert result == ()


def test_window_boundaries_are_inclusive() -> None:
    """Records exactly on either boundary remain eligible."""

    start_record = _record(
        title="Start Story",
        published_at=WINDOW_START,
    )

    end_record = _record(
        title="End Story",
        published_at=WINDOW_END,
    )

    result = filter_records_by_window(
        [start_record, end_record],
        (WINDOW_START, WINDOW_END),
    )

    assert result == (
        start_record,
        end_record,
    )


def test_missing_publication_time_is_excluded() -> None:
    """Records without confirmed publication time are excluded for now."""

    record = _record(
        published_at=None,
    )

    result = filter_records_by_window(
        [record],
        (WINDOW_START, WINDOW_END),
    )

    assert result == ()


def test_naive_window_timestamp_is_rejected() -> None:
    """Collection-window timestamps must remain timezone-aware."""

    naive_start = datetime(
        2026,
        8,
        10,
        9,
        0,
    )

    with pytest.raises(
        ValueError,
        match="collection_window start must be timezone-aware",
    ):
        filter_records_by_window(
            [_record()],
            (naive_start, WINDOW_END),
        )


def test_reversed_window_is_rejected() -> None:
    """The window end cannot precede the window start."""

    with pytest.raises(
        ValueError,
        match="collection window end must not be earlier than start",
    ):
        filter_records_by_window(
            [_record()],
            (WINDOW_END, WINDOW_START),
        )