"""Utilities for identifying image formats from their byte signatures.

Provides a helper for detecting supported image formats without relying on
third-party dependencies.
"""


class ImageDetector:
    """Identify image formats using their byte signatures."""

    IMAGE_SIGNATURES = {
        b"\x89PNG\r\n\x1a\n": ".png",
        b"\xff\xd8\xff": ".jpg",
        b"GIF87a": ".gif",
        b"GIF89a": ".gif",
        b"BM": ".bmp",
        b"\x00\x00\x01\x00": ".ico",
        b"\x00\x00\x02\x00": ".cur",
    }

    NETPBM_SIGNATURES = frozenset({
        b"P1", b"P2", b"P3",
        b"P4", b"P5", b"P6",
    })

    NETPBM_WHITESPACE = b" \t\r\n\v\f"

    HEIF_SIGNATURES = {
        b"avif": ".avif",
        b"avis": ".avif",
        b"heic": ".heic",
        b"heix": ".heic",
        b"hevc": ".heic",
        b"hevx": ".heic",
        b"heim": ".heic",
        b"heis": ".heic",
        b"hevm": ".heic",
        b"hevs": ".heic",
        b"mif1": ".heif",
        b"msf1": ".heif",
    }

    @classmethod
    def detect(cls, image_data: bytes) -> str | None:
        """Return the image format or None if unsupported."""

        header = image_data[:16]

        # Netpbm
        if header[:2] in cls.NETPBM_SIGNATURES:
            delimiter = header[2:3]

            if delimiter and delimiter in cls.NETPBM_WHITESPACE:
                return f".{header[:2].decode().lower()}"

            return None

        # WebP
        if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
            return ".webp"

        # HEIF / HEIC / AVIF
        if header[4:8] == b"ftyp":
            return cls.HEIF_SIGNATURES.get(header[8:12])

        # Standard image signatures
        for signature, extension in cls.IMAGE_SIGNATURES.items():
            if header.startswith(signature):
                return extension

        return None

    @classmethod
    def is_image(cls, image_data: bytes) -> bool:
        """Check whether byte data represents a supported image format."""

        return cls.detect(image_data) is not None
