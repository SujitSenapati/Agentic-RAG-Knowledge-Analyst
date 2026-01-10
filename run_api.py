"""
Script to run the FastAPI backend server.
Replaces the Gradio UI with a REST API for the Next.js frontend.
"""

import uvicorn

if __name__ == "__main__":
    print("Starting Agentic RAG API server...")
    print("API will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
