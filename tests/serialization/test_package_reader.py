import json
import zipfile

from pywrite_format.serialization.package_reader import PackageReader


def test_read_package(tmp_path):
    reader = PackageReader()

    metadata = {
        "title": "My Document",
        "author": "Piroz"
    }

    content = {
        "type": "paragraph",
        "children": [
            {"type": "text", "text": "Hello World"}
        ]
    }

    image_data = b"fake image data"
    asset_path = "assets/images/image_1.png"

    input_path = tmp_path / "test.pywrite"

    with zipfile.ZipFile(input_path, "w") as archive:
        archive.writestr(
            "metadata.json",
            json.dumps(metadata)
        )

        archive.writestr(
            "content.json",
            json.dumps(content)
        )

        archive.writestr(asset_path, image_data)

    result = reader.read(input_path)

    assert result["metadata"] == metadata
    assert result["content"] == content
    assert result["assets"] == {
        image_data: asset_path
    }


def test_read_package_without_assets(tmp_path):
    reader = PackageReader()

    input_path = tmp_path / "test.pywrite"

    with zipfile.ZipFile(input_path, "w") as archive:
        archive.writestr("metadata.json", "{}")
        archive.writestr("content.json", "{}")

    result = reader.read(input_path)

    assert result["assets"] == {}