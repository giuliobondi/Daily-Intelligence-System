"""Tests for the first configuration-to-normalised-record slice."""

from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from io import BytesIO
from urllib.error import HTTPError, URLError
from unittest.mock import patch

import pytest

from daily_intelligence.collect import CollectionError, collect_entries
from daily_intelligence.config import (
    ConfigurationError,
    SourceConfig,
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

def _fixture_source() -> SourceConfig:
    """Return controlled local fixture source configuration."""

    return SourceConfig(
        id="sample_source",
        name="Sample Source",
        feed_url=str(FIXTURE_PATH),
        source_type="rss",
        source_tier=1,
        default_domains=("technology",),
        language="en",
        geographic_scope=("Global",),
        active=True,
    )


def test_load_valid_source_configuration() -> None:
    """A valid YAML registry becomes typed source configuration."""

    sources = load_sources(CONFIG_PATH)

    assert len(sources) == 14

    assert tuple(source.id for source in sources) == (
        "bbc_world",
        "bbc_business",
        "ecb_press",
        "ec_highlights",
        "istat_press_en",
        "openai_news",
        "tech_eu",
        "tech_europe_foundation",
        "federal_reserve_monetary",
        "mimit_news",
        "lavoce_imprese",
        "google_deepmind_news",
        "ispi_geoeconomics",
        "european_investment_fund",
    )

    openai = next(
        source
        for source in sources
        if source.id == "openai_news"
    )

    assert openai.feed_url == "https://openai.com/news/rss.xml"
    assert openai.source_type == "rss"
    assert openai.source_tier == 1
    assert openai.default_domains == (
    "artificial_intelligence",
    )
    assert openai.language == "en"
    assert openai.geographic_scope == ("Global",)
    assert openai.active is True

    tech_eu = next(
        source
        for source in sources
        if source.id == "tech_eu"
    )

    assert tech_eu.feed_url == "https://tech.eu/feed/"
    assert tech_eu.source_type == "rss"
    assert tech_eu.source_tier == 2
    assert tech_eu.default_domains == ()
    assert tech_eu.language == "en"
    assert tech_eu.geographic_scope == ("Europe",)
    assert tech_eu.active is True

    tech_europe_foundation = next(
        source
        for source in sources
        if source.id == "tech_europe_foundation"
    )

    assert (
        tech_europe_foundation.feed_url
        == "https://tef.tech/news/feed/"
    )
    assert tech_europe_foundation.source_type == "rss"
    assert tech_europe_foundation.source_tier == 1
    assert tech_europe_foundation.default_domains == (
        "milan_bocconi_ecosystem",
    )
    assert tech_europe_foundation.language == "en"
    assert tech_europe_foundation.geographic_scope == (
        "Europe",
        "Italy",
        "Milan",
    )
    assert tech_europe_foundation.active is True

    federal_reserve_monetary = next(
        source
        for source in sources
        if source.id == "federal_reserve_monetary"
    )

    assert (
        federal_reserve_monetary.feed_url
        == "https://www.federalreserve.gov/feeds/press_monetary.xml"
    )
    assert federal_reserve_monetary.source_type == "rss"
    assert federal_reserve_monetary.source_tier == 1
    assert federal_reserve_monetary.default_domains == (
        "economics_macroeconomics",
    )
    assert federal_reserve_monetary.language == "en"
    assert federal_reserve_monetary.geographic_scope == (
        "United States",
    )
    assert federal_reserve_monetary.active is True

    mimit_news = next(
        source
        for source in sources
        if source.id == "mimit_news"
    )

    assert (
        mimit_news.feed_url
        == (
            "https://www.mimit.gov.it/index.php/it/"
            "notizie-stampa?format=feed&type=rss"
        )
    )
    assert mimit_news.source_type == "rss"
    assert mimit_news.source_tier == 1
    assert mimit_news.default_domains == ("italy",)
    assert mimit_news.language == "it"
    assert mimit_news.geographic_scope == ("Italy",)
    assert mimit_news.active is True    

    lavoce_imprese = next(
        source
        for source in sources
        if source.id == "lavoce_imprese"
    )

    assert (
        lavoce_imprese.feed_url
        == "https://lavoce.info/archives/category/argomenti/imprese/feed/"
    )
    assert lavoce_imprese.source_type == "rss"
    assert lavoce_imprese.source_tier == 2
    assert lavoce_imprese.default_domains == ("italy",)
    assert lavoce_imprese.language == "it"
    assert lavoce_imprese.geographic_scope == (
        "Italy",
        "Europe",
    )
    assert lavoce_imprese.active is True

    google_deepmind = next(
        source
        for source in sources
        if source.id == "google_deepmind_news"
    )

    assert google_deepmind.name == "Google DeepMind News"
    assert (
        google_deepmind.feed_url
        == "https://deepmind.google/blog/rss.xml"
    )
    assert google_deepmind.source_type == "rss"
    assert google_deepmind.source_tier == 1
    assert google_deepmind.default_domains == (
        "artificial_intelligence",
    )
    assert google_deepmind.language == "en"
    assert google_deepmind.geographic_scope == ("Global",)
    assert google_deepmind.active is True

    ispi_geoeconomics = next(
        source
        for source in sources
        if source.id == "ispi_geoeconomics"
    )

    assert ispi_geoeconomics.name == "ISPI Geoeconomics"
    assert (
        ispi_geoeconomics.feed_url
        == "https://www.ispionline.it/it/ricerca/geoeconomia/feed"
    )
    assert ispi_geoeconomics.source_type == "rss"
    assert ispi_geoeconomics.source_tier == 3
    assert ispi_geoeconomics.default_domains == ()
    assert ispi_geoeconomics.language == "it"
    assert ispi_geoeconomics.geographic_scope == (
        "Global",
        "Europe",
        "Italy",
    )
    assert ispi_geoeconomics.active is True

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

    source = _fixture_source()
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

def test_remote_feed_uses_timeout_and_user_agent() -> None:
    """Remote collection uses bounded requests with an explicit user agent."""

    source = replace(
        load_sources(CONFIG_PATH)[0],
        feed_url="https://example.com/feed.xml",
    )

    feed_bytes = FIXTURE_PATH.read_bytes()

    class FakeResponse(BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            self.close()

    captured_request = None
    captured_timeout = None

    def fake_urlopen(request, timeout):
        nonlocal captured_request, captured_timeout
        captured_request = request
        captured_timeout = timeout
        return FakeResponse(feed_bytes)

    with patch(
        "daily_intelligence.collect.urlopen",
        side_effect=fake_urlopen,
    ):
        entries = collect_entries(source)

    assert len(entries) == 1
    assert captured_request is not None
    assert captured_timeout == 10
    assert captured_request.get_header("User-agent") == (
        "Daily-Intelligence-System/0.1 "
        "(RSS reader; public-source research)"
    )


def test_remote_http_error_is_rejected() -> None:
    """An HTTP failure becomes a collection error."""

    source = replace(
        load_sources(CONFIG_PATH)[0],
        feed_url="https://example.com/feed.xml",
    )

    error = HTTPError(
        source.feed_url,
        403,
        "Forbidden",
        hdrs=None,
        fp=None,
    )

    with patch(
        "daily_intelligence.collect.urlopen",
        side_effect=error,
    ):
        with pytest.raises(
            CollectionError,
            match="HTTP 403",
        ):
            collect_entries(source)


def test_remote_url_error_is_rejected() -> None:
    """A remote network failure becomes a collection error."""

    source = replace(
        load_sources(CONFIG_PATH)[0],
        feed_url="https://example.com/feed.xml",
    )

    with patch(
        "daily_intelligence.collect.urlopen",
        side_effect=URLError("network unavailable"),
    ):
        with pytest.raises(
            CollectionError,
            match="network unavailable",
        ):
            collect_entries(source)


def test_remote_timeout_is_rejected() -> None:
    """A remote request cannot wait indefinitely."""

    source = replace(
        load_sources(CONFIG_PATH)[0],
        feed_url="https://example.com/feed.xml",
    )

    with patch(
        "daily_intelligence.collect.urlopen",
        side_effect=TimeoutError,
    ):
        with pytest.raises(
            CollectionError,
            match="timed out after 10 seconds",
        ):
            collect_entries(source)

def test_missing_local_feed_is_rejected() -> None:
    """A nonexistent local feed produces a collection error."""

    source = _fixture_source()
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

    source = _fixture_source()
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

    source = _fixture_source()
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
    source = _fixture_source()
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

def test_normalize_plain_text_description_is_preserved() -> None:
    """Plain-text feed descriptions remain unchanged."""

    entry = SimpleNamespace(
        title="Plain text article",
        link="https://example.com/plain-text",
        published_parsed=None,
        description="A plain feed-provided description.",
    )

    record = normalize_entry(
        entry=entry,
        source=_fixture_source(),
        retrieved_at=datetime(
            2026,
            8,
            17,
            tzinfo=timezone.utc,
        ),
    )

    assert record.description == "A plain feed-provided description."


def test_normalize_html_description_to_plain_text() -> None:
    """Visible text is retained while feed HTML markup is removed."""

    entry = SimpleNamespace(
        title="HTML article",
        link="https://example.com/html",
        published_parsed=None,
        description="<p>Hello <strong>world</strong>.</p>",
    )

    record = normalize_entry(
        entry=entry,
        source=_fixture_source(),
        retrieved_at=datetime(
            2026,
            8,
            17,
            tzinfo=timezone.utc,
        ),
    )

    assert record.description == "Hello world."


def test_normalize_description_discards_image_markup() -> None:
    """Non-text image markup does not enter normalized descriptions."""

    entry = SimpleNamespace(
        title="Article with image",
        link="https://example.com/image-description",
        published_parsed=None,
        description=(
            '<p><img alt="" src="https://example.com/image.jpg" /></p>'
            "<p>Useful summary text.</p>"
        ),
    )

    record = normalize_entry(
        entry=entry,
        source=_fixture_source(),
        retrieved_at=datetime(
            2026,
            8,
            17,
            tzinfo=timezone.utc,
        ),
    )

    assert record.description == "Useful summary text."


def test_normalize_description_decodes_html_entities() -> None:
    """HTML character entities become normal text."""

    entry = SimpleNamespace(
        title="Entity article",
        link="https://example.com/entities",
        published_parsed=None,
        description="<p>Tom &amp; Jerry &quot;example&quot;</p>",
    )

    record = normalize_entry(
        entry=entry,
        source=_fixture_source(),
        retrieved_at=datetime(
            2026,
            8,
            17,
            tzinfo=timezone.utc,
        ),
    )

    assert record.description == 'Tom & Jerry "example"'


def test_normalize_markup_only_description_becomes_none() -> None:
    """Descriptions with no visible text are treated as unavailable."""

    entry = SimpleNamespace(
        title="Image only article",
        link="https://example.com/image-only",
        published_parsed=None,
        description='<img alt="" src="https://example.com/image.jpg" />',
    )

    record = normalize_entry(
        entry=entry,
        source=_fixture_source(),
        retrieved_at=datetime(
            2026,
            8,
            17,
            tzinfo=timezone.utc,
        ),
    )

    assert record.description is None

def test_naive_retrieval_timestamp_is_rejected() -> None:
    """Retrieval timestamps must include timezone information."""

    source = _fixture_source()
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

def test_empty_default_domains_are_allowed(
    tmp_path: Path,
) -> None:
    """A broad source may rely entirely on content-based classification."""

    config_path = tmp_path / "sources.yaml"

    config_path.write_text(
        """
sources:
  - id: broad_source
    name: Broad Source
    feed_url: https://example.com/feed.xml
    source_type: rss
    source_tier: 2
    default_domains: []
    language: en
    geographic_scope:
      - Global
    active: true
""".strip()
        + "\n",
        encoding="utf-8",
    )

    sources = load_sources(config_path)

    assert len(sources) == 1
    assert sources[0].default_domains == ()

def test_empty_geographic_scope_is_rejected(
    tmp_path: Path,
) -> None:
    """Source geography remains required even when defaults are optional."""

    config_path = tmp_path / "sources.yaml"

    config_path.write_text(
        """
sources:
  - id: invalid_source
    name: Invalid Source
    feed_url: https://example.com/feed.xml
    source_type: rss
    source_tier: 2
    default_domains: []
    language: en
    geographic_scope: []
    active: true
""".strip()
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="geographic_scope.*non-empty list",
    ):
        load_sources(config_path)
