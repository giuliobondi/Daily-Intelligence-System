"""Collect raw entries from RSS and Atom sources."""

from pathlib import Path
from typing import Any

import feedparser

from daily_intelligence.config import SourceConfig


class CollectionError(RuntimeError):
    """Raised when a configured feed cannot be parsed reliably."""


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
