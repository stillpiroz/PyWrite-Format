# PyWrite-Format

**PyWrite-Format** is a lightweight Python library for creating, structuring, saving, and loading documents.

It provides a structured document model designed for [PyWrite](https://github.com/stillpiroz/PyWrite) and other applications.

## Status

Early development — `v0.1.0`

The core document structure and serialization system are implemented. The public API may change in future releases.

## Requirements

- Python 3.14 or later
- No runtime dependencies

## Installation

Install directly from the repository:

```bash
git clone https://github.com/stillpiroz/PyWrite-Format.git
cd PyWrite-Format
pip install .
```

## Quick Start

```python
from pywrite_format import Document, save, load
from pywrite_format.nodes.blocks import Paragraph
from pywrite_format.nodes.inlines import Text, Bold

# Create a document
document = Document()

# Add content
paragraph = Paragraph(
    children=[
        Text("Hello "),
        Bold([Text("World!")])
    ]
)

document.add(paragraph)

# Save the document
save(document, "example.pywrite")

# Load the document
loaded_document = load("example.pywrite")
```

## Features

- Structured document model
- Block and inline node architecture
- Text formatting (bold, italic, underline, strikethrough, and code)
- Hyperlinks
- Paragraph alignment and spacing properties
- Image support
- JSON-based serialization and deserialization
- ZIP-based `.pywrite` document packages
- Automatic image asset management and deduplication
- Public API for saving and loading documents

## Document Format

A `.pywrite` file is a ZIP archive containing JSON data and document assets.

Example structure:

```text
example.pywrite
├── metadata.json
├── content.json
└── assets/
    └── images/
        └── image_1.png
```

- `metadata.json`: Document metadata, including title, author, description, and timestamps.
- `content.json`: Serialized document structure and content.
- `assets/`: Binary assets used by the document, such as images.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.