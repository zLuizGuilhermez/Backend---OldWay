from fastapi import APIRouter

from app.fastapi.controllers.health_controller import router as health_router
from app.fastapi.controllers.item_controller import router as item_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(item_router, prefix="/api/v1")
