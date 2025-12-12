"""
Configuration settings for the application
"""

import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging - Normal logs
logging.basicConfig(
    level=logging.INFO,  # INFO level captures INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('normal.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Configure error logging - Separate error.log
error_logger = logging.getLogger('error')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('error.log')
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
error_logger.addHandler(error_handler)
error_logger.propagate = False  # Don't propagate to root logger

# OpenAI Configuration
# To test error logging: Comment out line below, uncomment the OPENAI_API_KEY_TEST line
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_TEST")  # Uncomment this to use fake key for testing
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "100"))
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

# API Configuration
API_TITLE = os.getenv("API_TITLE", "NEVIE-GLOBAL™ Test API")
API_DESCRIPTION = os.getenv("API_DESCRIPTION", "API for NEVIE-GLOBAL™ Test 1 & 2")
API_VERSION = os.getenv("API_VERSION", "1.0.0")

# ngrok Configuration (for cloud n8n access)
NGROK_URL = os.getenv("NGROK_URL")
API_PUBLIC_URL = f"{NGROK_URL}/nevie/test"

