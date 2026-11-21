"""Tests for image signature detection."""

import pytest

from pywrite_format.utils.is_image import is_image


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
def test_valid_image_signatures(tmp_path, signature):
    """Test recognition of supported image file signatures."""

    image = tmp_path / "test_image"
    image.write_bytes(signature)

    assert is_image(image)


def test_valid_webp_signature(tmp_path):
    """Test recognition of the WebP file signature."""

    image = tmp_path / "test.webp"
    image.write_bytes(b"RIFF\x00\x00\x00\x00WEBP")

    assert is_image(image)


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
def test_valid_heif_avif_signatures(tmp_path, brand):
    """Test recognition of supported HEIF and AVIF brands."""

    image = tmp_path / "test_image"
    image.write_bytes(b"\x00\x00\x00\x00ftyp" + brand)

    assert is_image(image)


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
def test_valid_netpbm_signatures(tmp_path, signature):
    """Test recognition of supported Netpbm signatures."""

    image = tmp_path / "test_image"
    image.write_bytes(signature)

    assert is_image(image)


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
def test_invalid_image_signatures(tmp_path, content):
    """Test rejection of unsupported image file signatures."""

    image = tmp_path / "test_image"
    image.write_bytes(content)

    assert not is_image(image)
