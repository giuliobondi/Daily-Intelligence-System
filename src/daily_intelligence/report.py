"""Generate readable Markdown reports from processed article records."""

from datetime import datetime
from typing import Iterable

from daily_intelligence.config import (
    DomainConfig,
    ReportConfig,
    SourceConfig,
)
from daily_intelligence.models import ArticleRecord


def render_report(
    records: Iterable[ArticleRecord],
    sources: Iterable[SourceConfig],
    domains: Iterable[DomainConfig],
    config: ReportConfig,
    report_date: str,
    generated_at: datetime,
) -> str:
    """Render processed article records as a deterministic Markdown report."""

    source_list = tuple(sources)
    domain_list = tuple(
        domain
        for domain in domains
        if domain.active
    )

    source_lookup = {
        source.id: source
        for source in source_list
    }

    domain_lookup = {
        domain.id: domain
        for domain in domain_list
    }

    selected = select_report_records(
        records=records,
        sources=source_list,
        domains=domain_list,
        config=config,
    )

    sections: dict[str, list[ArticleRecord]] = {
        domain.id: []
        for domain in domain_list
    }

    for record in selected:
        primary_domain = record.domains[0]
        sections[primary_domain].append(record)

    lines = [
        f"# Daily Intelligence — {report_date}",
        "",
        f"Generated: {_format_datetime(generated_at)}",
        f"Displayed items: {len(selected)}",
        "",
    ]

    if not selected:
        lines.extend(
            [
                "No classified items were selected for this report.",
                "",
            ]
        )
        return "\n".join(lines)

    for domain in domain_list:
        domain_records = sections[domain.id]

        if not domain_records:
            continue

        lines.extend(
            [
                f"## {domain.name}",
                "",
            ]
        )

        for record in domain_records:
            source = source_lookup[record.source_id]

            lines.extend(
                _render_story(
                    record=record,
                    source=source,
                    domain_lookup=domain_lookup,
                    max_description_length=config.max_description_length,
                )
            )

    return "\n".join(lines)


def select_report_records(
    records: Iterable[ArticleRecord],
    sources: Iterable[SourceConfig],
    domains: Iterable[DomainConfig],
    config: ReportConfig,
) -> tuple[ArticleRecord, ...]:
    """Return the processed records that should appear in the report."""

    source_lookup = {
        source.id: source
        for source in sources
    }

    domain_lookup = {
        domain.id: domain
        for domain in domains
        if domain.active
    }

    eligible = [
        record
        for record in records
        if (
            record.source_id in source_lookup
            and record.domains
            and record.domains[0] in domain_lookup
        )
    ]

    ranked = sorted(
        eligible,
        key=lambda record: _ranking_key(
            record,
            source_lookup[record.source_id],
        ),
    )

    selected: list[ArticleRecord] = []
    domain_counts: dict[str, int] = {}

    for record in ranked:
        if len(selected) >= config.max_total_items:
            break

        primary_domain = record.domains[0]
        current_count = domain_counts.get(primary_domain, 0)

        if current_count >= config.max_items_per_domain:
            continue

        selected.append(record)
        domain_counts[primary_domain] = current_count + 1

    return tuple(selected)


def _ranking_key(
    record: ArticleRecord,
    source: SourceConfig,
) -> tuple[object, ...]:
    """Return a stable deterministic ordering key."""

    published_at = (
        record.published_at.timestamp()
        if record.published_at is not None
        else float("-inf")
    )

    return (
        -record.relevance_score,
        -published_at,
        source.source_tier,
        record.normalized_title,
        record.record_id,
    )


def _render_story(
    record: ArticleRecord,
    source: SourceConfig,
    domain_lookup: dict[str, DomainConfig],
    max_description_length: int,
) -> list[str]:
    """Render one processed record as Markdown."""

    publication_time = (
        _format_datetime(record.published_at)
        if record.published_at is not None
        else "Publication time unavailable"
    )

    lines = [
        f"### [{record.title}]({record.article_url})",
        "",
        (
            f"**Source:** {source.name}  \n"
            f"**Published:** {publication_time}  \n"
            f"**Relevance score:** {record.relevance_score}"
        ),
    ]

    secondary_domains = [
        domain_lookup[domain_id].name
        for domain_id in record.domains[1:]
        if domain_id in domain_lookup
    ]

    if secondary_domains:
        lines.append(
            f"**Also:** {', '.join(secondary_domains)}"
        )

    if record.description:
        lines.extend(
            [
                "",
                _truncate_description(
                    record.description,
                    max_description_length,
                ),
            ]
        )

    lines.append("")

    return lines


def _truncate_description(
    description: str,
    max_length: int,
) -> str:
    """Truncate feed-provided text without generating new content."""

    if len(description) <= max_length:
        return description

    if max_length <= 3:
        return description[:max_length]

    return description[: max_length - 3].rstrip() + "..."


def _format_datetime(value: datetime) -> str:
    """Render a timezone-aware datetime using ISO 8601."""

    return value.isoformat()