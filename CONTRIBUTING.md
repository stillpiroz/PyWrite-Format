# Contributing

Contributions are welcome and greatly appreciated! There are several ways to contribute to PyWrite-Format.

## Report Bugs

Report bugs on the [GitHub Issues](https://github.com/stillpiroz/PyWrite-Format/issues) page.

If you are reporting a bug, please include:

- Your operating system name and version.
- Python version.
- Steps to reproduce the issue.
- Expected and actual behavior.

## Suggest Features

Feature suggestions are welcome.

Please open an issue to describe the feature and explain why it would be useful before starting development.

## Development Setup

1. Fork the repository.
2. Clone your fork.
3. Create a new branch.
4. Install development dependencies using `uv sync`.
5. Make your changes.
6. Run tests using `uv run pytest`.
7. Commit your changes and open a Pull Request.

## Documentation

Clear and simple documentation is preferred.

When writing documentation:

- Use simple and understandable English.
- Keep explanations short and clear.
- Follow the existing documentation style.

## Writing Commit Messages

PyWrite-Format follows the **Conventional Commits** specification.

Every commit must follow this format:

`type: short description`

Examples:

- `feat: add document metadata`
- `fix: handle invalid node types`
- `docs: update installation guide`
- `refactor: simplify document structure`

For reference, see this [example commit](https://github.com/stillpiroz/PyWrite-Format/commit/209a47672ac58a3f1947f10434d79478d7e7a2c8).

## Code Style

Please keep the code:

- Simple and readable.
- Consistent with the existing codebase.
- Compliant with Python's PEP 8 guidelines.
- Properly documented when necessary.

**Additional Formatting Convention:**

When writing a module-level docstring, follow these spacing rules:

- If the module is followed by import statements, leave one blank line between the docstring and the imports.
- If the module is followed directly by a class, function, or other definition, leave two blank lines between the docstring and the definition.

**Example (imports):**

```python
"""Define document metadata and timestamp management."""

from dataclasses import dataclass, field
```

**Example (class definition):**

```python
"""Core document structure definitions."""


class Node:
    """Base class for all document nodes."""

    pass
```

## Zero Dependencies

PyWrite-Format follows a **Zero Runtime Dependencies** policy.

The library must not require third-party packages at runtime.

Please avoid introducing external runtime dependencies when contributing new features.

## AI Usage Policy

If you use AI tools while contributing, please read our [AI Usage Policy](AI_USAGE_POLICY.md) and follow its guidelines.
