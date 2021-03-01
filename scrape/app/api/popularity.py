import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List

from fastapi import APIRouter
from fastapi.params import Query
from pandas import DataFrame
from pydantic import create_model
from pytrends import (  # TODO use pytrends to get populatiry score for terms
    dailydata,
    request,
)

log = logging.getLogger(__name__)
router = APIRouter()
pytrends = request.TrendReq(retries=3, backoff_factor=0.1, timeout=15)

"""
    Uses Search Engine APIs to get popularity metrics
    https://support.google.com/trends/answer/4355000
"""


@router.get(
    "",
    summary="Get trending searches globally.",
    response_model=create_model(
        "TrendingSearchesResponse",
        globally=(
            Dict[str, List[str]],
            ...,
        ),
    ),
)
def get_tending_google_topics():
    # FIXME hacky fetch of per country trending searches using internal library function.
    globally = pytrends._get_data(
        url=pytrends.TRENDING_SEARCHES_URL,
        method=pytrends.GET_METHOD,
        **pytrends.requests_args,
    )
    # NOTE could also use newspaper.hot() for US-only trending searches
    return dict(globally=globally)


@router.post(
    "",
    summary="Popularity data for given topic(s)",
    description="Given a list of topics/keywords, return populatiry scores (0-100) over time and by region as determined by Google APIs.",
    response_model=create_model(
        "TopicPopularityResponse",
        by_country=(
            Dict[str, Any],
            ...,
        ),
        over_time=(
            Dict[str, Any],
            ...,
        ),
        related_topics=(
            Dict[str, Any],
            ...,
        ),
        time_window_start=(
            str,
            ...,
        ),
        time_window_end=(
            str,
            ...,
        ),
    ),
)
def get_topic_popularity(
    keywords: List[str],
    time_window_d: int = Query(  # type: ignore
        1095,  # default to 3 years
        title="Number of days",
        description="Get popularity data from now up to time_window_d days ago.",
        gt=0,
    ),
):
    now = datetime.now()
    window_end = now.strftime("%Y-%m-%d")
    window_start = (now - timedelta(days=time_window_d)).strftime(
        "%Y-%m-%d"
    )  # .replace(microsecond=0).isoformat()
    time_window = f"{window_start} {window_end}"
    log.info(f"Fetching popularity data for {keywords} in time window {time_window}")

    # build request for keyword popularity for all regions over web search data
    pytrends.build_payload(
        keywords,
        cat=0,
        timeframe=time_window,
        geo="",
        gprop="",  # gprop="news"
    )

    # fetch interest per country
    by_country = pytrends.interest_by_region(
        # inc_geo_code=True,
        # resolution="CITY",  # TODO doesn't work
        inc_low_vol=True,
    )
    # fetch interest over time
    over_time = pytrends.interest_over_time()

    # fetch related searches
    related_payload: Dict[str, Dict[str, DataFrame]] = pytrends.related_queries()

    # convert related searches payload to a REST response type
    related: Dict[str, Dict[str, Any]] = dict()
    for query, metadata in related_payload.items():
        for meta_type, df in metadata.items():
            if query not in related:
                related[query] = dict()
            assert isinstance(
                df, DataFrame
            ), f"Unexpected pyload {metadata} returned from pytrends API"
            related[query][meta_type] = df.to_dict()

    return dict(
        by_country=by_country.to_dict(),
        over_time=over_time.to_dict(),
        related_topics=related,
        time_window_start=window_start,
        time_window_end=window_end,
    )
