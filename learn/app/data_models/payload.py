from typing import List

from pydantic import BaseModel


class ArticleSummarizationPayload(BaseModel):
    """
    Information sent by the summarize/ endpoint caller
    to fetch a summary of the article
    """

    text: str
    tags: List[str]
