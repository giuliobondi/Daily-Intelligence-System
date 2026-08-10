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