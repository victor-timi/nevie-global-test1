"""
Exception handlers for the FastAPI application
"""

from datetime import datetime
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.config import error_logger, logger
from app.models.models import ErrorResponse


def register_exception_handlers(app):
    """
    Register global exception handlers on the FastAPI app.
    
    Args:
        app: FastAPI application instance
    """
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        Handler for validation errors (400/422).
        These are expected client errors (bad input), not system failures.
        Optionally log to normal.log for monitoring, but they're not critical.
        """
        # Validation errors are expected client behavior - log to normal.log at INFO level
        # (normal.log = normal operations, error.log = system failures)
        error_details = exc.errors()
        logger.info(
            f"Validation error - {request.method} {request.url.path}: {error_details}"
        )
        
        # Return FastAPI's default validation error response
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()}
        )
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """
        Global exception handler for all unhandled exceptions.
        Logs to error.log and returns structured error response.
        """
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        # Log to error.log (unexpected system errors)
        error_logger.error(
            f"Unhandled exception: {type(exc).__name__}: {str(exc)}",
            exc_info=True,
            extra={
                "path": request.url.path,
                "method": request.method
            }
        )
        
        # Return structured error response
        error_response = ErrorResponse(
            status="error",
            message="AI processing failed",
            timestamp=timestamp
        )
        
        return JSONResponse(
            status_code=500,
            content=error_response.model_dump()
        )

