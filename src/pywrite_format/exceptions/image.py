class InvalidImageError(Exception):
    """Raised when the specified image is invalid."""

    pass


class ImageNotFoundError(Exception):
    """Raised when the specified image does not exist."""

    pass