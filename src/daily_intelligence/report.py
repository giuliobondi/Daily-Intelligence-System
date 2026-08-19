"""Generate readable Markdown reports from processed article records."""

from datetime import datetime
from typing import Iterable

from daily_intelligence.config import (
    DomainConfig,
    ReportConfig,
    SourceConfig,
)
from daily_intelligence.models import ArticleRecord
from daily_intelligence.run_summary import RunSummary


def render_report(
    records: Iterable[ArticleRecord],
    sources: Iterable[SourceConfig],
    domains: Iterable[DomainConfig],
    config: ReportConfig,
    report_date: str,
    generated_at: datetime,
    run_summary: RunSummary | None = None,
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
    ]

    if run_summary is not None:
        window_start, window_end = run_summary.collection_window

        lines.extend(
            [
                f"Run status: {run_summary.status}",
                (
                    "Monitored window: "
                    f"{_format_datetime(window_start)} "
                    f"to {_format_datetime(window_end)}"
                ),
                (
                    "Sources: "
                    f"{run_summary.active_sources} active, "
                    f"{run_summary.successful_sources} successful, "
                    f"{run_summary.empty_sources} empty, "
                    f"{run_summary.failed_sources} failed"
                ),
                f"Items collected: {run_summary.raw_items}",
                f"Displayed items: {len(selected)}",
                "",
            ]
        )

        if run_summary.warnings:
            lines.extend(
                [
                    "## Run Warnings",
                    "",
                    *[
                        f"- {warning}"
                        for warning in run_summary.warnings
                    ],
                    "",
                ]
            )
    else:
        lines.extend(
            [
                f"Displayed items: {len(selected)}",
                "",
            ]
        )

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


    lines.extend(
        [
            "",
            (
                "**Source context:** "
                + _format_source_context(
                    record=record,
                    max_length=max_description_length,
                )
            ),
        ]
    )

    lines.append("")

    return lines


def _format_source_context(
    record: ArticleRecord,
    max_length: int,
) -> str:
    """Return bounded source-provided context for report display."""

    description = record.description

    if (
        not description
        or description.casefold().strip()
        == record.title.casefold().strip()
    ):
        return "No additional source-provided context available."

    return _truncate_source_context(
        description=description,
        max_length=max_length,
    )


def _truncate_source_context(
    description: str,
    max_length: int,
) -> str:
    """Truncate source context at a useful deterministic boundary."""

    if len(description) <= max_length:
        return description

    if max_length <= 3:
        return description[:max_length]

    available_length = max_length - 3
    candidate = description[:available_length].rstrip()

    sentence_end = max(
        candidate.rfind("."),
        candidate.rfind("!"),
        candidate.rfind("?"),
    )

    if sentence_end >= 0:
        sentence = candidate[: sentence_end + 1].rstrip()

        if sentence:
            return sentence

    word_end = candidate.rfind(" ")

    if word_end > 0:
        candidate = candidate[:word_end].rstrip()

    return candidate + "..."


def _format_datetime(value: datetime) -> str:
    """Render a timezone-aware datetime using ISO 8601."""

    return value.isoformat()