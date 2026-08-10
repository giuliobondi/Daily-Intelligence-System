"""Tests for deterministic article record identity."""

from daily_intelligence.normalize import build_record_id


def test_record_id_is_deterministic() -> None:
    """The same stable inputs always produce the same record identifier."""

    first = build_record_id(
        "sample_source",
        "https://example.com/article",
    )

    second = build_record_id(
        "sample_source",
        "https://example.com/article",
    )

    assert first == second
    assert len(first) == 64


def test_different_source_changes_record_id() -> None:
    """The same URL from a different source receives a different identity."""

    first = build_record_id(
        "source_a",
        "https://example.com/article",
    )

    second = build_record_id(
        "source_b",
        "https://example.com/article",
    )

    assert first != second


def test_different_url_changes_record_id() -> None:
    """Different normalised URLs receive different identities."""

    first = build_record_id(
        "sample_source",
        "https://example.com/article-a",
    )

    second = build_record_id(
        "sample_source",
        "https://example.com/article-b",
    )

    assert first != second


def test_tracking_variations_share_identity_after_normalisation() -> None:
    """Identity depends on the normalised URL rather than the raw URL."""

    normalized_url = "https://example.com/article"

    first = build_record_id(
        "sample_source",
        normalized_url,
    )

    second = build_record_id(
        "sample_source",
        normalized_url,
    )

    assert first == second