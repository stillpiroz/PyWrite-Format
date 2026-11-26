import pytest

from pywrite_format.serialization.registry import Registry


class Paragraph:
    pass


class Text:
    pass


def test_register_node():
    registry = Registry()

    registry.register("paragraph", Paragraph)

    assert registry.get("paragraph") is Paragraph


def test_register_duplicate_node():
    registry = Registry()

    registry.register("paragraph", Paragraph)

    with pytest.raises(ValueError, match="already registered"):
        registry.register("paragraph", Text)


def test_get_unknown_node():
    registry = Registry()

    with pytest.raises(ValueError, match="Unknown node type"):
        registry.get("unknown")


def test_get_name():
    registry = Registry()

    registry.register("paragraph", Paragraph)

    assert registry.get_name(Paragraph) == "paragraph"


def test_get_name_unregistered_class():
    registry = Registry()

    with pytest.raises(ValueError, match="is not registered"):
        registry.get_name(Paragraph)
