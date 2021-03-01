from api import extract, popularity
from fastapi import APIRouter

api_router = APIRouter()


api_router.include_router(
    extract.router,
    tags=[
        "article-extract",
    ],
    prefix="/extract",
)


api_router.include_router(
    popularity.router,
    tags=["trends"],
    prefix="/trends",
)
