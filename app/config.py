"""
Application configuration and environment loading.

Responsibilities:
- Load environment variables
- Validate required configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

VECTORSTORE_DIR = "vectorstores"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is required")
