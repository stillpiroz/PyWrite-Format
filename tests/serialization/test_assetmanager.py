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


def test_get_existing_asset():
    manager = AssetManager()

    image_data = b"\x89PNG\r\n\x1a\n"
    asset_path = manager.add(image_data)

    assert manager.get(asset_path) == image_data


def test_get_unknown_asset():
    manager = AssetManager()

    with pytest.raises(KeyError, match="Asset .* not found"):
        manager.get("assets/images/unknown.png")


def test_get_multiple_assets():
    manager = AssetManager()

    first_image = b"\x89PNG\r\n\x1a\n"
    second_image = b"\xff\xd8\xff"

    first_path = manager.add(first_image)
    second_path = manager.add(second_image)

    assert manager.get(first_path) == first_image
    assert manager.get(second_path) == second_image