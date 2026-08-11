"""Integration tests for the local Daily Intelligence pipeline."""

import json
from datetime import datetime, timezone
from pathlib import Path
import logging

from daily_intelligence.pipeline import run_pipeline


SOURCES_PATH = Path("config/sources.yaml")
DOMAINS_PATH = Path("config/domains.yaml")
SETTINGS_PATH = Path("config/settings.yaml")

STARTED_AT = datetime(
    2026,
    8,
    6,
    9,
    0,
    tzinfo=timezone.utc,
)

COMPLETED_AT = datetime(
    2026,
    8,
    6,
    9,
    1,
    tzinfo=timezone.utc,
)

COLLECTION_WINDOW = (
    datetime(
        2026,
        8,
        5,
        9,
        0,
        tzinfo=timezone.utc,
    ),
    STARTED_AT,
)


def test_pipeline_runs_end_to_end(
    tmp_path: Path,
) -> None:
    """The controlled fixture passes through the complete local pipeline."""

    records_path = tmp_path / "processed.jsonl"
    report_path = tmp_path / "report.md"
    summary_path = tmp_path / "run-summary.json"

    result = run_pipeline(
        sources_path=SOURCES_PATH,
        domains_path=DOMAINS_PATH,
        settings_path=SETTINGS_PATH,
        records_path=records_path,
        report_path=report_path,
        run_summary_path=summary_path,
        run_id="20260806T090000Z",
        started_at=STARTED_AT,
        completed_at=COMPLETED_AT,
        collection_window=COLLECTION_WINDOW,
        report_date="2026-08-06",
    )

    assert len(result.collection_results) == 1

    collection_result = result.collection_results[0]

    assert collection_result.source_id == "sample_source"
    assert collection_result.status == "success"
    assert len(collection_result.entries) == 1

    assert len(
        result.validation_result.valid_records
    ) == 1

    assert len(
        result.validation_result.invalid_records
    ) == 0

    assert len(
        result.deduplication_result.unique_records
    ) == 1

    assert len(
        result.deduplication_result.duplicate_records
    ) == 0

    assert len(result.records) == 1

    record = result.records[0]

    assert record.source_id == "sample_source"
    assert record.title == "Sample AI Release"
    assert (
        record.normalized_title
        == "sample ai release"
    )
    assert (
        record.normalized_url
        == "https://example.com/articles/sample-ai-release"
    )
    assert record.domains == (
        "technology",
        "artificial_intelligence",
    )
    assert record.matched_keywords == ("ai",)
    assert record.relevance_score == 9
    assert record.score_components == (
        ("source_tier", 4),
        ("domain_matches", 4),
        ("keyword_matches", 1),
    )

    assert records_path.exists()

    stored_lines = records_path.read_text(
        encoding="utf-8",
    ).splitlines()

    assert len(stored_lines) == 1

    stored_record = json.loads(
        stored_lines[0]
    )

    assert (
        stored_record["source_id"]
        == "sample_source"
    )
    assert (
        stored_record["title"]
        == "Sample AI Release"
    )
    assert (
        stored_record["relevance_score"]
        == 9
    )

    assert report_path.exists()

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert stored_report == result.report

    assert (
        "# Daily Intelligence — 2026-08-06"
        in stored_report
    )

    assert (
        "Run status: success"
        in stored_report
    )

    assert (
        "Monitored window: "
        "2026-08-05T09:00:00+00:00 "
        "to 2026-08-06T09:00:00+00:00"
        in stored_report
    )

    assert (
        "Sources: 1 active, 1 successful, "
        "0 empty, 0 failed"
        in stored_report
    )

    assert (
        "Items collected: 1"
        in stored_report
    )

    assert (
        "Displayed items: 1"
        in stored_report
    )

    assert (
        "## Technology and Software"
        in stored_report
    )

    assert (
        "Sample AI Release"
        in stored_report
    )

    assert (
        "**Also:** Artificial Intelligence"
        in stored_report
    )

    assert (
        "**Relevance score:** 9"
        in stored_report
    )

    assert summary_path.exists()

    stored_summary = json.loads(
        summary_path.read_text(
            encoding="utf-8",
        )
    )

    assert result.run_summary.status == "success"
    assert result.run_summary.active_sources == 1
    assert result.run_summary.successful_sources == 1
    assert result.run_summary.failed_sources == 0
    assert result.run_summary.raw_items == 1
    assert result.run_summary.valid_items == 1
    assert result.run_summary.invalid_items == 0
    assert result.run_summary.duplicate_items == 0
    assert result.run_summary.displayed_items == 1

    assert stored_summary["status"] == "success"
    assert stored_summary["active_sources"] == 1
    assert stored_summary["successful_sources"] == 1
    assert stored_summary["failed_sources"] == 0
    assert stored_summary["raw_items"] == 1
    assert stored_summary["valid_items"] == 1
    assert stored_summary["invalid_items"] == 0
    assert stored_summary["duplicate_items"] == 0
    assert stored_summary["displayed_items"] == 1


