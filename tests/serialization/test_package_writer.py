import json
import zipfile

from pywrite_format.serialization.package_writer import PackageWriter


def test_write_package(tmp_path):
    writer = PackageWriter()

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
    assets = {
        image_data: "assets/images/image_1.png"
    }

    output_path = tmp_path / "test.pywrite"

    writer.write(metadata, content, assets, output_path)

    assert output_path.exists()

    with zipfile.ZipFile(output_path, "r") as archive:
        assert "metadata.json" in archive.namelist()
        assert "content.json" in archive.namelist()
        assert "assets/images/image_1.png" in archive.namelist()

        saved_metadata = json.loads(
            archive.read("metadata.json")
        )

        saved_content = json.loads(
            archive.read("content.json")
        )

        saved_image = archive.read(
            "assets/images/image_1.png"
        )

    assert saved_metadata == metadata
    assert saved_content == content
    assert saved_image == image_data
