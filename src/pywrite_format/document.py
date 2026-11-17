"""Define the document class and its content management."""


from pywrite_format.metadata import DocumentMetadata


class Document:
    """Represents a document containing metadata and content blocks."""

    def __init__(self, metadata=None):
        if metadata is None:
            self.metadata = DocumentMetadata()
        else:
            self.metadata = metadata
            
        self.children = []

    def add(self, block):
        self.children.append(block)
