from .registry import Registry
from pywrite_format.nodes.blocks import Paragraph, Image
from pywrite_format.nodes.inlines import (
    Text,
    Bold,
    Italic,
    Underline,
    Strikethrough,
    Code,
    Link,
)


registry = Registry()

# --- Blocks ---
registry.register("paragraph", Paragraph)
registry.register("image", Image)

# --- Inlines ---
registry.register("text", Text)
registry.register("bold", Bold)
registry.register("italic", Italic)
registry.register("underline", Underline)
registry.register("strikethrough", Strikethrough)
registry.register("code", Code)
registry.register("link", Link)
