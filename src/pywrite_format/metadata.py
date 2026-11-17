"""Define document metadata and timestamp management."""


from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class DocumentMetadata:
    """Stores metadata and timestamps associated with a document."""

    title: str | None = None
    author: str | None = None
    description: str | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    modified_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def update_modified_at(self) -> None:
        """Update the modified_at timestamp."""

        self.modified_at = datetime.now(timezone.utc)
