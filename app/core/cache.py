"""
In-memory cache for message summaries
"""

from typing import Dict, Optional, Tuple
from datetime import datetime

# In-memory cache: key = normalized message, value = (summary, timestamp)
_cache: Dict[str, Tuple[str, str]] = {}

# Statistics
_total_requests = 0
_cache_hits = 0
_cache_miss = 0


def normalize_message(message: str) -> str:
    """
    Normalize message for cache key (lowercase, strip whitespace)
    
    Args:
        message: Original message
        
    Returns:
        Normalized message string
    """
    return message.lower().strip()


def get_cached_summary(message: str) -> Optional[Tuple[str, str]]:
    """
    Get cached summary if exists.
    
    Args:
        message: Message to look up
        
    Returns:
        Tuple of (summary, timestamp) if found, None otherwise
    """
    key = normalize_message(message)
    return _cache.get(key)


def cache_summary(message: str, summary: str, timestamp: str) -> None:
    """
    Cache a summary for a message.
    
    Args:
        message: Original message
        summary: Generated summary
        timestamp: Timestamp of generation
    """
    key = normalize_message(message)
    _cache[key] = (summary, timestamp)


def increment_total_requests() -> None:
    """Increment total request counter"""
    global _total_requests
    _total_requests += 1


def increment_cache_hit() -> None:
    """Increment cache hit counter"""
    global _cache_hits
    _cache_hits += 1


def increment_cache_miss() -> None:
    """Increment cache miss counter"""
    global _cache_miss
    _cache_miss += 1


def get_stats() -> Dict[str, int]:
    """
    Get cache statistics.
    
    Returns:
        Dictionary with total_requests, cache_hits, cache_miss
    """
    return {
        "total_requests": _total_requests,
        "cache_hits": _cache_hits,
        "cache_miss": _cache_miss
    }


def clear_cache() -> None:
    """
    Clear the in-memory cache and reset statistics.
    Useful for testing or resetting state.
    """
    global _cache, _total_requests, _cache_hits, _cache_miss
    _cache.clear()
    _total_requests = 0
    _cache_hits = 0
    _cache_miss = 0

