"""
API routes/endpoints
"""

import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models import MessageRequest, MessageResponse
from app.services import get_summary_from_openai
from app.config import logger

router = APIRouter()


@router.post("/nevie/test", response_model=MessageResponse)
async def nevie_test(request: MessageRequest):
    """
    Process a message: validate, summarize via OpenAI, and return response.
    
    Args:
        request: MessageRequest containing the message to process
        
    Returns:
        MessageResponse with status, summary, and timestamp
    """
    try:
        logger.info(f"Received request with message: {request.message}")
        
        # Validate message (Pydantic already validates, but we can add custom validation)
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Call OpenAI to summarize
        summary = get_summary_from_openai(request.message)
        
        # Generate timestamp
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        # Prepare response
        response = MessageResponse(
            status="ok",
            summary=summary,
            timestamp=timestamp
        )
        
        logger.info(f"Request processed successfully. Summary: {summary}")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "NEVIE-GLOBAL™ Test API is running"}


@router.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat() + "Z"}

