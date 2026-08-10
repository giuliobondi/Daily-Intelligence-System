"""Reduce exact duplicate article records deterministically."""

from dataclasses import dataclass
from typing import Iterable

from daily_intelligence.models import ArticleRecord


@dataclass(frozen=True)
class DuplicateRecord:
    """One suppressed duplicate and the retained record it matches."""

    record: ArticleRecord
    duplicate_of: ArticleRecord
    reason: str


@dataclass(frozen=True)
class DeduplicationResult:
    """Unique and duplicate records produced by one deduplication pass."""

    unique_records: tuple[ArticleRecord, ...]
    duplicate_records: tuple[DuplicateRecord, ...]


def deduplicate_records(
    records: Iterable[ArticleRecord],
) -> DeduplicationResult:
    """Suppress exact URL or title duplicates while preserving first occurrence."""

    unique_records: list[ArticleRecord] = []
    duplicate_records: list[DuplicateRecord] = []

    records_by_url: dict[str, ArticleRecord] = {}
    records_by_title: dict[str, ArticleRecord] = {}

    for record in records:
        url_match = records_by_url.get(record.normalized_url)

        if url_match is not None:
            duplicate_records.append(
                DuplicateRecord(
                    record=record,
                    duplicate_of=url_match,
                    reason="normalized_url",
                )
            )
            continue

        title_match = records_by_title.get(record.normalized_title)

        if title_match is not None:
            duplicate_records.append(
                DuplicateRecord(
                    record=record,
                    duplicate_of=title_match,
                    reason="normalized_title",
                )
            )
            continue

        unique_records.append(record)
        records_by_url[record.normalized_url] = record
        records_by_title[record.normalized_title] = record

    return DeduplicationResult(
        unique_records=tuple(unique_records),
        duplicate_records=tuple(duplicate_records),
    )