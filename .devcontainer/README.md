# GitHub Codespaces Setup

This project is configured to work seamlessly with GitHub Codespaces.

## Quick Start

1. **Open in Codespaces**: Click the "Code" button on GitHub and select "Create codespace on main"

2. **Wait for setup**: The devcontainer will automatically:
   - Install Python 3.11
   - Install all dependencies from `requirements.txt`
   - Configure VS Code extensions (Python, Pylance, etc.)
   - Set up port forwarding for the Gradio UI (port 7860)

3. **Configure environment variables**:
   ```bash
   cp .env.template .env
   # Edit .env and add your OPENAI_API_KEY
   ```

4. **Ingest data** (optional - vector stores are included):
   ```bash
   python scripts/ingest_all.py
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the UI**: When Gradio starts, Codespaces will automatically forward port 7860. Click the notification or go to the "Ports" tab to open the UI.

## Features Included

- **Python 3.11** development environment
- **Pre-installed extensions**:
  - Python & Pylance for intelligent code completion
  - Black formatter for code formatting
  - Jupyter for notebook support
  - Ruff for fast linting
  - GitHub Copilot (if you have access)
- **Port forwarding** for Gradio UI (7860)
- **Git & Zsh** with oh-my-zsh configuration
- **Automatic dependency installation**

## Environment Variables

Required:
- `OPENAI_API_KEY`: Your OpenAI API key for LLM operations

Optional:
- `LANGCHAIN_TRACING_V2`: Enable LangSmith tracing (true/false)
- `LANGCHAIN_API_KEY`: Your LangSmith API key
- `LANGCHAIN_PROJECT`: Project name in LangSmith

## Running Tests

```bash
pytest tests/
```

## Building Documentation

```bash
mkdocs serve
```

The documentation will be available at port 8000 (automatically forwarded).

## Troubleshooting

### Missing API Key
If you see errors about missing API keys:
1. Make sure you've created `.env` from `.env.template`
2. Add your `OPENAI_API_KEY` to the `.env` file
3. Restart the application

### Port Already in Use
If port 7860 is already in use:
1. Stop the running process
2. Or modify the port in `run.py`

### Dependencies Not Installed
If dependencies are missing:
```bash
pip install -r requirements.txt
```
