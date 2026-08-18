"""Tests for deterministic domain configuration loading."""

from pathlib import Path

import pytest

from daily_intelligence.config import (
    ConfigurationError,
    load_domains,
)


CONFIG_PATH = Path("config/domains.yaml")


def test_load_valid_domain_configuration() -> None:
    """A valid YAML registry becomes typed domain configuration."""

    domains = load_domains(CONFIG_PATH)

    assert len(domains) == 10

    assert tuple(domain.id for domain in domains) == (
        "global_politics_geopolitics",
        "economics_macroeconomics",
        "companies_corporate_strategy",
        "artificial_intelligence",
        "technology",
        "startups_venture_capital",
        "europe_eu",
        "financial_markets",
        "milan_bocconi_ecosystem",
        "italy",
    )

    technology = next(
        domain
        for domain in domains
        if domain.id == "technology"
    )

    assert technology.name == "Technology and Software"
    assert technology.keywords == (
        "software",
        "cloud",
        "cybersecurity",
        "developer",
        "open source",
        "api",
    )
    assert technology.active is True

    artificial_intelligence = next(
        domain
        for domain in domains
        if domain.id == "artificial_intelligence"
    )
    assert "IA" in artificial_intelligence.keywords

    companies = next(
        domain
        for domain in domains
        if domain.id == "companies_corporate_strategy"
    )
    assert "acquired" in companies.keywords
    assert "fusione e acquisizione" in companies.keywords
    assert "piano industriale" in companies.keywords

    startups = next(
        domain
        for domain in domains
        if domain.id == "startups_venture_capital"
    )
    assert "early-stage fund" in startups.keywords
    assert "funding market" in startups.keywords

    global_politics = next(
        domain
        for domain in domains
        if domain.id == "global_politics_geopolitics"
    )
    assert "tariffs" in global_politics.keywords

    startups = next(
        domain
        for domain in domains
        if domain.id == "startups_venture_capital"
    )
    assert "startup" not in startups.keywords

    financial_markets = next(
        domain
        for domain in domains
        if domain.id == "financial_markets"
    )
    assert financial_markets.name == "Financial Markets"
    assert financial_markets.active is True
    assert "stock market" in financial_markets.keywords
    assert "financial stability" in financial_markets.keywords
    assert "FOMC" in financial_markets.keywords
    assert "Federal Open Market Committee" in financial_markets.keywords
    assert "discount rate" in financial_markets.keywords
    assert "mercati dei capitali" in financial_markets.keywords

    milan_bocconi = next(
        domain
        for domain in domains
        if domain.id == "milan_bocconi_ecosystem"
    )

    assert milan_bocconi.name == "Milan and Bocconi Ecosystem"
    assert milan_bocconi.keywords == ()
    assert milan_bocconi.active is True

    assert (
        artificial_intelligence.name
        == "Artificial Intelligence"
    )
    assert artificial_intelligence.active is True

def test_missing_domain_fields_are_rejected(tmp_path: Path) -> None:
    """An incomplete domain entry fails with a clear error."""

    invalid_config = tmp_path / "invalid-domains.yaml"
    invalid_config.write_text(
        "domains:\n"
        "  - id: incomplete\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="missing required fields",
    ):
        load_domains(invalid_config)


def test_missing_domain_file_is_rejected(tmp_path: Path) -> None:
    """A nonexistent domain registry produces a configuration error."""

    missing_config = tmp_path / "missing-domains.yaml"

    with pytest.raises(
        ConfigurationError,
        match="Domain configuration file not found",
    ):
        load_domains(missing_config)


def test_domains_must_be_a_list(tmp_path: Path) -> None:
    """The top-level domains value must contain a list."""

    invalid_config = tmp_path / "invalid-domains.yaml"
    invalid_config.write_text(
        "domains: invalid\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="must contain a 'domains' list",
    ):
        load_domains(invalid_config)


def test_domain_active_flag_must_be_boolean(tmp_path: Path) -> None:
    """Domain activation must use a real YAML boolean."""

    invalid_config = tmp_path / "invalid-domains.yaml"
    invalid_config.write_text(
        "domains:\n"
        "  - id: technology\n"
        "    name: Technology\n"
        "    keywords:\n"
        "      - software\n"
        "    active: yes-please\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ConfigurationError,
        match="field 'active' must be true or false",
    ):
        load_domains(invalid_config)

def test_empty_domain_keywords_are_allowed(
    tmp_path: Path,
) -> None:
    """A domain may rely entirely on source-default classification."""

    config_path = tmp_path / "domains.yaml"

    config_path.write_text(
        """
domains:
  - id: source_defined_domain
    name: Source Defined Domain
    keywords: []
    active: true
""".strip()
        + "\n",
        encoding="utf-8",
    )

    domains = load_domains(config_path)

    assert len(domains) == 1
    assert domains[0].keywords == ()
