"""Validate normalised article records before later processing."""

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable
from urllib.parse import urlsplit

from daily_intelligence.models import ArticleRecord


@dataclass(frozen=True)
class InvalidRecord:
    """One rejected article record and the reasons it was rejected."""

    record: ArticleRecord
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class ValidationResult:
    """Valid and invalid records produced by one validation pass."""

    valid_records: tuple[ArticleRecord, ...]
    invalid_records: tuple[InvalidRecord, ...]


def validate_record(record: ArticleRecord) -> tuple[str, ...]:
    """Return validation errors for one record, or an empty tuple if valid."""

    errors: list[str] = []

    if not isinstance(record.source_id, str) or not record.source_id.strip():
        errors.append("source_id must be a non-empty string")

    if not isinstance(record.title, str) or not record.title.strip():
        errors.append("title must be a non-empty string")

    if not _is_usable_article_url(record.article_url):
        errors.append(
            "article_url must be an absolute HTTP or HTTPS URL"
        )

    if not isinstance(record.retrieved_at, datetime):
        errors.append("retrieved_at must be a datetime")
    elif (
        record.retrieved_at.tzinfo is None
        or record.retrieved_at.utcoffset() is None
    ):
        errors.append("retrieved_at must be timezone-aware")

    return tuple(errors)


def validate_records(
    records: Iterable[ArticleRecord],
) -> ValidationResult:
    """Validate records independently so one invalid record does not stop others."""

    valid_records: list[ArticleRecord] = []
    invalid_records: list[InvalidRecord] = []

    for record in records:
        reasons = validate_record(record)

        if reasons:
            invalid_records.append(
                InvalidRecord(
                    record=record,
                    reasons=reasons,
                )
            )
        else:
            valid_records.append(record)

    return ValidationResult(
        valid_records=tuple(valid_records),
        invalid_records=tuple(invalid_records),
    )


def _is_usable_article_url(value: object) -> bool:
    """Return whether a value is a usable absolute web URL."""

    if not isinstance(value, str) or not value.strip():
        return False

    parts = urlsplit(value.strip())

    return (
        parts.scheme.casefold() in {"http", "https"}
        and bool(parts.netloc)
    )