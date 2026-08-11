"""Integration tests for the local end-to-end pipeline."""

import json
from datetime import datetime, timezone
from pathlib import Path

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

def test_pipeline_runs_controlled_fixture_end_to_end(
    tmp_path: Path,
) -> None:
    """The controlled fixture completes the full local processing chain."""

    records_path = (
        tmp_path
        / "data"
        / "processed"
        / "2026-08-06.jsonl"
    )

    report_path = (
        tmp_path
        / "reports"
        / "daily"
        / "2026-08-06.md"
    )

    summary_path = (
        tmp_path
        / "data"
        / "runs"
        / "2026-08-06.json"
    )

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
    assert collection_result.items_received == 1

    assert len(result.validation_result.valid_records) == 1
    assert result.validation_result.invalid_records == ()

    assert len(result.deduplication_result.unique_records) == 1
    assert result.deduplication_result.duplicate_records == ()

    assert len(result.records) == 1

    record = result.records[0]

    assert record.source_id == "sample_source"
    assert record.title == "Sample AI Release"
    assert record.normalized_title == "sample ai release"
    assert record.normalized_url == (
        "https://example.com/articles/sample-ai-release"
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

    assert records_path.is_file()

    stored_lines = records_path.read_text(
        encoding="utf-8",
    ).splitlines()

    assert len(stored_lines) == 1

    stored_record = json.loads(
        stored_lines[0]
    )

    assert stored_record["source_id"] == "sample_source"
    assert stored_record["title"] == "Sample AI Release"
    assert stored_record["domains"] == [
        "technology",
        "artificial_intelligence",
    ]
    assert stored_record["matched_keywords"] == ["ai"]
    assert stored_record["relevance_score"] == 9

    assert report_path.is_file()

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert stored_report == result.report
    assert "# Daily Intelligence — 2026-08-06" in stored_report
    assert "Displayed items: 1" in stored_report
    assert "## Technology and Software" in stored_report
    assert "Sample AI Release" in stored_report
    assert "**Also:** Artificial Intelligence" in stored_report
    assert "**Relevance score:** 9" in stored_report

    assert summary_path.is_file()

    stored_summary = json.loads(
        summary_path.read_text(
            encoding="utf-8",
        )
    )

    assert result.run_summary.status == "success"
    assert result.run_summary.active_sources == 1
    assert result.run_summary.successful_sources == 1
    assert result.run_summary.empty_sources == 0
    assert result.run_summary.failed_sources == 0
    assert result.run_summary.raw_items == 1
    assert result.run_summary.valid_items == 1
    assert result.run_summary.invalid_items == 0
    assert result.run_summary.duplicate_items == 0
    assert result.run_summary.displayed_items == 1
    assert result.run_summary.warnings == ()

    assert stored_summary["status"] == "success"
    assert stored_summary["raw_items"] == 1
    assert stored_summary["valid_items"] == 1
    assert stored_summary["displayed_items"] == 1


def test_pipeline_preserves_successful_results_when_one_source_fails(
    tmp_path: Path,
) -> None:
    """One failed source degrades the run without losing successful results."""

    sources_path = tmp_path / "sources.yaml"
    sources_path.write_text(
        "sources:\n"
        "  - id: sample_source\n"
        "    name: Sample Source\n"
        "    feed_url: tests/fixtures/sample_feed.xml\n"
        "    source_type: rss\n"
        "    source_tier: 1\n"
        "    default_domains:\n"
        "      - technology\n"
        "    language: en\n"
        "    geographic_scope:\n"
        "      - Global\n"
        "    active: true\n"
        "  - id: failing_source\n"
        "    name: Failing Source\n"
        "    feed_url: tests/fixtures/missing.xml\n"
        "    source_type: rss\n"
        "    source_tier: 2\n"
        "    default_domains:\n"
        "      - technology\n"
        "    language: en\n"
        "    geographic_scope:\n"
        "      - Global\n"
        "    active: true\n",
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
        collection_result.source_id: collection_result
        for collection_result in result.collection_results
    }

    assert results_by_source["sample_source"].status == "success"
    assert results_by_source["sample_source"].items_received == 1

    assert results_by_source["failing_source"].status == "failed"
    assert results_by_source["failing_source"].items_received == 0
    assert (
        "Local feed file not found"
        in results_by_source["failing_source"].error_message
    )

    assert len(result.records) == 1
    assert result.records[0].title == "Sample AI Release"

    assert result.run_summary.status == "degraded"
    assert result.run_summary.active_sources == 2
    assert result.run_summary.successful_sources == 1
    assert result.run_summary.failed_sources == 1
    assert result.run_summary.raw_items == 1
    assert result.run_summary.displayed_items == 1

    assert len(result.run_summary.warnings) == 1
    assert result.run_summary.warnings[0].startswith(
        "Source failing_source failed:"
    )

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert "Sample AI Release" in stored_report
    assert "Displayed items: 1" in stored_report

    stored_summary = json.loads(
        summary_path.read_text(
            encoding="utf-8",
        )
    )

    assert stored_summary["status"] == "degraded"
    assert stored_summary["successful_sources"] == 1
    assert stored_summary["failed_sources"] == 1

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

    assert len(result.validation_result.valid_records) == 1
    assert result.deduplication_result.unique_records == ()
    assert result.records == ()

    stored_lines = records_path.read_text(
        encoding="utf-8",
    ).splitlines()

    assert stored_lines == []

    stored_report = report_path.read_text(
        encoding="utf-8",
    )

    assert "Displayed items: 0" in stored_report
    assert "Sample AI Release" not in stored_report
    assert (
        "No classified items were selected for this report."
        in stored_report
    )

    assert result.run_summary.status == "success"
    assert result.run_summary.raw_items == 1
    assert result.run_summary.valid_items == 1
    assert result.run_summary.duplicate_items == 0
    assert result.run_summary.displayed_items == 0