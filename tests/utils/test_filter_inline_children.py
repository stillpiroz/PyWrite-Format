"""Tests for filter_inline_children.py module"""

import pytest

from pywrite_format.utils.filter_inline_children import filter_children
from pywrite_format.nodes.base import Inline

# Define several Inline subclasses for use in tests
class FirstExample(Inline):
    pass


class SecondExample(Inline):
    pass


# Tests
def test_children_not_list():
    """
    Test that the function raises the expected TypeError
    when children is not a list.
    """

    with pytest.raises(
        TypeError,
        match="children must be a list."
    ):
        filter_children("Hello", FirstExample)


def test_excluded_type_not_inline():
    """
    Test that the function raises a TypeError with the expected
    message when excluded_type is not a subclass of Inline.
    """

    with pytest.raises(
        TypeError,
        match="excluded_type must be a subclass of Inline."
    ):
        filter_children([], "Hello!")


def test_correct_filtering():
    """
    Test that when the arguments are valid,
    the function returns the correct result
    and filters the children correctly.
    """

    first_example_ins = FirstExample()
    second_example_ins = SecondExample()
    
    expected_result = [first_example_ins]

    filter_children([first_example_ins, second_example_ins], SecondExample)
