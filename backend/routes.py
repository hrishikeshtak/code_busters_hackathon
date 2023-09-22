from fastapi import APIRouter
from src.rest.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router)
