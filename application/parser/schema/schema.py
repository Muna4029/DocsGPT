"""Base schema for data structures."""
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any

from dataclasses_json import DataClassJsonMixin


@dataclass
class BaseDocument(DataClassJsonMixin):
    """Base document.

    Generic abstract interfaces that captures both index structs
    as well as documents.

    """

    # TODO: consolidate fields from Document/IndexStruct into base class
    text: str | None = None
    doc_id: str | None = None
    embedding: list[float] | None = None

    # extra fields
    extra_info: dict[str, Any] | None = None

    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        """Get Document type."""

    def get_text(self) -> str:
        """Get text."""
        if self.text is None:
            raise ValueError("text field not set.")
        return self.text

    def get_doc_id(self) -> str:
        """Get doc_id."""
        if self.doc_id is None:
            raise ValueError("doc_id not set.")
        return self.doc_id

    @property
    def is_doc_id_none(self) -> bool:
        """Check if doc_id is None."""
        return self.doc_id is None

    def get_embedding(self) -> list[float]:
        """Get embedding.

        Errors if embedding is None.

        """
        if self.embedding is None:
            raise ValueError("embedding not set.")
        return self.embedding

    @property
    def extra_info_str(self) -> str | None:
        """Extra info string."""
        if self.extra_info is None:
            return None

        return "\n".join([f"{k}: {v!s}" for k, v in self.extra_info.items()])
