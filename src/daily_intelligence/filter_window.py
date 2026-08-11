"""Filter article records by the configured collection window."""

from datetime import datetime
from typing import Iterable

from daily_intelligence.models import ArticleRecord


def filter_records_by_window(
    records: Iterable[ArticleRecord],
    collection_window: tuple[datetime, datetime],
) -> tuple[ArticleRecord, ...]:
    """Return records whose publication time falls inside the window."""

    window_start, window_end = collection_window

    _require_aware_datetime(
        window_start,
        "collection_window start",
    )
    _require_aware_datetime(
        window_end,
        "collection_window end",
    )

    if window_end < window_start:
        raise ValueError(
            "collection window end must not be earlier than start"
        )

    selected: list[ArticleRecord] = []

    for record in records:
        if record.published_at is None:
            continue

        _require_aware_datetime(
            record.published_at,
            "published_at",
        )

        if window_start <= record.published_at <= window_end:
            selected.append(record)

    return tuple(selected)


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