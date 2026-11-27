"""Provide public functions for saving and loading documents."""

from datetime import datetime

from pywrite_format.serialization.assetmanager import AssetManager
from pywrite_format.serialization.nodes import registry
from pywrite_format.serialization.package_writer import PackageWriter
from pywrite_format.serialization.serializer import Serializer
from pywrite_format.document import Document
from pywrite_format.metadata import DocumentMetadata
from pywrite_format.serialization.package_reader import PackageReader
from pywrite_format.serialization.deserializer import Deserializer


def save(document, output_path):
    """Save a document to a .pywrite file."""
    
    asset_manager = AssetManager()
    serializer = Serializer(registry, asset_manager)

    content = {
        "children": [
            serializer.serialize(child)
            for child in document.children
        ]
    }

    metadata = {
        "title": document.metadata.title,
        "author": document.metadata.author,
        "description": document.metadata.description,
        "created_at": document.metadata.created_at.isoformat(),
        "modified_at": document.metadata.modified_at.isoformat(),
    }

    writer = PackageWriter()

    writer.write(
        metadata,
        content,
        asset_manager.assets,
        output_path
    )

def load(input_path):
    """Load a document from a .pywrite file."""

    reader = PackageReader()
    package = reader.read(input_path)

    metadata = package["metadata"]
    content = package["content"]
    assets = package["assets"]

    document_metadata = DocumentMetadata(
        title=metadata["title"],
        author=metadata["author"],
        description=metadata["description"],
        created_at=datetime.fromisoformat(metadata["created_at"]),
        modified_at=datetime.fromisoformat(metadata["modified_at"]),
    )

    asset_manager = AssetManager()
    asset_manager.assets = assets

    deserializer = Deserializer(registry, asset_manager)

    document = Document(metadata=document_metadata)

    for child_data in content["children"]:
        document.add(
            deserializer.deserialize(child_data)
        )

    return document