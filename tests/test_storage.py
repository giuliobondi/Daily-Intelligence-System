"""Tests for deterministic JSON Lines record persistence."""

import json
from datetime import datetime, timezone
from pathlib import Path

from daily_intelligence.models import ArticleRecord
from daily_intelligence.storage import write_records_jsonl


def _record(
    *,
    title: str = "Sample AI Release",
    published_at: datetime | None = datetime(
        2026,
        8,
        6,
        8,
        30,
        tzinfo=timezone.utc,
    ),
) -> ArticleRecord:
    """Return a processed record suitable for storage tests."""

    return ArticleRecord(
        source_id="sample_source",
        title=title,
        normalized_title=title.casefold(),
        article_url="https://example.com/article",
        normalized_url="https://example.com/article",
        published_at=published_at,
        retrieved_at=datetime(
            2026,
            8,
            6,
            9,
            0,
            tzinfo=timezone.utc,
        ),
        description="Sample description.",
        domains=(
            "technology",
            "artificial_intelligence",
        ),
        matched_keywords=(
            "ai",
            "model release",
        ),
        relevance_score=10,
        score_components=(
            ("source_tier", 4),
            ("domain_matches", 4),
            ("keyword_matches", 2),
        ),
    )


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    """Read JSON Lines test output into parsed dictionaries."""

    return [
        json.loads(line)
        for line in path.read_text(
            encoding="utf-8",
        ).splitlines()
    ]


def test_records_are_written_as_json_lines(
    tmp_path: Path,
) -> None:
    """Each processed record is written as one JSON object per line."""

    output_path = tmp_path / "records.jsonl"

    first = _record()
    second = _record(
        title="Second Story",
    )

    write_records_jsonl(
        [first, second],
        output_path,
    )

    stored = _read_jsonl(output_path)

    assert len(stored) == 2
    assert stored[0]["title"] == "Sample AI Release"
    assert stored[1]["title"] == "Second Story"


def test_processed_metadata_is_preserved(
    tmp_path: Path,
) -> None:
    """Classification and scoring evidence survive persistence."""

    output_path = tmp_path / "records.jsonl"

    write_records_jsonl(
        [_record()],
        output_path,
    )

    stored = _read_jsonl(output_path)[0]

    assert stored["domains"] == [
        "technology",
        "artificial_intelligence",
    ]
    assert stored["matched_keywords"] == [
        "ai",
        "model release",
    ]
    assert stored["relevance_score"] == 10
    assert stored["score_components"] == [
        ["source_tier", 4],
        ["domain_matches", 4],
        ["keyword_matches", 2],
    ]


def test_datetimes_are_written_as_iso_8601(
    tmp_path: Path,
) -> None:
    """Machine-readable timestamps are stored consistently."""

    output_path = tmp_path / "records.jsonl"

    write_records_jsonl(
        [_record()],
        output_path,
    )

    stored = _read_jsonl(output_path)[0]

    assert stored["published_at"] == (
        "2026-08-06T08:30:00+00:00"
    )
    assert stored["retrieved_at"] == (
        "2026-08-06T09:00:00+00:00"
    )


def test_missing_publication_time_is_stored_as_null(
    tmp_path: Path,
) -> None:
    """Unavailable publication time remains explicitly missing."""

    output_path = tmp_path / "records.jsonl"

    write_records_jsonl(
        [
            _record(
                published_at=None,
            )
        ],
        output_path,
    )

    stored = _read_jsonl(output_path)[0]

    assert stored["published_at"] is None


def test_parent_directories_are_created(
    tmp_path: Path,
) -> None:
    """Storage creates the requested output directory when necessary."""

    output_path = (
        tmp_path
        / "data"
        / "processed"
        / "records.jsonl"
    )

    write_records_jsonl(
        [_record()],
        output_path,
    )

    assert output_path.exists()


def test_empty_record_collection_creates_empty_file(
    tmp_path: Path,
) -> None:
    """A legitimate empty result produces a valid empty JSONL file."""

    output_path = tmp_path / "records.jsonl"

    write_records_jsonl(
        [],
        output_path,
    )

    assert output_path.exists()
    assert output_path.read_text(
        encoding="utf-8"
    ) == ""


def test_repeated_write_does_not_append_duplicates(
    tmp_path: Path,
) -> None:
    """Writing unchanged input twice produces unchanged storage."""

    output_path = tmp_path / "records.jsonl"
    record = _record()

    write_records_jsonl(
        [record],
        output_path,
    )

    first_content = output_path.read_text(
        encoding="utf-8",
    )

    write_records_jsonl(
        [record],
        output_path,
    )

    second_content = output_path.read_text(
        encoding="utf-8",
    )

    assert second_content == first_content
    assert len(_read_jsonl(output_path)) == 1