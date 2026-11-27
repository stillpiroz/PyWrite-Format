"""Read document packages from .pywrite files."""

import json
import zipfile


class PackageReader:
    """Reads document data and assets from a package."""

    def read(self, input_path):
        with zipfile.ZipFile(input_path, mode="r") as archive:
            metadata = json.loads(
                archive.read("metadata.json")
            )

            content = json.loads(
                archive.read("content.json")
            )

            assets = {}

            for asset_path in archive.namelist():
                if asset_path.startswith("assets/"):
                    image_data = archive.read(asset_path)
                    assets[image_data] = asset_path

        return {
            "metadata": metadata,
            "content": content,
            "assets": assets,
        }
