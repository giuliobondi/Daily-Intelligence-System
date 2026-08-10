"""Tests for structured source collection outcomes."""

from datetime import datetime, timezone
from pathlib import Path

import pytest

from daily_intelligence.collect import collect_source
from daily_intelligence.config import SourceConfig


RETRIEVED_AT = datetime(
    2026,
    8,
    10,
    7,
    0,
    tzinfo=timezone.utc,
)


def _source(
    feed_url: str,
) -> SourceConfig:
    """Return controlled source configuration."""

    return SourceConfig(
        id="sample_source",
        name="Sample Source",
        feed_url=feed_url,
        source_type="rss",
        source_tier=1,
        default_domains=("technology",),
        language="en",
        geographic_scope=("Global",),
        active=True,
    )


def test_source_with_entries_returns_success() -> None:
    """A valid populated feed produces a successful source result."""

    result = collect_source(
        _source("tests/fixtures/sample_feed.xml"),
        RETRIEVED_AT,
    )

    assert result.source_id == "sample_source"
    assert result.status == "success"
    assert result.items_received == 1
    assert len(result.entries) == 1
    assert result.error_type is None
    assert result.error_message is None
    assert result.retrieved_at == RETRIEVED_AT


def test_missing_feed_returns_failed_result(
    tmp_path: Path,
) -> None:
    """An operational source failure is recorded instead of raised."""

    missing_feed = tmp_path / "missing.xml"

    result = collect_source(
        _source(str(missing_feed)),
        RETRIEVED_AT,
    )

    assert result.status == "failed"
    assert result.entries == ()
    assert result.items_received == 0
    assert result.error_type == "CollectionError"
    assert result.error_message is not None
    assert "Local feed file not found" in result.error_message


def test_empty_feed_returns_empty_result(
    tmp_path: Path,
) -> None:
    """A valid feed with no entries is distinct from a failed source."""

    empty_feed = tmp_path / "empty.xml"
    empty_feed.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Empty Feed</title>
    <link>https://example.com</link>
    <description>No current entries</description>
  </channel>
</rss>
""",
        encoding="utf-8",
    )

    result = collect_source(
        _source(str(empty_feed)),
        RETRIEVED_AT,
    )

    assert result.status == "empty"
    assert result.entries == ()
    assert result.items_received == 0
    assert result.error_type is None
    assert result.error_message is None


def test_malformed_feed_returns_failed_result(
    tmp_path: Path,
) -> None:
    """Malformed source content becomes a visible failed result."""

    malformed_feed = tmp_path / "malformed.xml"
    malformed_feed.write_text(
        "<rss><channel><item>",
        encoding="utf-8",
    )

    result = collect_source(
        _source(str(malformed_feed)),
        RETRIEVED_AT,
    )

    assert result.status == "failed"
    assert result.items_received == 0
    assert result.error_type == "CollectionError"
    assert result.error_message is not None


def test_naive_retrieval_time_is_rejected() -> None:
    """Collection outcomes require an unambiguous retrieval timestamp."""

    naive_time = datetime(
        2026,
        8,
        10,
        7,
        0,
    )

    with pytest.raises(
        ValueError,
        match="retrieved_at must be timezone-aware",
    ):
        collect_source(
            _source("tests/fixtures/sample_feed.xml"),
            naive_time,
        )