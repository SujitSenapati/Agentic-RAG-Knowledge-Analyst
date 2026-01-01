"""
LLM initialization.

Responsibilities:
- Load environment variables
- Initialize LLM clients
- Fail fast if API key is missing
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Ensure .env is loaded before client creation
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY not found. Ensure .env exists and is loaded."
    )
__all__ = ["llm_fast", "llm_reasoning"]

# Primary low-latency LLM used for short-form tasks such as the
# critic and judge prompts, quick clarifications, and retries.
llm_fast: ChatOpenAI = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Higher-capacity reasoning LLM intended for longer-form chain-of-thought
# style reasoning when the agent needs deeper analysis.
llm_reasoning: ChatOpenAI = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)
