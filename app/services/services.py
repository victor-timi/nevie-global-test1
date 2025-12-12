"""
Business logic services for OpenAI and recommendations
"""

import logging
from openai import OpenAI
from app.core.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_MAX_TOKENS,
    OPENAI_TEMPERATURE,
    logger
)

# Initialize OpenAI client
openai_client = None
try:
    if OPENAI_API_KEY:
        openai_client = OpenAI(api_key=OPENAI_API_KEY)
        logger.info("OpenAI client initialized successfully")
    else:
        logger.warning("OPENAI_API_KEY not found in environment variables")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")


def get_summary_from_openai(message: str) -> str:
    """
    Call OpenAI to summarize the message in one clear sentence.
    
    Args:
        message: The input message to summarize
        
    Returns:
        A one-sentence summary
        
    Raises:
        Exception: If OpenAI API call fails
    """
    if not openai_client:
        raise Exception("OpenAI client not initialized. Please set OPENAI_API_KEY environment variable.")
    
    try:
        response = openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes messages in one clear sentence."},
                {"role": "user", "content": f"Summarize this message in one clear sentence: {message}"}
            ],
            max_tokens=OPENAI_MAX_TOKENS,
            temperature=OPENAI_TEMPERATURE
        )
        
        summary = response.choices[0].message.content.strip()
        logger.info(f"OpenAI summary generated successfully")
        return summary
        
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        raise Exception(f"Failed to generate summary: {str(e)}")


def get_recommendation(summary: str) -> str:
    """
    Mini AI Pipeline: Takes the summary and returns one recommendation sentence.
    
    Args:
        summary: The summarized message
        
    Returns:
        A one-sentence recommendation
    """
    # Simple recommendation logic based on summary
    # In a real scenario, this could call another AI model or use more complex logic
    recommendation = f"Based on the summary '{summary}', I recommend reviewing the key points and taking appropriate action."
    
    logger.info(f"Recommendation generated: {recommendation}")
    return recommendation