def test_pipeline_preserves_successful_results_when_one_source_fails(
    tmp_path: Path,
) -> None:
    """One failed source degrades the run without discarding good results."""

    sources_path = tmp_path / "sources.yaml"

    sources_path.write_text(
        """
sources:
  - id: sample_source
    name: Sample Source
    feed_url: tests/fixtures/sample_feed.xml
    source_type: rss
    source_tier: 1
    default_domains:
      - technology
    language: en
    geographic_scope:
      - Global
    active: true

  - id: failing_source
    name: Failing Source
    feed_url: tests/fixtures/missing.xml
    source_type: rss
    source_tier: 1
    default_domains:
      - technology
    language: en
    geographic_scope:
      - Global
    active: true
""".strip()
        + "\n",
        encoding="utf-8",
    )

    records_path = tmp_path / "processed.jsonl"
    report_path = tmp_path / "report.md"
    summary_path = tmp_path / "run-summary.json"

    result = run_pipeline(
        sources_path=sources_path,
        domains_path=DOMAINS_PATH,
        settings_path=SETTINGS_PATH,
        records_path=records_path,
        report_path=report_path,
        run_summary_path=summary_path,
        run_id="20260806T090000Z",
        started_at=STARTED_AT,
        completed_at=COMPLETED_AT,
        collection_window=COLLECTION_WINDOW,
        report_date="2026-08-06",
    )

    assert len(result.collection_results) == 2

    results_by_source = {
        item.source_id: item
        for item in result.collection_results
    }

    successful = results_by_source[
        "sample_source"
    ]

    failed = results_by_source[
        "failing_source"
    ]

    assert successful.status == "success"

    assert failed.status == "failed"

    assert failed.error_type == "CollectionError"

    assert failed.error_message is not None

    assert (
        "Local feed file not found"
        in failed.error_message
    )

    assert len(result.records) == 1

    assert (
        result.records[0].title
        == "Sample AI Release"
    )

    assert (
        result.run_summary.status
        == "degraded"
    )

    assert (
        result.run_summary.active_sources
        == 2
    )

    assert (
        result.run_summary.successful_sources
        == 1
    )

    assert (
        result.run_summary.failed_sources
        == 1
    )

    assert (
        result.run_summary.raw_items
        == 1
    )

    assert (
        result.run_summary.displayed_items
        == 1
    )

    assert result.run_summary.warnings

    assert (
        result.run_summary.warnings[0].startswith(
            "Source failing_source failed:"
        )
    )

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert (
        "Run status: degraded"
        in stored_report
    )

    assert (
        "Sources: 2 active, 1 successful, "
        "0 empty, 1 failed"
        in stored_report
    )

    assert (
        "Items collected: 1"
        in stored_report
    )

    assert (
        "Displayed items: 1"
        in stored_report
    )

    assert (
        "## Run Warnings"
        in stored_report
    )

    assert (
        "Source failing_source failed:"
        in stored_report
    )

    assert (
        "Sample AI Release"
        in stored_report
    )

    stored_summary = json.loads(
        summary_path.read_text(
            encoding="utf-8",
        )
    )

    assert (
        stored_summary["status"]
        == "degraded"
    )

    assert (
        stored_summary["active_sources"]
        == 2
    )

    assert (
        stored_summary["successful_sources"]
        == 1
    )

    assert (
        stored_summary["failed_sources"]
        == 1
    )


