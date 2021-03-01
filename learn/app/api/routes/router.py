from api.routes import heartbeat
from api.routes import summarize
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    heartbeat.router,
    tags=["health"],
    prefix="/health",
)

api_router.include_router(
    summarize.router,
    tags=[
        "summarize",
    ],
    prefix="/model",
)
