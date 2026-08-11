"""Orchestrate the local Daily Intelligence processing pipeline."""

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from daily_intelligence.classify import classify_record
from daily_intelligence.collect import (
    SourceCollectionResult,
    collect_source,
)
from daily_intelligence.config import (
    DomainConfig,
    RankingConfig,
    SourceConfig,
    load_domains,
    load_ranking,
    load_report,
    load_sources,
)
from daily_intelligence.deduplicate import (
    DeduplicationResult,
    deduplicate_records,
)
from daily_intelligence.filter_window import (
    filter_records_by_window,
)
from daily_intelligence.models import ArticleRecord
from daily_intelligence.normalize import normalize_entry
from daily_intelligence.rank import score_record
from daily_intelligence.report import (
    render_report,
    select_report_records,
)
from daily_intelligence.run_summary import (
    RunSummary,
    build_run_summary,
    write_run_summary_json,
)
from daily_intelligence.storage import write_records_jsonl
from daily_intelligence.validate import (
    ValidationResult,
    validate_records,
)


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PipelineResult:
    """Outputs and processing results from one local pipeline run."""

    records: tuple[ArticleRecord, ...]
    collection_results: tuple[SourceCollectionResult, ...]
    validation_result: ValidationResult
    deduplication_result: DeduplicationResult
    run_summary: RunSummary
    report: str


def run_pipeline(
    *,
    sources_path: str | Path,
    domains_path: str | Path,
    settings_path: str | Path,
    records_path: str | Path,
    report_path: str | Path,
    run_summary_path: str | Path,
    run_id: str,
    started_at: datetime,
    completed_at: datetime,
    collection_window: tuple[datetime, datetime],
    report_date: str,
) -> PipelineResult:
    """Run the deterministic local pipeline from collection to output."""

    sources = tuple(
        source
        for source in load_sources(sources_path)
        if source.active
    )

    domains = tuple(
        load_domains(domains_path)
    )

    ranking_config = load_ranking(
        settings_path
    )

    report_config = load_report(
        settings_path
    )

    logger.info(
        "Pipeline started: %s active source(s)",
        len(sources),
    )

    source_lookup = {
        source.id: source
        for source in sources
    }

    collection_results = tuple(
        collect_source(
            source,
            retrieved_at=started_at,
        )
        for source in sources
    )

    for result in collection_results:
        if result.status == "failed":
            logger.warning(
                "Source collection failed: %s (%s)",
                result.source_id,
                result.error_message,
            )
        else:
            logger.info(
                "Source collection %s: %s item(s)",
                result.source_id,
                len(result.entries),
            )

    normalized_records = _normalize_collected_entries(
        collection_results=collection_results,
        source_lookup=source_lookup,
    )

    validation_result = validate_records(
        normalized_records
    )

    logger.info(
        "Validation complete: %s valid, %s invalid",
        len(validation_result.valid_records),
        len(validation_result.invalid_records),
    )

    window_records = filter_records_by_window(
        validation_result.valid_records,
        collection_window,
    )

    logger.info(
        "Collection-window filtering complete: %s item(s) retained",
        len(window_records),
    )

    deduplication_result = deduplicate_records(
        window_records
    )

    logger.info(
        "Deduplication complete: %s unique, %s duplicate(s)",
        len(deduplication_result.unique_records),
        len(deduplication_result.duplicate_records),
    )

    processed_records = tuple(
        _classify_and_score(
            record=record,
            source=source_lookup[record.source_id],
            domains=domains,
            ranking_config=ranking_config,
        )
        for record in deduplication_result.unique_records
    )

    unclassified_count = sum(
        1
        for record in processed_records
        if not record.domains
    )

    logger.info(
        "Classification and ranking complete: "
        "%s processed, %s unclassified",
        len(processed_records),
        unclassified_count,
    )

    selected_records = select_report_records(
        records=processed_records,
        sources=sources,
        domains=domains,
        config=report_config,
    )

    write_records_jsonl(
        processed_records,
        records_path,
    )

    run_summary = build_run_summary(
        run_id=run_id,
        started_at=started_at,
        completed_at=completed_at,
        collection_window=collection_window,
        collection_results=collection_results,
        validation_result=validation_result,
        deduplication_result=deduplication_result,
        displayed_items=len(selected_records),
    )

    report = render_report(
        records=processed_records,
        sources=sources,
        domains=domains,
        config=report_config,
        report_date=report_date,
        generated_at=completed_at,
        run_summary=run_summary,
    )

    _write_report(
        report,
        report_path,
    )

    write_run_summary_json(
        run_summary,
        run_summary_path,
    )

    logger.info(
        "Outputs written: records=%s report=%s run_summary=%s",
        records_path,
        report_path,
        run_summary_path,
    )

    if run_summary.status == "degraded":
        logger.warning(
            "Pipeline completed with status: %s",
            run_summary.status,
        )
    else:
        logger.info(
            "Pipeline completed with status: %s",
            run_summary.status,
        )

    return PipelineResult(
        records=processed_records,
        collection_results=collection_results,
        validation_result=validation_result,
        deduplication_result=deduplication_result,
        run_summary=run_summary,
        report=report,
    )


def _normalize_collected_entries(
    *,
    collection_results: tuple[
        SourceCollectionResult,
        ...,
    ],
    source_lookup: dict[str, SourceConfig],
) -> tuple[ArticleRecord, ...]:
    """Normalize entries from successful source collections."""

    records: list[ArticleRecord] = []

    for result in collection_results:
        if result.status != "success":
            continue

        source = source_lookup[result.source_id]

        for entry in result.entries:
            records.append(
                normalize_entry(
                    entry,
                    source,
                    result.retrieved_at,
                )
            )

    return tuple(records)


def _classify_and_score(
    *,
    record: ArticleRecord,
    source: SourceConfig,
    domains: tuple[DomainConfig, ...],
    ranking_config: RankingConfig,
) -> ArticleRecord:
    """Classify and score one validated unique record."""

    classified = classify_record(
        record,
        source,
        domains,
    )

    return score_record(
        classified,
        source,
        ranking_config,
    )


def _write_report(
    report: str,
    path: str | Path,
) -> None:
    """Write one Markdown report to its target path."""

    output_path = Path(path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        report,
        encoding="utf-8",
    )