import json
import zipfile

from pywrite_format.document import Document
from pywrite_format.document_io import save, load
from pywrite_format.metadata import DocumentMetadata
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import Text, Bold, Italic, Link


def test_save_document(tmp_path):
    document = Document()

    paragraph = Paragraph(
        children=[Text("Hello World")]
    )

    document.add(paragraph)

    output_path = tmp_path / "test.pywrite"

    save(document, output_path)

    assert output_path.exists()

    with zipfile.ZipFile(output_path, "r") as archive:
        metadata = json.loads(
            archive.read("metadata.json")
        )

        content = json.loads(
            archive.read("content.json")
        )

    assert metadata["title"] == document.metadata.title
    assert metadata["author"] == document.metadata.author
    assert metadata["description"] == document.metadata.description

    assert metadata["created_at"] == document.metadata.created_at.isoformat()
    assert metadata["modified_at"] == document.metadata.modified_at.isoformat()

    assert content == {
        "children": [
            {
                "type": "paragraph",
                "children": [
                    {
                        "type": "text",
                        "text": "Hello World"
                    }
                ],
                "alignment": "left",
                "indentation": 0,
                "spacing_before": 0,
                "spacing_after": 0,
                "line_spacing": 1
            }
        ]
    }


def test_document_round_trip(tmp_path):
    metadata = DocumentMetadata(
        title="Round Trip Test",
        author="Piroz",
        description="Testing document serialization"
    )

    document = Document(metadata=metadata)

    paragraph = Paragraph(
        children=[
            Text("Hello "),
            Bold([
                Text("World"),
                Italic([Text("!")])
            ]),
            Link(
                url="https://example.com",
                children=[Text(" Example")]
            )
        ]
    )

    image_data = b"\x89PNG\r\n\x1a\n"

    document.add(paragraph)
    document.add(Image(image_data))

    output_path = tmp_path / "round_trip.pywrite"

    save(document, output_path)
    loaded_document = load(output_path)

    # Metadata
    assert loaded_document.metadata.title == metadata.title
    assert loaded_document.metadata.author == metadata.author
    assert loaded_document.metadata.description == metadata.description
    assert loaded_document.metadata.created_at == metadata.created_at
    assert loaded_document.metadata.modified_at == metadata.modified_at

    # Document structure
    assert len(loaded_document.children) == 2

    loaded_paragraph = loaded_document.children[0]

    assert isinstance(loaded_paragraph, Paragraph)
    assert isinstance(loaded_paragraph.children[0], Text)
    assert isinstance(loaded_paragraph.children[1], Bold)
    assert isinstance(loaded_paragraph.children[2], Link)

    # Image
    loaded_image = loaded_document.children[1]

    assert isinstance(loaded_image, Image)
    assert loaded_image.image_data == image_data


def test_public_api():
    from pywrite_format import (
        Document,
        DocumentMetadata,
        save,
        load,
    )

    assert callable(save)
    assert callable(load)
    assert Document is not None
    assert DocumentMetadata is not None