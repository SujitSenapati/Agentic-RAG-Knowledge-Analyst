@echo off
REM ============================================
REM Create virtual environment if it does not exist
REM ============================================

if not exist .venv (
    python -m venv .venv
)

REM ============================================
REM Activate virtual environment
REM ============================================

call .venv\Scripts\activate

REM ============================================
REM Upgrade pip and install dependencies
REM ============================================

python -m pip install --upgrade pip
pip install -r requirements.txt -q

echo.
echo Environment setup complete.
pause
