import logging

from data_models.payload import ArticleSummarizationPayload
from data_models.summarize import ArticleSummarizationResult
from fastapi import APIRouter
from ml_models import adaptnlp, bert, bart_hf
from starlette.requests import Request

router = APIRouter()
log = logging.getLogger(__name__)


@router.post("/summarize/adapt", response_model=ArticleSummarizationResult)
def summarize_adapt(
    request: Request, payload: ArticleSummarizationPayload = None
) -> ArticleSummarizationResult:

    log.info(f"Computing summaries for test of length {len(payload.text)}")
    summaries = adaptnlp.summarize(payload.text)
    summaries = {s: 1.0 for s in summaries}
    return ArticleSummarizationResult(summaries=summaries)


@router.post("/summarize/bart", response_model=ArticleSummarizationResult)
def summarize_bart(
    request: Request, payload: ArticleSummarizationPayload = None
) -> ArticleSummarizationResult:

    log.info(f"Computing summaries for test of length {len(payload.text)}")
    summaries = bart_hf.summarize(payload.text)
    summaries = {s: 1.0 for s in summaries}
    return ArticleSummarizationResult(summaries=summaries)


@router.post("/summarize/bert", response_model=ArticleSummarizationResult)
def summarize_bert(
    request: Request, payload: ArticleSummarizationPayload = None
) -> ArticleSummarizationResult:

    log.info(f"Computing summaries for test of length {len(payload.text)}")
    summaries = bert.summarize(payload.text)
    summaries = {s: 1.0 for s in summaries}
    return ArticleSummarizationResult(summaries=summaries)
