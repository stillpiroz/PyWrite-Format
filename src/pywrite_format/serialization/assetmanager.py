from pywrite_format.utils.is_image import ImageDetector


class AssetManager:
    """Manages document image assets and prevents duplicate storage."""

    def __init__(self):
        self.assets = {}
        self._counter = 0

    def add(self, image_data: bytes) -> str:
        extension = ImageDetector.detect(image_data)

        if extension is None:
            raise ValueError("Unsupported image format.")

        if image_data in self.assets:
            return self.assets[image_data]

        self._counter += 1
        asset_path = f"assets/images/image_{self._counter}{extension}"

        self.assets[image_data] = asset_path

        return asset_path
