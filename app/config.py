"""
Configuration settings for the application
"""

import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('nevie_api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "100"))
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

# API Configuration
API_TITLE = os.getenv("API_TITLE", "NEVIE-GLOBAL™ Test API")
API_DESCRIPTION = os.getenv("API_DESCRIPTION", "API for NEVIE-GLOBAL™ Test 1")
API_VERSION = os.getenv("API_VERSION", "1.0.0")

# ngrok Configuration (for cloud n8n access)
NGROK_URL = os.getenv("NGROK_URL")
API_PUBLIC_URL = f"{NGROK_URL}/nevie/test"

