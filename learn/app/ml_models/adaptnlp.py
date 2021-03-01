import logging
from typing import List

from adaptnlp import EasySummarizer

log = logging.getLogger(__name__)
summarizer = EasySummarizer()


# Summarize
def summarize(text: str) -> List[str]:
    summaries = summarizer.summarize(
        text=text,
        model_name_or_path="t5-small",
        mini_batch_size=1,
        num_beams=4,
        min_length=0,
        max_length=100,
        early_stopping=True,
    )
    log.info(
        f"Generated {len(summaries)} summary/summaries for text of length {len(text)}"
    )
    return summaries
