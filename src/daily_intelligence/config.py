"""Load and validate source configuration."""

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


_REQUIRED_FIELDS = {
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


def _validate_source(raw_source: Any, index: int) -> SourceConfig:
    """Validate one source entry and return a SourceConfig object."""

    if not isinstance(raw_source, dict):
        raise ConfigurationError(
            f"Source entry {index} must be a mapping."
        )

    missing_fields = _REQUIRED_FIELDS - raw_source.keys()

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

    if not isinstance(source_tier, int) or isinstance(source_tier, bool):
        raise ConfigurationError(
            f"Source entry {index} field 'source_tier' must be an integer."
        )

    if source_tier not in {1, 2, 3, 4}:
        raise ConfigurationError(
            f"Source entry {index} field 'source_tier' must be between 1 and 4."
        )

    default_domains = _require_string_list(
        raw_source, "default_domains", index
    )
    geographic_scope = _require_string_list(
        raw_source, "geographic_scope", index
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
) -> list[str]:
    """Require one field to contain a list of non-empty strings."""

    value = raw_source[field]

    if not isinstance(value, list) or not value:
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must be a non-empty list."
        )

    if not all(isinstance(item, str) and item.strip() for item in value):
        raise ConfigurationError(
            f"Source entry {index} field {field!r} "
            "must contain only non-empty strings."
        )

    return [item.strip() for item in value]