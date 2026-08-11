"""Tests for deterministic Markdown report generation."""

from datetime import datetime, timezone

from daily_intelligence.config import (
    DomainConfig,
    ReportConfig,
    SourceConfig,
)
from daily_intelligence.models import ArticleRecord
from daily_intelligence.report import (
    render_report,
    select_report_records,
)
from daily_intelligence.run_summary import RunSummary


GENERATED_AT = datetime(
    2026,
    8,
    10,
    7,
    0,
    tzinfo=timezone.utc,
)


def _source(
    *,
    source_id: str = "source_a",
    name: str = "Source A",
    source_tier: int = 1,
) -> SourceConfig:
    """Return source configuration for report tests."""

    return SourceConfig(
        id=source_id,
        name=name,
        feed_url="https://example.com/feed.xml",
        source_type="rss",
        source_tier=source_tier,
        default_domains=("technology",),
        language="en",
        geographic_scope=("Global",),
        active=True,
    )


def _domains() -> tuple[DomainConfig, ...]:
    """Return a controlled report taxonomy."""

    return (
        DomainConfig(
            id="technology",
            name="Technology and Software",
            keywords=("software",),
            active=True,
        ),
        DomainConfig(
            id="artificial_intelligence",
            name="Artificial Intelligence",
            keywords=("ai",),
            active=True,
        ),
    )


def _config(
    *,
    max_items_per_domain: int = 5,
    max_total_items: int = 30,
    max_description_length: int = 300,
) -> ReportConfig:
    """Return controlled report configuration."""

    return ReportConfig(
        max_items_per_domain=max_items_per_domain,
        max_total_items=max_total_items,
        max_description_length=max_description_length,
    )


def _record(
    *,
    record_id: str = "record-a",
    source_id: str = "source_a",
    title: str = "Sample Technology Story",
    published_at: datetime | None = datetime(
        2026,
        8,
        10,
        6,
        0,
        tzinfo=timezone.utc,
    ),
    description: str | None = "Feed-provided description.",
    domains: tuple[str, ...] = ("technology",),
    relevance_score: int = 5,
) -> ArticleRecord:
    """Return a processed record for report tests."""

    return ArticleRecord(
        source_id=source_id,
        title=title,
        normalized_title=title.casefold(),
        article_url="https://example.com/article",
        normalized_url="https://example.com/article",
        published_at=published_at,
        retrieved_at=datetime(
            2026,
            8,
            10,
            6,
            30,
            tzinfo=timezone.utc,
        ),
        description=description,
        domains=domains,
        matched_keywords=("software",),
        relevance_score=relevance_score,
        score_components=(("source_tier", 4),),
        record_id=record_id,
    )


def _run_summary(
    *,
    status: str = "success",
    active_sources: int = 1,
    successful_sources: int = 1,
    empty_sources: int = 0,
    failed_sources: int = 0,
    raw_items: int = 1,
    displayed_items: int = 1,
    warnings: tuple[str, ...] = (),
) -> RunSummary:
    """Return controlled operational metadata for report tests."""

    return RunSummary(
        run_id="20260810T070000Z",
        started_at=GENERATED_AT,
        completed_at=GENERATED_AT,
        status=status,
        collection_window=(
            datetime(
                2026,
                8,
                9,
                7,
                0,
                tzinfo=timezone.utc,
            ),
            GENERATED_AT,
        ),
        active_sources=active_sources,
        successful_sources=successful_sources,
        empty_sources=empty_sources,
        failed_sources=failed_sources,
        raw_items=raw_items,
        valid_items=1,
        invalid_items=0,
        duplicate_items=0,
        displayed_items=displayed_items,
        warnings=warnings,
    )


