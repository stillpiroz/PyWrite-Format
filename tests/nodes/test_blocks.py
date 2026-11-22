import pytest

from pywrite_format.nodes.base import Inline
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.styles import Alignment
from pywrite_format.exceptions.image import InvalidImageError


# --- Paragraph ---
def test_paragraph_custom_attributes():
    values = {
        "children": [],
        "alignment": Alignment.RIGHT,
        "indentation": 0.1,
        "spacing_before": 0.1,
        "spacing_after": 0.1,
        "line_spacing": 1.2,
    }

    ins_paragraph = Paragraph(**values)

    for key, value in values.items():
        assert getattr(ins_paragraph, key) == value


def test_paragraph_default_values():
    ins_paragraph = Paragraph(children=[])

    assert ins_paragraph.children == []
    assert ins_paragraph.alignment == Alignment.LEFT
    assert ins_paragraph.indentation == 0.0
    assert ins_paragraph.spacing_before == 0.0
    assert ins_paragraph.spacing_after == 0.0
    assert ins_paragraph.line_spacing == 1.0


# --- Image ---
@pytest.mark.parametrize(
    "image_data",
    [
        b"\x89PNG\r\n\x1a\n",
        b"\xff\xd8\xff",
        b"GIF89a",
        b"BM",
        b"RIFF\x00\x00\x00\x00WEBP",
    ],
)
def test_image_accepts_supported_signatures(image_data):
    ins_image = Image(image_data)

    assert isinstance(ins_image, Image)


def test_image_data():
    image_data = b"\x89PNG\r\n\x1a\n"

    ins_image = Image(image_data)

    assert ins_image.image_data is image_data


@pytest.mark.parametrize(
    "image_data",
    [
        b"",
        b"Hello World",
        b"1234567890",
        b"\x00\x00\x00\x00",
        b"PNG",
    ],
)
def test_image_invalid_data(image_data):
    with pytest.raises(
        InvalidImageError,
        match="Invalid or unsupported image data.",
    ):
        Image(image_data)
