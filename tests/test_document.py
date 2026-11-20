"""Test document creation and block management."""

from pywrite_format.document import Document
from pywrite_format.metadata import DocumentMetadata


def test_document_children_are_empty():
    """Test that a new document has no children."""

    document = Document()

    assert document.children == []


def test_document_metadata_default():
    """Test that a new document has default metadata."""

    document = Document()

    assert isinstance(document.metadata, DocumentMetadata)


def test_document_with_custom_metadata():
    """Test that a document uses the provided metadata."""

    metadata = DocumentMetadata(title="My Document")

    document = Document(metadata=metadata)

    assert document.metadata is metadata


def test_add_block_to_document():
    """Test that a block is added to the document."""

    document = Document()

    block = "test"
    document.add(block)

    assert document.children == [block]


def test_add_multiple_blocks_to_document():
    """Test that multiple blocks are added in order."""

    document = Document()

    first_block = "first"
    second_block = "second"

    document.add(first_block)
    document.add(second_block)

    assert document.children == [first_block, second_block]
