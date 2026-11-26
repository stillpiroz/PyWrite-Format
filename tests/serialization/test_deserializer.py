import pytest

from pywrite_format.serialization.deserializer import Deserializer
from pywrite_format.serialization.nodes import registry
from pywrite_format.serialization.assetmanager import AssetManager
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import Text, Bold, Link
from pywrite_format.styles import Alignment


@pytest.fixture
def asset_manager():
    return AssetManager()


@pytest.fixture
def deserializer(asset_manager):
    return Deserializer(registry, asset_manager)


def test_deserialize_text(deserializer):
    data = {
        "type": "text",
        "text": "Hello",
    }

    node = deserializer.deserialize(data)

    assert isinstance(node, Text)
    assert node.text == "Hello"


def test_deserialize_paragraph(deserializer):
    data = {
        "type": "paragraph",
        "children": [],
        "alignment": "right",
        "indentation": 0.1,
        "spacing_before": 0.2,
        "spacing_after": 0.3,
        "line_spacing": 1.5,
    }

    node = deserializer.deserialize(data)

    assert isinstance(node, Paragraph)
    assert node.alignment == Alignment.RIGHT
    assert node.indentation == 0.1
    assert node.spacing_before == 0.2
    assert node.spacing_after == 0.3
    assert node.line_spacing == 1.5
    assert node.children == []


def test_deserialize_link(deserializer):
    data = {
        "type": "link",
        "url": "https://example.com",
        "children": [
            {
                "type": "text",
                "text": "Example",
            }
        ],
    }

    node = deserializer.deserialize(data)

    assert isinstance(node, Link)
    assert node.url == "https://example.com"
    assert len(node.children) == 1
    assert isinstance(node.children[0], Text)
    assert node.children[0].text == "Example"


def test_deserialize_nested_nodes(deserializer):
    data = {
        "type": "paragraph",
        "children": [
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
        ],
        "alignment": "left",
        "indentation": 0,
        "spacing_before": 0,
        "spacing_after": 0,
        "line_spacing": 1,
    }

    node = deserializer.deserialize(data)

    assert isinstance(node, Paragraph)
    assert isinstance(node.children[0], Text)
    assert node.children[0].text == "Hello "

    assert isinstance(node.children[1], Bold)
    assert isinstance(node.children[1].children[0], Text)
    assert node.children[1].children[0].text == "World"


def test_deserialize_image(asset_manager):
    image_data = b"\x89PNG\r\n\x1a\n"
    asset_path = asset_manager.add(image_data)

    deserializer = Deserializer(registry, asset_manager)

    data = {
        "type": "image",
        "asset_path": asset_path,
    }

    node = deserializer.deserialize(data)

    assert isinstance(node, Image)
    assert node.image_data == image_data


def test_deserialize_unknown_node(deserializer):
    data = {
        "type": "unknown",
    }

    with pytest.raises(ValueError, match="Unknown node type"):
        deserializer.deserialize(data)