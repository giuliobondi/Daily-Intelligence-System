"""Tests for the Daily Intelligence command-line entry point."""

import logging
from pathlib import Path
from unittest.mock import patch


from daily_intelligence.cli import main


def test_cli_run_invokes_pipeline_with_repository_defaults() -> None:
    """The run command delegates one execution to the pipeline."""

    with (
        patch(
            "sys.argv",
            ["daily-intelligence", "run"],
        ),
        patch(
            "daily_intelligence.cli.run_pipeline"
        ) as mocked_run_pipeline,
        patch(
            "daily_intelligence.cli.logging.basicConfig"
        ) as mocked_basic_config,
    ):
        main()

        mocked_basic_config.assert_called_once_with(
            level=logging.INFO,
            format="%(levelname)s %(name)s: %(message)s",
        )

    mocked_run_pipeline.assert_called_once()

    call = mocked_run_pipeline.call_args.kwargs

    assert call["sources_path"] == "config/sources.yaml"
    assert call["domains_path"] == "config/domains.yaml"
    assert call["settings_path"] == "config/settings.yaml"

    assert isinstance(
        call["records_path"],
        Path,
    )

    assert isinstance(
        call["report_path"],
        Path,
    )

    assert isinstance(
        call["run_summary_path"],
        Path,
    )

    assert call["report_date"] in str(
        call["records_path"]
    )

    assert call["report_date"] in str(
        call["report_path"]
    )

    assert call["report_date"] in str(
        call["run_summary_path"]
    )