def test_report_contains_header_and_story() -> None:
    """A processed record becomes a readable Markdown story."""

    report = render_report(
        records=[_record()],
        sources=[_source(name="Example Technology Source")],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "# Daily Intelligence — 2026-08-10" in report
    assert "Generated: 2026-08-10T07:00:00+00:00" in report
    assert "## Technology and Software" in report
    assert (
        "### [Sample Technology Story]"
        "(https://example.com/article)"
    ) in report
    assert "**Source:** Example Technology Source" in report
    assert "**Relevance score:** 5" in report
    assert "Feed-provided description." in report


def test_higher_ranked_story_is_displayed_first() -> None:
    """Report ordering follows deterministic relevance ranking."""

    lower = _record(
        record_id="lower",
        title="Lower Ranked Story",
        relevance_score=4,
    )

    higher = _record(
        record_id="higher",
        title="Higher Ranked Story",
        relevance_score=10,
    )

    report = render_report(
        records=[lower, higher],
        sources=[_source()],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert report.index("Higher Ranked Story") < report.index(
        "Lower Ranked Story"
    )


def test_per_domain_limit_is_enforced() -> None:
    """No domain exceeds its configured item limit."""

    first = _record(
        record_id="first",
        title="First Story",
        relevance_score=10,
    )

    second = _record(
        record_id="second",
        title="Second Story",
        relevance_score=9,
    )

    report = render_report(
        records=[first, second],
        sources=[_source()],
        domains=_domains(),
        config=_config(max_items_per_domain=1),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "First Story" in report
    assert "Second Story" not in report
    assert "Displayed items: 1" in report


def test_total_report_limit_is_enforced() -> None:
    """The full report respects its configured maximum size."""

    technology = _record(
        record_id="technology",
        title="Technology Story",
        relevance_score=10,
    )

    ai = _record(
        record_id="ai",
        title="AI Story",
        domains=("artificial_intelligence",),
        relevance_score=9,
    )

    report = render_report(
        records=[technology, ai],
        sources=[_source()],
        domains=_domains(),
        config=_config(max_total_items=1),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "Technology Story" in report
    assert "AI Story" not in report
    assert "Displayed items: 1" in report


def test_unclassified_records_are_omitted() -> None:
    """Unclassified records remain outside the main report by default."""

    record = _record(
        domains=(),
    )

    report = render_report(
        records=[record],
        sources=[_source()],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "Sample Technology Story" not in report
    assert "Displayed items: 0" in report
    assert (
        "No classified items were selected for this report."
        in report
    )


def test_missing_publication_time_is_visible() -> None:
    """Missing publication metadata is not silently replaced."""

    report = render_report(
        records=[
            _record(
                published_at=None,
            )
        ],
        sources=[_source()],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "Publication time unavailable" in report


def test_description_is_truncated_to_configured_limit() -> None:
    """Feed-provided descriptions respect report-length configuration."""

    report = render_report(
        records=[
            _record(
                description="ABCDEFGHIJKLMNO",
            )
        ],
        sources=[_source()],
        domains=_domains(),
        config=_config(max_description_length=10),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert "ABCDEFG..." in report
    assert "ABCDEFGHIJKLMNO" not in report


def test_secondary_domains_are_shown_without_repeating_story() -> None:
    """Cross-domain records appear once and expose secondary tags."""

    report = render_report(
        records=[
            _record(
                domains=(
                    "technology",
                    "artificial_intelligence",
                ),
            )
        ],
        sources=[_source()],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
    )

    assert report.count("Sample Technology Story") == 1
    assert "**Also:** Artificial Intelligence" in report


def test_select_report_records_matches_report_limits() -> None:
    """Public report selection exposes the exact displayed records."""

    first = _record(
        record_id="first",
        title="First Story",
        relevance_score=10,
    )

    second = _record(
        record_id="second",
        title="Second Story",
        relevance_score=9,
    )

    selected = select_report_records(
        records=[first, second],
        sources=[_source()],
        domains=_domains(),
        config=_config(max_items_per_domain=1),
    )

    assert selected == (first,)


def test_report_exposes_degraded_run_status_and_warning() -> None:
    """Operational degradation is visible in the Markdown report."""

    report = render_report(
        records=[_record()],
        sources=[_source()],
        domains=_domains(),
        config=_config(),
        report_date="2026-08-10",
        generated_at=GENERATED_AT,
        run_summary=_run_summary(
            status="degraded",
            active_sources=2,
            successful_sources=1,
            failed_sources=1,
            raw_items=1,
            warnings=(
                "Source source_b failed: Feed unavailable",
            ),
        ),
    )

    assert "Run status: degraded" in report
    assert (
        "Monitored window: "
        "2026-08-09T07:00:00+00:00 "
        "to 2026-08-10T07:00:00+00:00"
    ) in report
    assert (
        "Sources: 2 active, 1 successful, "
        "0 empty, 1 failed"
    ) in report
    assert "Items collected: 1" in report
    assert "## Run Warnings" in report
    assert (
        "- Source source_b failed: Feed unavailable"
        in report
    )