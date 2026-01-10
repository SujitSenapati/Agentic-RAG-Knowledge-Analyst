"""
FastAPI-based REST API for the Agentic RAG system.

Responsibilities:
- Provide REST API endpoints for the frontend
- Forward user questions to the agent execution loop
- Return the final answer and agent trace as JSON
- Enable CORS for frontend communication
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Tuple
from app.agent.agent_loop import run_agent

app = FastAPI(
    title="Agentic RAG API",
    description="REST API for Enterprise Knowledge Analyst",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    """Request model for asking a question."""
    question: str


class AgentResponse(BaseModel):
    """Response model containing answer and trace."""
    answer: str
    trace: Dict[str, Any]


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Agentic RAG API is running"}


@app.post("/api/ask", response_model=AgentResponse)
def ask_agent(request: QuestionRequest):
    """
    Handle a user question and return the agent's answer and trace.

    Args:
        request: QuestionRequest containing the user's question

    Returns:
        AgentResponse with answer and execution trace

    Raises:
        HTTPException: If an error occurs during agent execution
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        answer, trace = run_agent(request.question)
        
        return AgentResponse(answer=answer, trace=trace)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent execution failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
