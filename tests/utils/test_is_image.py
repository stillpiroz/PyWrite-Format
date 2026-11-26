"""Tests for image signature detection."""

import pytest

from pywrite_format.utils.is_image import ImageDetector


@pytest.mark.parametrize(
    "signature",
    [
        # PNG
        b"\x89PNG\r\n\x1a\n",

        # JPEG
        b"\xff\xd8\xff",

        # GIF
        b"GIF87a",
        b"GIF89a",

        # BMP
        b"BM",

        # Windows Icon / Cursor
        b"\x00\x00\x01\x00",
        b"\x00\x00\x02\x00",
    ],
)
def test_valid_image_signatures(signature):
    """Test recognition of supported image file signatures."""

    assert ImageDetector.is_image(signature)



def test_valid_webp_signature():
    """Test recognition of the WebP file signature."""

    ImageDetector.is_image(b"RIFF\x00\x00\x00\x00WEBP")


@pytest.mark.parametrize(
    "brand",
    [
        b"avif",
        b"avis",
        b"heic",
        b"heix",
        b"hevc",
        b"hevx",
        b"heim",
        b"heis",
        b"hevm",
        b"hevs",
        b"mif1",
        b"msf1",
    ],
)
def test_valid_heif_avif_signatures(brand):
    """Test recognition of supported HEIF and AVIF brands."""

    assert ImageDetector.is_image(b"\x00\x00\x00\x00ftyp" + brand)


@pytest.mark.parametrize(
    "signature",
    [
        b"P1 ",
        b"P2 ",
        b"P3 ",
        b"P4 ",
        b"P5 ",
        b"P6 ",
    ],
)
def test_valid_netpbm_signatures(signature):
    """Test recognition of supported Netpbm signatures."""

    assert ImageDetector.is_image(signature)


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"Hello World",
        b"1234567890",
        b"\x00\x00\x00\x00",
        b"PNG",
        b"RIFF\x00\x00\x00\x00XXXX",
    ],
)
def test_invalid_image_signatures(content):
    """Test rejection of unsupported image file signatures."""

    assert not ImageDetector.is_image(content)