import logging

from core.extract import Scraper, Strategy
from data_models.extract import ExtractRequest, ExtractResult
from fastapi import APIRouter, Query
from starlette.requests import Request

log = logging.getLogger(__name__)
router = APIRouter()


@router.post("/web", response_model=ExtractResult)
def extract_article(
    request: Request,
    payload: ExtractRequest,
    strategy: Strategy = Query(
        Strategy.news_paper,
        title="Scrape Strategy",
        description="Selection of scrape strategies. Each provides different levels of scrape completeness.",
    ),
) -> ExtractResult:
    log.info(f"Metadata of article to scrape: {payload}, request: {request}")

    scraped = Scraper.scrape(strategy, payload.url, payload.tags)
    log.info(f"Scraped content: {scraped}")

    return scraped
