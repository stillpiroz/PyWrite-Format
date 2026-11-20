"""Test document metadata creation and default values."""

from datetime import datetime, timezone
from unittest.mock import patch

from pywrite_format.metadata import DocumentMetadata


def test_create_metadata_without_arguments():
    """Test that metadata is created with default values."""

    metadata = DocumentMetadata()

    assert metadata.title is None
    assert metadata.author is None
    assert metadata.description is None

    assert isinstance(metadata.created_at, datetime)
    assert isinstance(metadata.modified_at, datetime)


def test_metadata_with_custom_values():
    """Test that metadata is created with the provided values."""

    metadata = DocumentMetadata("title", "author", "description")

    assert metadata.title == "title"
    assert metadata.author == "author"
    assert metadata.description == "description"


def is_timestamp_valid(factory, attribute):
    """Check whether an instance's timestamp falls within a time range."""

    before = datetime.now(timezone.utc)

    instance = factory()

    after = datetime.now(timezone.utc)

    timestamp = getattr(instance, attribute)

    return before <= timestamp <= after


def test_created_at_initial_value():
    """Test that the initial created_at timestamp is valid."""

    assert is_timestamp_valid(DocumentMetadata, "created_at")


def test_modified_at_initial_value():
    """Test that the initial modified_at timestamp is valid."""

    before = datetime.now(timezone.utc)

    instance = DocumentMetadata()

    after = datetime.now(timezone.utc)

    assert before <= instance.modified_at <= after


def test_update_modified_at():
    """Test that updating modified_at does not change created_at."""

    original_time = datetime(2026, 1, 1, tzinfo=timezone.utc)
    updated_time = datetime(2026, 1, 2, tzinfo=timezone.utc)

    with patch("pywrite_format.metadata.datetime") as mock_datetime:
        mock_datetime.now.return_value = original_time

        metadata = DocumentMetadata()

        mock_datetime.now.return_value = updated_time

        original_created_at = metadata.created_at

        metadata.update_modified_at()

    assert metadata.modified_at == updated_time
    assert metadata.created_at == original_created_at
