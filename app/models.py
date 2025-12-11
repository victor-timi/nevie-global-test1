"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    """Request model for /nevie/test endpoint"""
    message: str = Field(..., min_length=1, description="Message to be summarized")


class MessageResponse(BaseModel):
    """Response model for /nevie/test endpoint"""
    status: str
    summary: str
    timestamp: str

