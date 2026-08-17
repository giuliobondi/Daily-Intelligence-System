"""Load and validate project configuration."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class ConfigurationError(ValueError):
    """Raised when project configuration is missing or invalid."""


@dataclass(frozen=True)
class SourceConfig:
    """Validated configuration for one information source."""

    id: str
    name: str
    feed_url: str
    source_type: str
    source_tier: int
    default_domains: tuple[str, ...]
    language: str
    geographic_scope: tuple[str, ...]
    active: bool


_SOURCE_REQUIRED_FIELDS = {
    "id",
    "name",
    "feed_url",
    "source_type",
    "source_tier",
    "default_domains",
    "language",
    "geographic_scope",
    "active",
}

_DOMAIN_REQUIRED_FIELDS = {
    "id",
    "name",
    "keywords",
    "active",
}

_RANKING_REQUIRED_FIELDS = {
    "source_tier_scores",
    "domain_match_score",
    "keyword_match_score",
}

_REPORT_REQUIRED_FIELDS = {
    "max_items_per_domain",
    "max_total_items",
    "max_description_length",
}


@dataclass(frozen=True)
class DomainConfig:
    """Validated configuration for one information domain."""

    id: str
    name: str
    keywords: tuple[str, ...]
    active: bool


@dataclass(frozen=True)
class RankingConfig:
    """Validated configuration for provisional relevance scoring."""

    source_tier_scores: tuple[tuple[int, int], ...]
    domain_match_score: int
    keyword_match_score: int


@dataclass(frozen=True)
class ReportConfig:
    """Validated configuration for Markdown report generation."""

    max_items_per_domain: int
    max_total_items: int
    max_description_length: int


def load_sources(path: str | Path) -> list[SourceConfig]:
    """Load and validate all source entries from a YAML file."""

    config_path = Path(path)

    try:
        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as error:
        raise ConfigurationError(
            f"Source configuration file not found: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigurationError(
            f"Source configuration contains invalid YAML: {config_path}"
        ) from error

    if not isinstance(data, dict):
        raise ConfigurationError(
            "Source configuration must contain a top-level mapping."
        )

    raw_sources = data.get("sources")

    if not isinstance(raw_sources, list):
        raise ConfigurationError(
            "Source configuration must contain a 'sources' list."
        )

    sources = [
        _validate_source(raw_source, index)
        for index, raw_source in enumerate(raw_sources)
    ]

    return sources


def load_domains(path: str | Path) -> list[DomainConfig]:
    """Load and validate all domain entries from a YAML file."""

    config_path = Path(path)

    try:
        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as error:
        raise ConfigurationError(
            f"Domain configuration file not found: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigurationError(
            f"Domain configuration contains invalid YAML: {config_path}"
        ) from error

    if not isinstance(data, dict):
        raise ConfigurationError(
            "Domain configuration must contain a top-level mapping."
        )

    raw_domains = data.get("domains")

    if not isinstance(raw_domains, list):
        raise ConfigurationError(
            "Domain configuration must contain a 'domains' list."
        )

    domains = [
        _validate_domain(raw_domain, index)
        for index, raw_domain in enumerate(raw_domains)
    ]

    return domains


def load_ranking(path: str | Path) -> RankingConfig:
    """Load and validate provisional ranking configuration."""

    config_path = Path(path)

    try:
        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as error:
        raise ConfigurationError(
            f"Settings configuration file not found: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigurationError(
            f"Settings configuration contains invalid YAML: {config_path}"
        ) from error

    if not isinstance(data, dict):
        raise ConfigurationError(
            "Settings configuration must contain a top-level mapping."
        )

    raw_ranking = data.get("ranking")

    if not isinstance(raw_ranking, dict):
        raise ConfigurationError(
            "Settings configuration must contain a 'ranking' mapping."
        )

    missing_fields = _RANKING_REQUIRED_FIELDS - raw_ranking.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ConfigurationError(
            f"Ranking configuration is missing required fields: {missing}"
        )

    source_tier_scores = _validate_source_tier_scores(
        raw_ranking["source_tier_scores"]
    )

    domain_match_score = _require_non_negative_integer(
        raw_ranking["domain_match_score"],
        "domain_match_score",
    )

    keyword_match_score = _require_non_negative_integer(
        raw_ranking["keyword_match_score"],
        "keyword_match_score",
    )

    return RankingConfig(
        source_tier_scores=source_tier_scores,
        domain_match_score=domain_match_score,
        keyword_match_score=keyword_match_score,
    )


def _validate_source(
    raw_source: Any,
    index: int,
) -> SourceConfig:
    """Validate one source entry and return a SourceConfig object."""

    if not isinstance(raw_source, dict):
        raise ConfigurationError(
            f"Source entry {index} must be a mapping."
        )

    missing_fields = _SOURCE_REQUIRED_FIELDS - raw_source.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ConfigurationError(
            f"Source entry {index} is missing required fields: {missing}"
        )

    _require_non_empty_string(raw_source, "id", index)
    _require_non_empty_string(raw_source, "name", index)
    _require_non_empty_string(raw_source, "feed_url", index)
    _require_non_empty_string(raw_source, "language", index)

    source_type = raw_source["source_type"]

    if source_type not in {"rss", "atom"}:
        raise ConfigurationError(
            f"Source entry {index} has unsupported source_type: "
            f"{source_type!r}"
        )

    source_tier = raw_source["source_tier"]

    if not isinstance(source_tier, int) or isinstance(
        source_tier,
        bool,
    ):
        raise ConfigurationError(
            f"Source entry {index} field 'source_tier' "
            "must be an integer."
        )

    if source_tier not in {1, 2, 3, 4}:
        raise ConfigurationError(
            f"Source entry {index} field 'source_tier' "
            "must be between 1 and 4."
        )

    default_domains = _require_string_list(
        raw_source,
        "default_domains",
        index,
        allow_empty=True,
    )

    geographic_scope = _require_string_list(
        raw_source,
        "geographic_scope",
        index,
    )

    active = raw_source["active"]

    if not isinstance(active, bool):
        raise ConfigurationError(
            f"Source entry {index} field 'active' must be true or false."
        )

    return SourceConfig(
        id=raw_source["id"].strip(),
        name=raw_source["name"].strip(),
        feed_url=raw_source["feed_url"].strip(),
        source_type=source_type,
        source_tier=source_tier,
        default_domains=tuple(default_domains),
        language=raw_source["language"].strip(),
        geographic_scope=tuple(geographic_scope),
        active=active,
    )


def _validate_domain(
    raw_domain: Any,
    index: int,
) -> DomainConfig:
    """Validate one domain entry and return a DomainConfig object."""

    if not isinstance(raw_domain, dict):
        raise ConfigurationError(
            f"Domain entry {index} must be a mapping."
        )

    missing_fields = _DOMAIN_REQUIRED_FIELDS - raw_domain.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ConfigurationError(
            f"Domain entry {index} is missing required fields: {missing}"
        )

    _require_non_empty_string(raw_domain, "id", index)
    _require_non_empty_string(raw_domain, "name", index)

    keywords = _require_string_list(
        raw_domain,
        "keywords",
        index,
        allow_empty=True,
    )

    active = raw_domain["active"]

    if not isinstance(active, bool):
        raise ConfigurationError(
            f"Domain entry {index} field 'active' must be true or false."
        )

    return DomainConfig(
        id=raw_domain["id"].strip(),
        name=raw_domain["name"].strip(),
        keywords=tuple(keywords),
        active=active,
    )


def _require_non_empty_string(
    raw_source: dict[str, Any],
    field: str,
    index: int,
) -> None:
    """Require one field to contain a non-empty string."""

    value = raw_source[field]

    if not isinstance(value, str) or not value.strip():
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must be a non-empty string."
        )


def _require_string_list(
    raw_source: dict[str, Any],
    field: str,
    index: int,
    *,
    allow_empty: bool = False,
) -> list[str]:
    """Require one field to contain a valid list of strings."""

    value = raw_source[field]

    if not isinstance(value, list):
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must be a list."
        )

    if not value and not allow_empty:
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must be a non-empty list."
        )

    if not all(
        isinstance(item, str) and item.strip()
        for item in value
    ):
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must contain only non-empty strings."
        )

    return [
        item.strip()
        for item in value
    ]


def _validate_source_tier_scores(
    value: Any,
) -> tuple[tuple[int, int], ...]:
    """Validate configured scores for source tiers 1 through 4."""

    if not isinstance(value, dict):
        raise ConfigurationError(
            "Ranking field 'source_tier_scores' must be a mapping."
        )

    expected_tiers = {1, 2, 3, 4}

    if set(value.keys()) != expected_tiers:
        raise ConfigurationError(
            "Ranking field 'source_tier_scores' "
            "must define exactly source tiers 1, 2, 3 and 4."
        )

    scores: list[tuple[int, int]] = []

    for tier in sorted(expected_tiers):
        score = _require_non_negative_integer(
            value[tier],
            f"source_tier_scores[{tier}]",
        )
        scores.append((tier, score))

    return tuple(scores)


def _require_non_negative_integer(
    value: Any,
    field: str,
) -> int:
    """Require a ranking value to be a non-negative integer."""

    if (
        not isinstance(value, int)
        or isinstance(value, bool)
        or value < 0
    ):
        raise ConfigurationError(
            f"Ranking field {field!r} "
            "must be a non-negative integer."
        )

    return value


def load_report(path: str | Path) -> ReportConfig:
    """Load and validate report configuration."""

    config_path = Path(path)

    try:
        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as error:
        raise ConfigurationError(
            f"Settings configuration file not found: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigurationError(
            f"Settings configuration contains invalid YAML: "
            f"{config_path}"
        ) from error

    if not isinstance(data, dict):
        raise ConfigurationError(
            "Settings configuration must contain a top-level mapping."
        )

    raw_report = data.get("report")

    if not isinstance(raw_report, dict):
        raise ConfigurationError(
            "Settings configuration must contain a 'report' mapping."
        )

    missing_fields = _REPORT_REQUIRED_FIELDS - raw_report.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ConfigurationError(
            f"Report configuration is missing required fields: {missing}"
        )

    return ReportConfig(
        max_items_per_domain=_require_positive_integer(
            raw_report["max_items_per_domain"],
            "max_items_per_domain",
        ),
        max_total_items=_require_positive_integer(
            raw_report["max_total_items"],
            "max_total_items",
        ),
        max_description_length=_require_positive_integer(
            raw_report["max_description_length"],
            "max_description_length",
        ),
    )


def _require_positive_integer(
    value: Any,
    field: str,
) -> int:
    """Require a configuration value to be a positive integer."""

    if (
        not isinstance(value, int)
        or isinstance(value, bool)
        or value <= 0
    ):
        raise ConfigurationError(
            f"Report field {field!r} must be a positive integer."
        )

    return value