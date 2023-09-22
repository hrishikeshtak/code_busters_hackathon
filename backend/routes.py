from fastapi import APIRouter

from src.rest.endpoints import auth, category, organization, stats

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(category.router)
api_router.include_router(organization.router)
api_router.include_router(stats.router)
