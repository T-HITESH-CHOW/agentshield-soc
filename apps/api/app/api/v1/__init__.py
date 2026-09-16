"""Versioned API surface."""
from fastapi import APIRouter
from app.api.v1.alerts import router as alerts_router

router = APIRouter(prefix="/api/v1")
router.include_router(alerts_router, tags=["Alerts"])
