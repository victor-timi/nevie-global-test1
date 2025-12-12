"""
API routes/endpoints
"""

import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models.models import MessageRequest, MessageResponse, StatsResponse, ErrorResponse
from app.services.services import get_summary_from_openai
from app.core.cache import (
    get_cached_summary,
    cache_summary,
    increment_total_requests,
    increment_cache_hit,
    increment_cache_miss,
    get_stats,
    clear_cache
)
from app.core.config import logger, error_logger

router = APIRouter()


@router.post("/nevie/test", response_model=MessageResponse)
async def nevie_test(request: MessageRequest):
    """
    Process a message: validate, summarize via OpenAI, and return response.
    Uses in-memory cache to avoid duplicate AI calls.
    
    Args:
        request: MessageRequest containing the message to process
        
    Returns:
        MessageResponse with status, summary, timestamp, and cached flag
    """
    # Increment total requests counter
    increment_total_requests()
    
    try:
        logger.info(f"Received request with message: {request.message}")
        
        # Validate message (Pydantic already validates, but we can add custom validation)
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Check cache first
        cached_result = get_cached_summary(request.message)
        
        if cached_result:
            # Cache hit - return cached result
            summary, timestamp = cached_result
            increment_cache_hit()
            logger.info(f"Cache HIT for message: {request.message[:50]}...")
            
            response = MessageResponse(
                status="ok",
                summary=summary,
                timestamp=timestamp,
                cached=True
            )
            return response
        
        # Cache miss - call OpenAI
        increment_cache_miss()
        logger.info(f"Cache MISS for message: {request.message[:50]}...")
        
        # Call OpenAI to summarize
        summary = get_summary_from_openai(request.message)
        
        # Replace ALL double quotes with single quotes to avoid JSON issues in n8n
        summary = summary.replace('"', "'")
        
        # Generate timestamp
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        # Cache the result
        cache_summary(request.message, summary, timestamp)
        
        # Prepare response
        response = MessageResponse(
            status="ok",
            summary=summary,
            timestamp=timestamp,
            cached=False
        )
        
        logger.info(f"Request processed successfully. Summary: {summary}")
        return response
        
    except HTTPException:
        # Re-raise HTTP exceptions (validation errors, etc.)
        raise
    except Exception as e:
        # Log to error.log
        error_logger.error(f"Error processing request: {e}", exc_info=True)
        # Let global exception handler catch this and return structured error
        raise


@router.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "NEVIE-GLOBAL™ Test API is running"}


@router.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat() + "Z"}


@router.get("/nevie/stats", response_model=StatsResponse)
async def get_statistics():
    """
    Get cache and request statistics.
    
    Returns:
        StatsResponse with total_requests, cache_hits, cache_miss
    """
    stats = get_stats()
    logger.info(f"Stats requested: {stats}")
    return StatsResponse(**stats)

