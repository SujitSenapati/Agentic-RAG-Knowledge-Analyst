#!/bin/bash

# Quick start script for GitHub Codespaces
# This script helps set up the environment after the devcontainer is ready

echo "🚀 Agentic RAG Knowledge Analyst - Quick Start"
echo "=============================================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.template .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Please add your OPENAI_API_KEY to the .env file"
    echo "   You can edit it by running: code .env"
    echo ""
else
    echo "✅ .env file already exists"
    echo ""
fi

# Check if OPENAI_API_KEY is set
if grep -q "your_openai_api_key_here" .env 2>/dev/null; then
    echo "⚠️  WARNING: OPENAI_API_KEY is not configured"
    echo "   Please edit .env and add your OpenAI API key"
    echo "   Run: code .env"
    echo ""
else
    echo "✅ OPENAI_API_KEY appears to be configured"
    echo ""
fi

# Check if vector stores exist
if [ -d "vectorstores/k8s" ]; then
    echo "✅ Vector stores found (data is ready)"
    echo ""
else
    echo "ℹ️  Vector stores not found"
    echo "   The project includes pre-built vector stores in the repository"
    echo "   If you want to re-ingest data, run: python scripts/ingest_all.py"
    echo ""
fi

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $PYTHON_VERSION"
echo ""

# Check if dependencies are installed
if python -c "import gradio" 2>/dev/null; then
    echo "✅ Dependencies are installed"
else
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the application, run:"
echo "   python run.py"
echo ""
echo "The Gradio UI will be available at: http://localhost:7860"
echo "(Codespaces will automatically forward the port)"
echo ""