def test_pipeline_excludes_records_outside_collection_window(
    tmp_path: Path,
) -> None:
    """Older publications do not enter the current report."""

    records_path = tmp_path / "processed.jsonl"
    report_path = tmp_path / "report.md"
    summary_path = tmp_path / "run-summary.json"

    current_window = (
        datetime(
            2026,
            8,
            10,
            9,
            0,
            tzinfo=timezone.utc,
        ),
        datetime(
            2026,
            8,
            11,
            9,
            0,
            tzinfo=timezone.utc,
        ),
    )

    result = run_pipeline(
        sources_path=SOURCES_PATH,
        domains_path=DOMAINS_PATH,
        settings_path=SETTINGS_PATH,
        records_path=records_path,
        report_path=report_path,
        run_summary_path=summary_path,
        run_id="20260811T090000Z",
        started_at=current_window[1],
        completed_at=current_window[1],
        collection_window=current_window,
        report_date="2026-08-11",
    )

    assert len(
        result.validation_result.valid_records
    ) == 1

    assert (
        result.deduplication_result.unique_records
        == ()
    )

    assert result.records == ()

    stored_lines = records_path.read_text(
        encoding="utf-8",
    ).splitlines()

    assert stored_lines == []

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert (
        "Run status: success"
        in stored_report
    )

    assert (
        "Monitored window: "
        "2026-08-10T09:00:00+00:00 "
        "to 2026-08-11T09:00:00+00:00"
        in stored_report
    )

    assert (
        "Items collected: 1"
        in stored_report
    )

    assert (
        "Displayed items: 0"
        in stored_report
    )

    assert (
        "Sample AI Release"
        not in stored_report
    )

    assert (
        "No classified items were selected for this report."
        in stored_report
    )

    assert (
        result.run_summary.status
        == "success"
    )

    assert (
        result.run_summary.raw_items
        == 1
    )

    assert (
        result.run_summary.valid_items
        == 1
    )

    assert (
        result.run_summary.duplicate_items
        == 0
    )

    assert (
        result.run_summary.displayed_items
        == 0
    )

def test_pipeline_emits_run_level_logs(
    tmp_path: Path,
    caplog,
) -> None:
    """The pipeline exposes useful run-level operational logs."""

    records_path = tmp_path / "processed.jsonl"
    report_path = tmp_path / "report.md"
    summary_path = tmp_path / "run-summary.json"

    with caplog.at_level(
        logging.INFO,
        logger="daily_intelligence.pipeline",
    ):
        run_pipeline(
            sources_path=SOURCES_PATH,
            domains_path=DOMAINS_PATH,
            settings_path=SETTINGS_PATH,
            records_path=records_path,
            report_path=report_path,
            run_summary_path=summary_path,
            run_id="20260806T090000Z",
            started_at=STARTED_AT,
            completed_at=COMPLETED_AT,
            collection_window=COLLECTION_WINDOW,
            report_date="2026-08-06",
        )

    messages = [
        record.getMessage()
        for record in caplog.records
    ]

    assert (
        "Pipeline started: 1 active source(s)"
        in messages
    )

    assert (
        "Source collection sample_source: 1 item(s)"
        in messages
    )

    assert (
        "Validation complete: 1 valid, 0 invalid"
        in messages
    )

    assert (
        "Collection-window filtering complete: "
        "1 item(s) retained"
        in messages
    )

    assert (
        "Deduplication complete: 1 unique, 0 duplicate(s)"
        in messages
    )

    assert (
        "Classification and ranking complete: "
        "1 processed, 0 unclassified"
        in messages
    )

    assert any(
        message.startswith("Outputs written:")
        for message in messages
    )

    assert (
        "Pipeline completed with status: success"
        in messages
    )