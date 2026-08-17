"""Tests for deterministic domain classification."""

from dataclasses import replace
from datetime import datetime, timezone

from daily_intelligence.classify import classify_record
from daily_intelligence.config import DomainConfig, SourceConfig
from daily_intelligence.models import ArticleRecord


def _record(
    *,
    title: str = "General business update",
    description: str | None = None,
) -> ArticleRecord:
    """Return a valid unclassified article record."""

    return ArticleRecord(
        source_id="sample_source",
        title=title,
        normalized_title=title.casefold(),
        article_url="https://example.com/article",
        normalized_url="https://example.com/article",
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
        description=description,
    )


def _source(
    *,
    default_domains: tuple[str, ...] = ("technology",),
) -> SourceConfig:
    """Return source configuration for classifier tests."""

    return SourceConfig(
        id="sample_source",
        name="Sample Source",
        feed_url="tests/fixtures/sample_feed.xml",
        source_type="rss",
        source_tier=1,
        default_domains=default_domains,
        language="en",
        geographic_scope=("Global",),
        active=True,
    )


def _domains() -> tuple[DomainConfig, ...]:
    """Return a small controlled domain taxonomy."""

    return (
        DomainConfig(
            id="technology",
            name="Technology and Software",
            keywords=(
                "software",
                "cloud",
                "api",
            ),
            active=True,
        ),
        DomainConfig(
            id="artificial_intelligence",
            name="Artificial Intelligence",
            keywords=(
                "artificial intelligence",
                "AI",
                "machine learning",
                "model release",
            ),
            active=True,
        ),
    )


def test_source_default_domain_is_assigned() -> None:
    """Configured source defaults contribute to classification."""

    record = _record()

    result = classify_record(
        record,
        _source(),
        _domains(),
    )

    assert result.domains == ("technology",)
    assert result.matched_keywords == ()


def test_title_keyword_assigns_domain() -> None:
    """A configured title keyword assigns its domain."""

    record = _record(
        title="New AI model release announced",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ("artificial_intelligence",)
    assert result.matched_keywords == (
        "AI",
        "model release",
    )


def test_description_keyword_assigns_domain() -> None:
    """Feed-provided description text may contribute to classification."""

    record = _record(
        description="The company launched new cloud infrastructure.",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ("technology",)
    assert result.matched_keywords == ("cloud",)


def test_multiple_domains_can_be_assigned() -> None:
    """One article may legitimately receive several domains."""

    record = _record(
        title="AI software platform launches",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == (
        "technology",
        "artificial_intelligence",
    )
    assert result.matched_keywords == (
        "software",
        "AI",
    )


def test_source_default_and_keyword_domain_are_combined() -> None:
    """Source defaults and content matches contribute together."""

    record = _record(
        title="AI research update",
    )

    result = classify_record(
        record,
        _source(),
        _domains(),
    )

    assert result.domains == (
        "technology",
        "artificial_intelligence",
    )
    assert result.matched_keywords == ("AI",)


def test_unmatched_record_remains_unclassified() -> None:
    """No configured evidence leaves the record explicitly unclassified."""

    record = _record(
        title="Quarterly business update",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ()
    assert result.matched_keywords == ()


def test_inactive_domain_is_ignored() -> None:
    """Inactive domains do not participate in classification."""

    inactive_domain = DomainConfig(
        id="artificial_intelligence",
        name="Artificial Intelligence",
        keywords=("AI",),
        active=False,
    )

    record = _record(
        title="AI model announced",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        (inactive_domain,),
    )

    assert result.domains == ()
    assert result.matched_keywords == ()


def test_keyword_matching_does_not_use_partial_words() -> None:
    """Short keywords do not match inside unrelated words."""

    record = _record(
        title="Company chair said revenue increased",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ()
    assert result.matched_keywords == ()

def test_uppercase_keyword_matching_is_case_sensitive() -> None:
    """Intentional uppercase keywords preserve acronym case."""

    record = _record(
        title="Company plans to use AI for customer support",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ("artificial_intelligence",)
    assert result.matched_keywords == ("AI",)


def test_uppercase_keyword_does_not_match_lowercase_italian_word() -> None:
    """The AI acronym does not match the Italian lowercase word 'ai'."""

    record = _record(
        title="Incentivi ai nuovi residenti",
        description="Ai cittadini vengono offerti nuovi bonus.",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ()
    assert result.matched_keywords == ()

def test_existing_record_is_not_mutated() -> None:
    """Classification returns an enriched immutable record."""

    record = _record(
        title="Cloud software update",
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert record.domains == ()
    assert record.matched_keywords == ()

    assert result is not record
    assert result.domains == ("technology",)


def test_existing_classification_is_replaced_deterministically() -> None:
    """Reclassification derives output from current rules rather than stale data."""

    record = replace(
        _record(title="AI model release"),
        domains=("old_domain",),
        matched_keywords=("old_keyword",),
    )

    result = classify_record(
        record,
        _source(default_domains=()),
        _domains(),
    )

    assert result.domains == ("artificial_intelligence",)
    assert result.matched_keywords == (
        "AI",
        "model release",
    )