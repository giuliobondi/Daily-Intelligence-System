"""Persist processed article records as JSON Lines."""

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

from daily_intelligence.models import ArticleRecord


def write_records_jsonl(
    records: Iterable[ArticleRecord],
    path: str | Path,
) -> None:
    """Write processed article records to a JSON Lines file."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        json.dumps(
            _record_to_dict(record),
            ensure_ascii=False,
            sort_keys=True,
        )
        for record in records
    ]

    content = "\n".join(lines)

    if lines:
        content += "\n"

    output_path.write_text(
        content,
        encoding="utf-8",
    )


def _record_to_dict(record: ArticleRecord) -> dict[str, object]:
    """Convert one ArticleRecord into JSON-serialisable data."""

    data = asdict(record)

    data["published_at"] = _serialize_datetime(
        record.published_at
    )
    data["retrieved_at"] = _serialize_datetime(
        record.retrieved_at
    )

    return data


def _serialize_datetime(
    value: datetime | None,
) -> str | None:
    """Serialise a datetime using ISO 8601."""

    if value is None:
        return None

    return value.isoformat()