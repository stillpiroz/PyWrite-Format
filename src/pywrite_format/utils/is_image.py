"""Utilities for identifying image files based on their file signatures.

Provides helper for detecting supported image formats without relying on
third-party dependencies.
"""

from pathlib import Path

from pywrite_format.exceptions.image import ImageNotFoundError


IMAGE_SIGNATURES = frozenset({
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
})

NETPBM_SIGNATURES = frozenset({
    b"P1", b"P2", b"P3",
    b"P4", b"P5", b"P6",
})

NETPBM_WHITESPACE = b" \t\r\n\v\f"

HEIF_SIGNATURES = frozenset({
    b"avif", b"avis",
    b"heic", b"heix",
    b"hevc", b"hevx",
    b"heim", b"heis",
    b"hevm", b"hevs",
    b"mif1", b"msf1",
})


def is_image(image_path: str | Path) -> bool:
    """Check whether a file has a supported image signature.

    This function only identifies the image format based on its file
    signature. It does not validate the file's integrity or guarantee
    that the image can be decoded.
    """

    image_path = Path(image_path)

    if not image_path.exists():
        raise ImageNotFoundError(f"Image not found: {image_path}")

    if image_path.is_dir():
        raise IsADirectoryError(
            f"Expected a file, got a directory: {image_path}"
        )

    if not image_path.is_file():
        raise OSError(f"Expected a regular file: {image_path}")

    with image_path.open("rb") as file:
        header = file.read(16)

    # Netpbm
    if header[:2] in NETPBM_SIGNATURES:
        delimiter = header[2:3]
        return bool(delimiter) and delimiter in NETPBM_WHITESPACE

    # WebP
    if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
        return True

    # HEIF / HEIC / AVIF
    if header[4:8] == b"ftyp" and header[8:12] in HEIF_SIGNATURES:
        return True

    return any(
        header.startswith(signature)
        for signature in IMAGE_SIGNATURES
    )
