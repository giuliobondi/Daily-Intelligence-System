"""Normalise raw feed entries into internal article records."""

from datetime import datetime, timezone
from time import struct_time
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from hashlib import sha256

from daily_intelligence.config import SourceConfig
from daily_intelligence.models import ArticleRecord


_TRACKING_PARAMETERS = {
    "utm_campaign",
    "utm_content",
    "utm_medium",
    "utm_source",
    "utm_term",
}


class NormalizationError(ValueError):
    """Raised when a raw feed entry cannot be normalised safely."""


def normalize_entry(
    entry: Any,
    source: SourceConfig,
    retrieved_at: datetime,
) -> ArticleRecord:
    """Convert one raw feed entry into an ArticleRecord."""

    retrieved_at_utc = _require_utc_datetime(
        retrieved_at,
        field_name="retrieved_at",
    )

    title = _require_text(entry, "title")
    article_url = _require_text(entry, "link")

    clean_title = _collapse_whitespace(title)
    description = _optional_text(entry, "description")
    normalized_url = normalize_url(article_url)

    return ArticleRecord(
        source_id=source.id,
        title=clean_title,
        normalized_title=clean_title.casefold(),
        article_url=article_url.strip(),
        normalized_url=normalize_url(article_url),
        record_id=build_record_id(
            source.id,
            normalized_url,
            ),
        published_at=_parse_publication_time(entry),
        retrieved_at=retrieved_at_utc,
        description=(
            _collapse_whitespace(description)
            if description is not None
            else None
        ),
    )


def normalize_url(url: str) -> str:
    """Remove fragments and known tracking parameters from a URL."""

    clean_url = url.strip()
    parts = urlsplit(clean_url)

    filtered_query = [
        (key, value)
        for key, value in parse_qsl(
            parts.query,
            keep_blank_values=True,
        )
        if key.casefold() not in _TRACKING_PARAMETERS
    ]

    return urlunsplit(
        (
            parts.scheme.casefold(),
            parts.netloc.casefold(),
            parts.path,
            urlencode(filtered_query, doseq=True),
            "",
        )
    )

def build_record_id(
    source_id: str,
    normalized_url: str,
) -> str:
    """Build a deterministic identifier from source and normalised URL."""

    identity = f"{source_id}\n{normalized_url}"

    return sha256(
        identity.encode("utf-8")
    ).hexdigest()

def _parse_publication_time(entry: Any) -> datetime | None:
    """Convert feedparser publication time into a UTC datetime."""

    published_parsed = getattr(entry, "published_parsed", None)

    if published_parsed is None:
        return None

    if not isinstance(published_parsed, struct_time):
        raise NormalizationError(
            "Feed entry field 'published_parsed' has an invalid type."
        )

    return datetime(
        year=published_parsed.tm_year,
        month=published_parsed.tm_mon,
        day=published_parsed.tm_mday,
        hour=published_parsed.tm_hour,
        minute=published_parsed.tm_min,
        second=published_parsed.tm_sec,
        tzinfo=timezone.utc,
    )


def _require_text(entry: Any, field: str) -> str:
    """Return a required non-empty text field from a feed entry."""

    value = getattr(entry, field, None)

    if not isinstance(value, str) or not value.strip():
        raise NormalizationError(
            f"Feed entry field {field!r} must be a non-empty string."
        )

    return value


def _optional_text(entry: Any, field: str) -> str | None:
    """Return an optional text field or None when it is unavailable."""

    value = getattr(entry, field, None)

    if value is None:
        return None

    if not isinstance(value, str):
        raise NormalizationError(
            f"Feed entry field {field!r} must be text when present."
        )

    clean_value = value.strip()

    return clean_value or None


def _collapse_whitespace(value: str) -> str:
    """Replace repeated whitespace with single spaces."""

    return " ".join(value.split())


def _require_utc_datetime(
    value: datetime,
    field_name: str,
) -> datetime:
    """Require an aware datetime and convert it to UTC."""

    if not isinstance(value, datetime):
        raise NormalizationError(
            f"{field_name} must be a datetime."
        )

    if value.tzinfo is None or value.utcoffset() is None:
        raise NormalizationError(
            f"{field_name} must be timezone-aware."
        )

    return value.astimezone(timezone.utc)
