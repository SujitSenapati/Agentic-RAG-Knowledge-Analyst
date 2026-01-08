# Contributing to Agentic RAG Knowledge Analyst

Thank you for your interest in contributing to this project!

## Development Environment

### GitHub Codespaces (Recommended)

1. Open the project in GitHub Codespaces
2. The environment will automatically configure itself with:
   - Python 3.11
   - All required dependencies
   - VS Code extensions (Python, Pylance, Black, etc.)
   - Port forwarding for Gradio UI

3. Set up your environment variables:
   ```bash
   cp .env.template .env
   # Add your OPENAI_API_KEY to .env
   ```

### Local Development

Follow the setup instructions in [README.md](README.md#option-2-local-setup).

## Project Structure

The project is organized into two main phases:

1. **Offline Ingestion** (`scripts/ingest_all.py`)
   - Fetches and processes documents
   - Creates vector embeddings
   - Stores in ChromaDB

2. **Online Agent Runtime** (`app/`)
   - Planner: Intent detection and tool selection
   - Tools: Retrieval from vector stores
   - Reasoner: Answer generation
   - Critic: Logical verification
   - Judge: Quality evaluation

## Running Tests

```bash
pytest -v
```

Tests validate:
- Planner decisions and tool selection
- Clarification behavior
- Agent loop execution
- Trace structure consistency

## Code Style

- Use Black for formatting (configured in devcontainer)
- Follow PEP 8 guidelines
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

## Making Changes

1. Create a new branch for your feature/fix
2. Make your changes
3. Run tests to ensure nothing breaks
4. Update documentation if needed
5. Submit a pull request

## Testing Your Changes

### Test the Agent Loop

```bash
python run.py
```

Then test various queries in the Gradio UI:
- Simple questions (e.g., "What is a Kubernetes pod?")
- Ambiguous questions (should trigger clarification)
- Cross-domain questions (should use multiple tools)

### Test Specific Components

```bash
# Test planner
pytest tests/test_planner.py -v

# Test agent loop
pytest tests/test_agent_loop.py -v

# Test judge
pytest tests/test_judge.py -v
```

## Architecture Guidelines

- **Separation of Concerns**: Ingestion is offline, runtime is read-only
- **No Direct LLM Calls in Tools**: Tools only retrieve from vector stores
- **Externalized Prompts**: All prompts live in `prompts/` directory
- **Auditable Traces**: Every agent run produces a complete trace
- **Controlled Retry**: Maximum one retry per query

## Documentation

- Update `docs/` if you add/change agent components
- Update `README.md` for architectural changes
- Add docstrings to all new functions/classes
- Use type hints for all function parameters

## Building Documentation

```bash
mkdocs serve
```

Visit `http://localhost:8000` to preview documentation changes.

## Questions?

Open an issue on GitHub for questions or discussions about contributing.
