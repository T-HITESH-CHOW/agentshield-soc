"""FastAPI application entry point for AgentShield SOC."""

from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.v1 import router as api_v1_router
from app.config import settings


def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.app_name,
        description=(
            "HTTP API foundation for AgentShield SOC. "
            "This Day 2 surface exposes liveness only; "
            "SOC, AI, and data-store features are not implemented yet."
        ),
        version="0.2.0",
        debug=settings.debug,
    )
    application.include_router(health_router)
    application.include_router(api_v1_router)
    return application


app = create_app()
