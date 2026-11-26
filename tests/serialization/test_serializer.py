import pytest

from pywrite_format.serialization.serializer import Serializer
from pywrite_format.serialization.nodes import registry
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import Text, Bold, Link
from pywrite_format.styles import Alignment
from pywrite_format.serialization.assetmanager import AssetManager
from pywrite_format.exceptions.image import InvalidImageError


@pytest.fixture
def serializer():
    return Serializer(registry, AssetManager())


def test_serialize_text(serializer):
    node = Text("Hello")

    assert serializer.serialize(node) == {
        "type": "text",
        "text": "Hello",
    }


def test_serialize_paragraph(serializer):
    node = Paragraph(
        children=[],
        alignment=Alignment.RIGHT,
        indentation=0.1,
        spacing_before=0.2,
        spacing_after=0.3,
        line_spacing=1.5,
    )

    assert serializer.serialize(node) == {
        "type": "paragraph",
        "children": [],
        "alignment": Alignment.RIGHT.value,
        "indentation": 0.1,
        "spacing_before": 0.2,
        "spacing_after": 0.3,
        "line_spacing": 1.5,
    }


def test_serialize_link(serializer):
    node = Link(
        url="https://example.com",
        children=[Text("Example")],
    )

    assert serializer.serialize(node) == {
        "type": "link",
        "url": "https://example.com",
        "children": [
            {
                "type": "text",
                "text": "Example",
            }
        ],
    }


def test_serialize_nested_nodes(serializer):
    node = Paragraph(
        children=[
            Text("Hello "),
            Bold(children=[Text("World")]),
        ],
        alignment=Alignment.LEFT,
    )

    result = serializer.serialize(node)

    assert result["type"] == "paragraph"
    assert result["children"] == [
        {
            "type": "text",
            "text": "Hello ",
        },
        {
            "type": "bold",
            "children": [
                {
                    "type": "text",
                    "text": "World",
                }
            ],
        },
    ]


def test_serialize_invalid_image():
    with pytest.raises(InvalidImageError, match="Invalid or unsupported image data"):
        Image(image_data=b"fake image data")


def test_serialize_single_image(serializer):
    image_data = b"\x89PNG\r\n\x1a\n"

    node = Image(image_data=image_data)

    result = serializer.serialize(node)

    assert result == {
        "type": "image",
        "asset_path": "assets/images/image_1.png",
    }


def test_serialize_duplicate_images(serializer):
    image_data = b"\x89PNG\r\n\x1a\n"

    node = Paragraph(
        children=[
            Image(image_data=image_data),
            Image(image_data=image_data),
        ],
    )

    result = serializer.serialize(node)

    assert result["children"] == [
        {
            "type": "image",
            "asset_path": "assets/images/image_1.png",
        },
        {
            "type": "image",
            "asset_path": "assets/images/image_1.png",
        },
    ]