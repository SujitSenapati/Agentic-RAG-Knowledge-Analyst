"""
DEPRECATED: This script runs the legacy Gradio UI.
For the new Next.js frontend, use run_api.py instead.

To run the modern stack:
1. Backend: python run_api.py
2. Frontend: cd frontend && npm run dev
"""

from app.ui.gradio_app import launch

if __name__ == "__main__":
    print("⚠️  WARNING: Running legacy Gradio UI")
    print("📝 For the modern Next.js frontend, run:")
    print("   Backend:  python run_api.py")
    print("   Frontend: cd frontend && npm run dev")
    print()
    launch()
