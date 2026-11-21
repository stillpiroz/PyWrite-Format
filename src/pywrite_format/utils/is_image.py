"""Utilities for identifying image formats from their byte signatures.

Provides a helper for detecting supported image formats without relying on
third-party dependencies.
"""


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


def is_image(image_data: bytes) -> bool:
    """Check whether byte data starts with a supported image signature.

    This function only identifies the image format based on its file
    signature. It does not validate the file's integrity or guarantee
    that the image can be decoded.
    """

    header = image_data[:16]

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
