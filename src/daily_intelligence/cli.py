"""Command-line entry point for the Daily Intelligence pipeline."""

from argparse import ArgumentParser
from datetime import datetime, timedelta, timezone
from pathlib import Path

from daily_intelligence.pipeline import run_pipeline


def main() -> None:
    """Run the local pipeline from the command line."""

    parser = ArgumentParser(
        description="Run the Daily Intelligence pipeline."
    )

    parser.add_argument(
        "command",
        choices=("run",),
    )

    args = parser.parse_args()

    if args.command == "run":
        _run()


def _run() -> None:
    """Run one local pipeline execution using repository defaults."""

    started_at = datetime.now(timezone.utc)
    completed_at = started_at

    report_date = started_at.date().isoformat()
    run_id = started_at.strftime("%Y%m%dT%H%M%SZ")

    collection_window = (
        started_at - timedelta(hours=24),
        started_at,
    )

    year = started_at.strftime("%Y")
    month = started_at.strftime("%m")

    records_path = (
        Path("data")
        / "processed"
        / year
        / month
        / f"{report_date}.jsonl"
    )

    report_path = (
        Path("reports")
        / "daily"
        / year
        / month
        / f"{report_date}.md"
    )

    summary_path = (
        Path("data")
        / "runs"
        / year
        / month
        / f"{report_date}.json"
    )

    run_pipeline(
        sources_path="config/sources.yaml",
        domains_path="config/domains.yaml",
        settings_path="config/settings.yaml",
        records_path=records_path,
        report_path=report_path,
        run_summary_path=summary_path,
        run_id=run_id,
        started_at=started_at,
        completed_at=completed_at,
        collection_window=collection_window,
        report_date=report_date,
    )


if __name__ == "__main__":
    main()