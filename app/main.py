"""
FastAPI application initialization
"""

from fastapi import FastAPI
from app.config import API_TITLE, API_DESCRIPTION, API_VERSION
from app.routes import router

# Initialize FastAPI app
app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

# Include routers
app.include_router(router)

