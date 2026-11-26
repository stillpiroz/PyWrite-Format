import pytest

from pywrite_format.serialization.assetmanager import AssetManager


def test_add_png_image():
    manager = AssetManager()

    image_data = b"\x89PNG\r\n\x1a\n"

    result = manager.add(image_data)

    assert result == "assets/images/image_1.png"


def test_add_unsupported_image():
    manager = AssetManager()

    with pytest.raises(ValueError, match="Unsupported image format"):
        manager.add(b"fake image data")


def test_add_duplicate_image():
    manager = AssetManager()

    image_data = b"\x89PNG\r\n\x1a\n"

    first = manager.add(image_data)
    second = manager.add(image_data)

    assert first == second
    assert first == "assets/images/image_1.png"
    assert len(manager.assets) == 1


def test_add_different_images():
    manager = AssetManager()

    first = manager.add(b"\x89PNG\r\n\x1a\n")
    second = manager.add(b"\xff\xd8\xff")

    assert first == "assets/images/image_1.png"
    assert second == "assets/images/image_2.jpg"
    assert len(manager.assets) == 2


def test_asset_counter():
    manager = AssetManager()

    manager.add(b"\x89PNG\r\n\x1a\n")
    manager.add(b"\xff\xd8\xff")

    assert manager._counter == 2