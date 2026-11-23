"""
Inline elements for creating and formatting text content.

Provides text, formatting, code, and hyperlink elements.
"""

from pywrite_format.inline_utils import filter_children


class Text(Inline):
    """Normal text"""

    def __init__(self, text: str):
        self.text = text


class Bold(Inline):
    """Bold text"""

    def __init__(self, children: list[Inline] | None = None):
        self.children = filter_children(children, Bold)


class Italic(Inline):
    """Italic text"""

    def __init__(self, children: list[Inline] | None = None):
        self.children = filter_children(children, Italic)


class Underline(Inline):
    """Underline text"""

    def __init__(self, children: list[Inline] | None = None):
        self.children = filter_children(children, Underline)


class Strikethrough(Inline):
    """Strikethrough text"""

    def __init__(self, children: list[Inline] | None = None):
        self.children = filter_children(children, Strikethrough)


class Code(Inline):
    """Code text"""

    def __init__(self, children: list[Inline] | None = None):
        self.children = filter_children(children, Code)


class Link(Inline):
    """Hyperlink or URL"""

    def __init__(
        self,
        url: str,
        children: list[Inline] | None = None,
    ):
        self.url = url
        self.children = filter_children(children, Link)
