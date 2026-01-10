@echo off
REM Startup script for the Agentic RAG system with Next.js frontend

echo ========================================
echo Agentic RAG - Modern Stack Setup
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo [ERROR] .env file not found!
    echo Please copy .env.template to .env and add your OPENAI_API_KEY
    echo.
    echo Run: copy .env.template .env
    echo.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist .venv (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install Python dependencies
echo [INFO] Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Starting Backend API Server
echo ========================================
echo.
echo Backend will run at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo.
echo To start the frontend:
echo 1. Open a new terminal
echo 2. Run: cd frontend
echo 3. Run: npm install (first time only)
echo 4. Run: npm run dev
echo.
echo Frontend will be at: http://localhost:3000
echo.
echo Press Ctrl+C to stop the backend server
echo ========================================
echo.

python run_api.py
