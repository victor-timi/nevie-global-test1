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
    cached: bool = Field(default=False, description="Whether the response was served from cache")


class ErrorResponse(BaseModel):
    """Error response model"""
    status: str = "error"
    message: str
    timestamp: str


class StatsResponse(BaseModel):
    """Stats response model"""
    total_requests: int
    cache_hits: int
    cache_miss: int

