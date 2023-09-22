from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_app()
