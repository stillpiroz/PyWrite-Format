"""Utilities for filtering and managing Inline children."""

from pywrite_format.nodes.base import Inline


def filter_children(
    children: list[Inline],
    excluded_type: type[Inline],
) -> list[Inline]:
    """
    Filter children by excluding instances of a specified Inline type.

    This function is intended for use in Inline subclasses to prevent
    redundant nested formatting, such as Bold inside another Bold.
    """

    if not isinstance(children, list):
        raise TypeError("children must be a list.")

    if not isinstance(excluded_type, type) or not issubclass(excluded_type, Inline):
        raise TypeError("excluded_type must be a subclass of Inline.")

    return [
        child for child in children
        if not isinstance(child, excluded_type)
    ]
