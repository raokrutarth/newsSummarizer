from typing import Dict

from pydantic import BaseModel


class ArticleSummarizationResult(BaseModel):
    """
    Type of result sent to caller of the summarize/
    endpoint. mappings of summary text -> <some reasonable score>
    """

    summaries: Dict[str, float]
