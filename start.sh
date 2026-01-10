#!/bin/bash

# Startup script for the Agentic RAG system with Next.js frontend

echo "========================================"
echo "Agentic RAG - Modern Stack Setup"
echo "========================================"
echo

# Check if .env exists
if [ ! -f .env ]; then
    echo "[ERROR] .env file not found!"
    echo "Please copy .env.template to .env and add your OPENAI_API_KEY"
    echo
    echo "Run: cp .env.template .env"
    echo
    exit 1
fi

# Check if virtual environment exists
if [ ! -d .venv ]; then
    echo "[INFO] Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "[INFO] Activating virtual environment..."
source .venv/bin/activate

# Install Python dependencies
echo "[INFO] Installing Python dependencies..."
pip install -r requirements.txt

echo
echo "========================================"
echo "Starting Backend API Server"
echo "========================================"
echo
echo "Backend will run at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo
echo "To start the frontend:"
echo "1. Open a new terminal"
echo "2. Run: cd frontend"
echo "3. Run: npm install (first time only)"
echo "4. Run: npm run dev"
echo
echo "Frontend will be at: http://localhost:3000"
echo
echo "Press Ctrl+C to stop the backend server"
echo "========================================"
echo

python run_api.py
