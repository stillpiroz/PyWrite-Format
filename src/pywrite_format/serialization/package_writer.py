"""Write document packages to .pywrite files."""

import json
import zipfile


class PackageWriter:
    """Writes document data and assets into a package."""

    def write(self, metadata, content, assets, output_path):
        with zipfile.ZipFile(
            output_path, "w", compression=zipfile.ZIP_DEFLATED
            ) as archive:

            archive.writestr(
                "metadata.json",
                json.dumps(metadata, indent=4))

            archive.writestr(
                "content.json",
                json.dumps(content, indent=4))

            for image_data, asset_path in assets.items():
                archive.writestr(asset_path, image_data)
