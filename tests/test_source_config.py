"""Tests for production source configuration."""

from pathlib import Path

from daily_intelligence.config import load_sources


CONFIG_PATH = Path("config/sources.yaml")


def test_european_investment_fund_source_configuration() -> None:
    """EIF is configured as an active Tier 1 RSS source without defaults."""
    sources = load_sources(CONFIG_PATH)

    assert len(sources) == 14

    eif = next(
        source
        for source in sources
        if source.id == "european_investment_fund"
    )

    assert eif.name == "European Investment Fund"
    assert (
        eif.feed_url
        == "https://www.eif.org/press/release/index.rss"
    )
    assert eif.source_type == "rss"
    assert eif.source_tier == 1
    assert eif.default_domains == ()
    assert eif.language == "en"
    assert eif.geographic_scope == ("Europe",)
    assert eif.active is True