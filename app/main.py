from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.document_routes import router as document_router
from app.core.settings import settings
from app.core.startup import on_startup


@asynccontextmanager
async def lifespan(app: FastAPI):
    on_startup()
    yield
    

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(document_router)

@app.get("/")
async def health_check():
    
    return {
        "status": "UP",
        "application": settings.APP_NAME,
        "environment": settings.ENVIRONMENT
    }