"""Core data models for the daily intelligence pipeline."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ArticleRecord:
    """One normalised article record produced from a source entry."""

    source_id: str
    title: str
    normalized_title: str
    article_url: str
    normalized_url: str
    published_at: datetime | None
    retrieved_at: datetime
    description: str | None