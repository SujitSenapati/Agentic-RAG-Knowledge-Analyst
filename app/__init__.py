"""
`app` package for the Enterprise Knowledge Analyst application.

This package contains modules for ingestion, chunking, LLM clients,
agent orchestration, retrieval tools, and a small Gradio UI used for
local testing. Each submodule exposes a focused API used by the
agent execution loop and components.

Typical usage:
- Import top-level helpers: `from app import utils`
- Run the agent loop: `from app.agent.agent_loop import run_agent`
"""
