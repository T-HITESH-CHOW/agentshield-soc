"""Versioned API surface. No SOC endpoints are registered on Day 2."""

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")
