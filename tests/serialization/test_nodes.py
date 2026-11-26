from pywrite_format.serialization.nodes import registry
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import (
    Text,
    Bold,
    Italic,
    Underline,
    Strikethrough,
    Code,
    Link,
)


def test_registered_blocks():
    assert registry.get("paragraph") is Paragraph
    assert registry.get("image") is Image


def test_registered_inlines():
    assert registry.get("text") is Text
    assert registry.get("bold") is Bold
    assert registry.get("italic") is Italic
    assert registry.get("underline") is Underline
    assert registry.get("strikethrough") is Strikethrough
    assert registry.get("code") is Code
    assert registry.get("link") is Link


def test_get_registered_names():
    assert registry.get_name(Paragraph) == "paragraph"
    assert registry.get_name(Image) == "image"

    assert registry.get_name(Text) == "text"
    assert registry.get_name(Bold) == "bold"
    assert registry.get_name(Italic) == "italic"
    assert registry.get_name(Underline) == "underline"
    assert registry.get_name(Strikethrough) == "strikethrough"
    assert registry.get_name(Code) == "code"
    assert registry.get_name(Link) == "link"