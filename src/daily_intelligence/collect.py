"""Collect raw entries from RSS and Atom sources."""
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import feedparser

from daily_intelligence.config import SourceConfig


class CollectionError(RuntimeError):
    """Raised when a configured feed cannot be parsed reliably."""

@dataclass(frozen=True)
class SourceCollectionResult:
    """Structured outcome from collecting one configured source."""

    source_id: str
    status: str
    entries: tuple[Any, ...]
    items_received: int
    error_type: str | None
    error_message: str | None
    retrieved_at: datetime

def collect_entries(source: SourceConfig) -> list[Any]:
    """Parse one configured source and return its raw feed entries."""

    feed_location = _resolve_feed_location(source.feed_url)
    parsed_feed = feedparser.parse(feed_location)

    if parsed_feed.bozo:
        error = getattr(parsed_feed, "bozo_exception", None)
        message = f"Could not parse source {source.id!r}"

        if error is not None:
            message = f"{message}: {error}"

        raise CollectionError(message)

    return list(parsed_feed.entries)


def _resolve_feed_location(feed_url: str) -> str:
    """Return a local fixture path or remote feed URL for feedparser."""

    if feed_url.startswith(("http://", "https://")):
        return feed_url

    path = Path(feed_url)

    if not path.is_file():
        raise CollectionError(f"Local feed file not found: {path}")

    return str(path)

def collect_source(
    source: SourceConfig,
    retrieved_at: datetime,
) -> SourceCollectionResult:
    """Collect one source and preserve success, empty, or failure status."""

    if (
        retrieved_at.tzinfo is None
        or retrieved_at.utcoffset() is None
    ):
        raise ValueError(
            "retrieved_at must be timezone-aware"
        )

    try:
        entries = tuple(collect_entries(source))
    except CollectionError as error:
        return SourceCollectionResult(
            source_id=source.id,
            status="failed",
            entries=(),
            items_received=0,
            error_type=type(error).__name__,
            error_message=str(error),
            retrieved_at=retrieved_at,
        )

    status = "success" if entries else "empty"

    return SourceCollectionResult(
        source_id=source.id,
        status=status,
        entries=entries,
        items_received=len(entries),
        error_type=None,
        error_message=None,
        retrieved_at=retrieved_at,
    )