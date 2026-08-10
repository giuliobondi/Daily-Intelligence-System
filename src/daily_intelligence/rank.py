"""Assign deterministic relevance scores to article records."""

from dataclasses import replace

from daily_intelligence.config import RankingConfig, SourceConfig
from daily_intelligence.models import ArticleRecord


def score_record(
    record: ArticleRecord,
    source: SourceConfig,
    ranking: RankingConfig,
) -> ArticleRecord:
    """Return a record with an explainable deterministic relevance score."""

    source_tier_scores = dict(ranking.source_tier_scores)

    source_tier_score = source_tier_scores[source.source_tier]
    domain_score = len(record.domains) * ranking.domain_match_score
    keyword_score = (
        len(record.matched_keywords)
        * ranking.keyword_match_score
    )

    score_components = (
        ("source_tier", source_tier_score),
        ("domain_matches", domain_score),
        ("keyword_matches", keyword_score),
    )

    relevance_score = sum(
        value
        for _, value in score_components
    )

    return replace(
        record,
        relevance_score=relevance_score,
        score_components=score_components,
    )