"""
FastAPI application initialization and entry point
"""

import uvicorn
from fastapi import FastAPI
from app.core.config import API_TITLE, API_DESCRIPTION, API_VERSION
from app.api.routes import router
from app.core.exceptions import register_exception_handlers

# Initialize FastAPI app
app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

# Register exception handlers
register_exception_handlers(app)

# Include routers
app.include_router(router)


# Entry point for running the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

