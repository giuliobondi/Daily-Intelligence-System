"""Tests for deterministic ranking configuration loading."""

from pathlib import Path

import pytest

from daily_intelligence.config import (
    ConfigurationError,
    load_ranking,
)


CONFIG_PATH = Path("config/settings.yaml")


def test_load_valid_ranking_configuration() -> None:
    """Valid settings become typed ranking configuration."""

    ranking = load_ranking(CONFIG_PATH)

    assert ranking.source_tier_scores == (
        (1, 4),
        (2, 3),
        (3, 2),
        (4, 1),
    )
    assert ranking.domain_match_score == 2
    assert ranking.keyword_match_score == 1


def test_missing_settings_file_is_rejected(tmp_path: Path) -> None:
    """A nonexistent settings file produces a configuration error."""

    missing_config = tmp_path / "missing-settings.yaml"

    with pytest.raises(
        ConfigurationError,
        match="Settings configuration file not found",
    ):
        load_ranking(missing_config)


def test_ranking_must_be_a_mapping(tmp_path: Path) -> None:
    """The top-level ranking value must contain a mapping."""

    invalid_config = tmp_path / "invalid-settings.yaml"
    invalid_config.write_text(
        "ranking: invalid\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="must contain a 'ranking' mapping",
    ):
        load_ranking(invalid_config)


def test_missing_ranking_fields_are_rejected(tmp_path: Path) -> None:
    """Incomplete ranking configuration fails visibly."""

    invalid_config = tmp_path / "invalid-settings.yaml"
    invalid_config.write_text(
        "ranking:\n"
        "  domain_match_score: 2\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="missing required fields",
    ):
        load_ranking(invalid_config)


def test_all_source_tiers_must_be_configured(tmp_path: Path) -> None:
    """Ranking requires an explicit score for each supported source tier."""

    invalid_config = tmp_path / "invalid-settings.yaml"
    invalid_config.write_text(
        "ranking:\n"
        "  source_tier_scores:\n"
        "    1: 4\n"
        "    2: 3\n"
        "    3: 2\n"
        "  domain_match_score: 2\n"
        "  keyword_match_score: 1\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="must define exactly source tiers 1, 2, 3 and 4",
    ):
        load_ranking(invalid_config)


def test_negative_ranking_score_is_rejected(tmp_path: Path) -> None:
    """Provisional ranking weights cannot be negative."""

    invalid_config = tmp_path / "invalid-settings.yaml"
    invalid_config.write_text(
        "ranking:\n"
        "  source_tier_scores:\n"
        "    1: 4\n"
        "    2: 3\n"
        "    3: 2\n"
        "    4: 1\n"
        "  domain_match_score: -2\n"
        "  keyword_match_score: 1\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="must be a non-negative integer",
    ):
        load_ranking(invalid_config)


def test_boolean_ranking_score_is_rejected(tmp_path: Path) -> None:
    """YAML booleans are not silently accepted as integer scores."""

    invalid_config = tmp_path / "invalid-settings.yaml"
    invalid_config.write_text(
        "ranking:\n"
        "  source_tier_scores:\n"
        "    1: 4\n"
        "    2: 3\n"
        "    3: 2\n"
        "    4: 1\n"
        "  domain_match_score: true\n"
        "  keyword_match_score: 1\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="must be a non-negative integer",
    ):
        load_ranking(invalid_config)