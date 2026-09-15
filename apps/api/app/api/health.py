"""Deterministic liveness endpoint. Does not touch a database or AI services."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(description="Service liveness status.")
    service: Literal["agentshield-api"] = Field(description="Stable service identifier.")


@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    return HealthResponse(status="ok", service="agentshield-api")
