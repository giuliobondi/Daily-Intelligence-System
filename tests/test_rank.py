"""Tests for deterministic provisional relevance scoring."""

from dataclasses import replace
from datetime import datetime, timezone

from daily_intelligence.config import RankingConfig, SourceConfig
from daily_intelligence.models import ArticleRecord
from daily_intelligence.rank import score_record


def _record(
    *,
    domains: tuple[str, ...] = (),
    matched_keywords: tuple[str, ...] = (),
) -> ArticleRecord:
    """Return a valid classified record for ranking tests."""

    return ArticleRecord(
        source_id="sample_source",
        title="Sample AI Release",
        normalized_title="sample ai release",
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
        description="Sample description.",
        domains=domains,
        matched_keywords=matched_keywords,
    )


def _source(
    *,
    source_tier: int = 1,
) -> SourceConfig:
    """Return source configuration for ranking tests."""

    return SourceConfig(
        id="sample_source",
        name="Sample Source",
        feed_url="tests/fixtures/sample_feed.xml",
        source_type="rss",
        source_tier=source_tier,
        default_domains=("technology",),
        language="en",
        geographic_scope=("Global",),
        active=True,
    )


def _ranking() -> RankingConfig:
    """Return controlled ranking configuration."""

    return RankingConfig(
        source_tier_scores=(
            (1, 4),
            (2, 3),
            (3, 2),
            (4, 1),
        ),
        domain_match_score=2,
        keyword_match_score=1,
    )


def test_score_uses_source_tier() -> None:
    """Source quality contributes its configured score."""

    result = score_record(
        _record(),
        _source(source_tier=1),
        _ranking(),
    )

    assert result.relevance_score == 4
    assert result.score_components == (
        ("source_tier", 4),
        ("domain_matches", 0),
        ("keyword_matches", 0),
    )


def test_domains_contribute_to_score() -> None:
    """Each assigned domain contributes the configured amount."""

    result = score_record(
        _record(
            domains=(
                "technology",
                "artificial_intelligence",
            )
        ),
        _source(),
        _ranking(),
    )

    assert result.relevance_score == 8
    assert result.score_components == (
        ("source_tier", 4),
        ("domain_matches", 4),
        ("keyword_matches", 0),
    )


def test_keywords_contribute_to_score() -> None:
    """Each matched keyword contributes the configured amount."""

    result = score_record(
        _record(
            matched_keywords=(
                "ai",
                "model release",
            )
        ),
        _source(),
        _ranking(),
    )

    assert result.relevance_score == 6
    assert result.score_components == (
        ("source_tier", 4),
        ("domain_matches", 0),
        ("keyword_matches", 2),
    )


def test_score_combines_all_current_components() -> None:
    """The provisional score combines all implemented factors."""

    result = score_record(
        _record(
            domains=(
                "technology",
                "artificial_intelligence",
            ),
            matched_keywords=(
                "ai",
                "model release",
            ),
        ),
        _source(),
        _ranking(),
    )

    assert result.relevance_score == 10
    assert result.score_components == (
        ("source_tier", 4),
        ("domain_matches", 4),
        ("keyword_matches", 2),
    )


def test_lower_source_tier_receives_lower_source_score() -> None:
    """Configured source tiers affect relevance deterministically."""

    result = score_record(
        _record(),
        _source(source_tier=4),
        _ranking(),
    )

    assert result.relevance_score == 1
    assert result.score_components[0] == (
        "source_tier",
        1,
    )


def test_existing_record_is_not_mutated() -> None:
    """Scoring returns an enriched immutable record."""

    record = _record(
        domains=("technology",),
        matched_keywords=("software",),
    )

    result = score_record(
        record,
        _source(),
        _ranking(),
    )

    assert record.relevance_score == 0
    assert record.score_components == ()

    assert result is not record
    assert result.relevance_score == 7


def test_existing_score_is_replaced_deterministically() -> None:
    """Re-scoring derives output from current data and configuration."""

    record = replace(
        _record(
            domains=("technology",),
        ),
        relevance_score=999,
        score_components=(("old", 999),),
    )

    result = score_record(
        record,
        _source(),
        _ranking(),
    )

    assert result.relevance_score == 6
    assert result.score_components == (
        ("source_tier", 4),
        ("domain_matches", 2),
        ("keyword_matches", 0),
    )