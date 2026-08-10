"""Classify article records using deterministic domain rules."""

from dataclasses import replace
import re
from typing import Iterable

from daily_intelligence.config import DomainConfig, SourceConfig
from daily_intelligence.models import ArticleRecord


def classify_record(
    record: ArticleRecord,
    source: SourceConfig,
    domains: Iterable[DomainConfig],
) -> ArticleRecord:
    """Return a record with deterministic domain classification evidence."""

    active_domains = {
        domain.id: domain
        for domain in domains
        if domain.active
    }

    assigned_domains: list[str] = []
    matched_keywords: list[str] = []

    for domain_id in source.default_domains:
        if domain_id in active_domains:
            _append_unique(assigned_domains, domain_id)

    searchable_text = " ".join(
        part
        for part in (
            record.title,
            record.description,
        )
        if part
    )

    for domain in active_domains.values():
        domain_matched = False

        for keyword in domain.keywords:
            if _contains_keyword(searchable_text, keyword):
                _append_unique(matched_keywords, keyword)
                domain_matched = True

        if domain_matched:
            _append_unique(assigned_domains, domain.id)

    return replace(
        record,
        domains=tuple(assigned_domains),
        matched_keywords=tuple(matched_keywords),
    )


def _contains_keyword(text: str, keyword: str) -> bool:
    """Match a keyword case-insensitively without partial-word matches."""

    pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"

    return re.search(
        pattern,
        text,
        flags=re.IGNORECASE,
    ) is not None


def _append_unique(values: list[str], value: str) -> None:
    """Append a value while preserving deterministic insertion order."""

    if value not in values:
        values.append(value)