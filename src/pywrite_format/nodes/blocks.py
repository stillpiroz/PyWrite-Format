"""Document block definitions.

Provides block-level elements for document content, including paragraphs
and images.
"""

from dataclasses import dataclass

from pywrite_format.exceptions.image import InvalidImageError
from pywrite_format.nodes.base import Block, Inline
from pywrite_format.styles import Alignment
from pywrite_format.utils.is_image import is_image


@dataclass
class Paragraph(Block):
    """Represents a paragraph in a document."""

    children: list[Inline]
    alignment: Alignment = Alignment.LEFT
    indentation: float = 0.0
    spacing_before: float = 0.0
    spacing_after: float = 0.0
    line_spacing: float = 1.0


class Image(Block):
    """Represent an image and its underlying byte data."""

    def __init__(self, image_data: bytes):
        if not is_image(image_data[:16]):
            raise InvalidImageError("Invalid or unsupported image data.")
        
        self.image_data = image_data
