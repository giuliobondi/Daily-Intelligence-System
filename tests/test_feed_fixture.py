"""Tests for the first configuration-to-normalised-record slice."""

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from daily_intelligence.collect import CollectionError, collect_entries
from daily_intelligence.config import (
    ConfigurationError,
    load_sources,
)
from daily_intelligence.models import ArticleRecord
from daily_intelligence.normalize import (
    NormalizationError,
    normalize_entry,
    normalize_url,
)


CONFIG_PATH = Path("config/sources.yaml")
FIXTURE_PATH = Path("tests/fixtures/sample_feed.xml")


def test_load_valid_source_configuration() -> None:
    """A valid YAML registry becomes a typed source configuration."""

    sources = load_sources(CONFIG_PATH)

    assert len(sources) == 1

    source = sources[0]

    assert source.id == "sample_source"
    assert source.feed_url == str(FIXTURE_PATH)
    assert source.source_type == "rss"
    assert source.source_tier == 1
    assert source.default_domains == ("technology",)
    assert source.language == "en"
    assert source.geographic_scope == ("Global",)
    assert source.active is True


def test_missing_source_fields_are_rejected(tmp_path: Path) -> None:
    """An incomplete source entry fails with a clear configuration error."""

    invalid_config = tmp_path / "invalid-sources.yaml"
    invalid_config.write_text(
        "sources:\n"
        "  - id: incomplete\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="missing required fields",
    ):
        load_sources(invalid_config)


def test_collect_fixture_entry() -> None:
    """The controlled RSS fixture returns one unchanged raw entry."""

    source = load_sources(CONFIG_PATH)[0]
    entries = collect_entries(source)

    assert len(entries) == 1

    entry = entries[0]

    assert entry.title == "Sample AI   Release"
    assert entry.link == (
        "https://example.com/articles/"
        "sample-ai-release?utm_source=fixture#details"
    )
    assert entry.published == "Thu, 06 Aug 2026 08:30:00 GMT"
    assert entry.description == (
        "A sample feed-provided description "
        "for the first article record."
    )


def test_missing_local_feed_is_rejected() -> None:
    """A nonexistent local feed produces a collection error."""

    source = load_sources(CONFIG_PATH)[0]
    missing_source = replace(
        source,
        feed_url="tests/fixtures/missing.xml",
    )

    with pytest.raises(
        CollectionError,
        match="Local feed file not found",
    ):
        collect_entries(missing_source)


def test_malformed_feed_is_rejected(tmp_path: Path) -> None:
    """Malformed XML is not accepted as a valid feed."""

    malformed_feed = tmp_path / "malformed-feed.xml"
    malformed_feed.write_text(
        "<rss><channel><item>",
        encoding="utf-8",
    )

    source = load_sources(CONFIG_PATH)[0]
    malformed_source = replace(
        source,
        feed_url=str(malformed_feed),
    )

    with pytest.raises(
        CollectionError,
        match="Could not parse source",
    ):
        collect_entries(malformed_source)


def test_fixture_normalises_into_article_record() -> None:
    """One raw fixture entry becomes the expected ArticleRecord."""

    source = load_sources(CONFIG_PATH)[0]
    entry = collect_entries(source)[0]
    retrieved_at = datetime(
        2026,
        8,
        6,
        9,
        0,
        tzinfo=timezone.utc,
    )

    record = normalize_entry(
        entry,
        source,
        retrieved_at,
    )

    assert isinstance(record, ArticleRecord)
    assert record.source_id == "sample_source"
    assert record.title == "Sample AI Release"
    assert record.normalized_title == "sample ai release"
    assert record.article_url == (
        "https://example.com/articles/"
        "sample-ai-release?utm_source=fixture#details"
    )
    assert record.normalized_url == (
        "https://example.com/articles/sample-ai-release"
    )
    assert record.published_at == datetime(
        2026,
        8,
        6,
        8,
        30,
        tzinfo=timezone.utc,
    )
    assert record.retrieved_at == retrieved_at
    assert record.description == (
        "A sample feed-provided description "
        "for the first article record."
    )
    assert len(record.record_id) == 64


def test_url_normalisation_preserves_meaningful_query_parameters() -> None:
    """Known tracking parameters are removed without losing useful ones."""

    result = normalize_url(
        "HTTPS://Example.COM/article"
        "?id=123&utm_source=test#section"
    )

    assert result == "https://example.com/article?id=123"


def test_missing_optional_metadata_is_preserved_as_none() -> None:
    """Missing publication time and description are not invented."""

    entry = SimpleNamespace(
        title="No date article",
        link="https://example.com/no-date",
        description=None,
    )
    source = load_sources(CONFIG_PATH)[0]
    retrieved_at = datetime(
        2026,
        8,
        6,
        9,
        0,
        tzinfo=timezone.utc,
    )

    record = normalize_entry(
        entry,
        source,
        retrieved_at,
    )

    assert record.published_at is None
    assert record.description is None


def test_naive_retrieval_timestamp_is_rejected() -> None:
    """Retrieval timestamps must include timezone information."""

    source = load_sources(CONFIG_PATH)[0]
    entry = collect_entries(source)[0]
    naive_time = datetime(2026, 8, 6, 9, 0)

    with pytest.raises(
        NormalizationError,
        match="retrieved_at must be timezone-aware",
    ):
        normalize_entry(
            entry,
            source,
            naive_time,
        )