from datetime import datetime
from typing import List

from pydantic import BaseModel


class ExtractRequest(BaseModel):
    url: str
    tags: List[str]


class ExtractResult(BaseModel):
    raw_text: str
    is_cleaned: bool
    title: str
    url: str
    images: List[str]
    date_fetched: datetime
    date_published: datetime
    nested_urls: List[str]

    def snipped(self) -> str:
        """
        Return the human-readable version of the object
        """
        attributes = vars(self)
        text_snipped = f"raw_text={self.raw_text[:10]}...{self.raw_text[-10:]}"
        other_fields = ", ".join(
            f"{key}: {value}"
            for (key, value) in attributes.items()
            if key != "raw_text"
        )
        return f"{self.__class__.__name__}({text_snipped}, {other_fields})"
