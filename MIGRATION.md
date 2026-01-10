# Migration Guide: Gradio → Next.js + FastAPI

This guide explains the transition from Gradio to a modern Next.js frontend with FastAPI backend.

## What Changed

### Old Architecture (Gradio)
- **UI**: Gradio Python library
- **Deployment**: Single Python process
- **Interaction**: Synchronous function calls

### New Architecture (Next.js + FastAPI)
- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **Backend**: FastAPI REST API
- **Interaction**: HTTP REST API
- **Deployment**: Separate frontend and backend processes

## Key Benefits

1. **Modern UI/UX**: Professional React-based interface with Tailwind styling
2. **Type Safety**: Full TypeScript support in frontend
3. **Better Performance**: Separate frontend/backend allows independent scaling
4. **API First**: Backend can be consumed by multiple clients
5. **Developer Experience**: Hot reload, better debugging, modern tooling

## File Structure Changes

### New Files Created

```
frontend/                          # New Next.js application
├── src/
│   ├── app/                      # Next.js app router
│   │   ├── layout.tsx           # Root layout
│   │   ├── page.tsx             # Home page
│   │   └── globals.css          # Global styles
│   ├── components/
│   │   └── AgentInterface.tsx   # Main UI component (replaces Gradio)
│   └── lib/
│       └── api.ts               # API client
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js

app/api.py                        # New FastAPI backend
run_api.py                        # New startup script for API
start.bat / start.sh              # Convenience startup scripts
```

### Modified Files

- `requirements.txt`: Replaced `gradio` with `fastapi` and `uvicorn`
- `run.py`: Added deprecation notice
- `README.md`: Updated setup instructions

### Unchanged Files

All core agent logic remains the same:
- `app/agent/` - All agent components
- `app/tools/` - Tool implementations
- `app/config.py`, `app/llms.py`, etc.

## Component Mapping

| Gradio Component | Next.js Equivalent |
|-----------------|-------------------|
| `gr.Textbox` | `<textarea>` with Tailwind styling |
| `gr.Button` | `<button>` with gradient styling |
| `gr.Markdown` | `<ReactMarkdown>` component |
| `gr.JSON` | `<pre>` with formatted JSON |
| `gr.Blocks` | React component structure |

## Running the New Stack

### Quick Start

**Option 1: Using startup scripts**
```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

**Option 2: Manual startup**

Terminal 1 (Backend):
```bash
python run_api.py
```

Terminal 2 (Frontend):
```bash
cd frontend
npm install  # First time only
npm run dev
```

### URLs

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## API Reference

### POST /api/ask

Request:
```json
{
  "question": "How do I scale a Kubernetes deployment?"
}
```

Response:
```json
{
  "answer": "To scale a Kubernetes deployment...",
  "trace": {
    "plan": ["..."],
    "tools_used": ["kubernetes_docs"],
    "...": "..."
  }
}
```

## Development

### Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
npm start

# Lint code
npm run lint
```

### Backend Development

The FastAPI backend supports hot reload:
```bash
python run_api.py
# Edit files in app/ and server auto-reloads
```

### Environment Variables

**Backend** (`.env`):
```env
OPENAI_API_KEY=your_key_here
LANGCHAIN_API_KEY=your_key_here  # Optional
```

**Frontend** (`frontend/.env.local`):
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Deployment Considerations

### Backend
- Use `uvicorn` with multiple workers in production
- Consider using Gunicorn as process manager
- Deploy on cloud platforms (AWS, GCP, Azure)

### Frontend
- Build static files: `npm run build`
- Deploy to Vercel, Netlify, or any static host
- Configure API URL environment variable

### Together
- Use reverse proxy (nginx) to serve both on same domain
- Configure CORS properly for production
- Use environment variables for API endpoints

## Troubleshooting

### Frontend can't connect to backend
- Check that backend is running on port 8000
- Verify CORS settings in `app/api.py`
- Check `NEXT_PUBLIC_API_URL` in frontend

### TypeScript errors
- Run `npm install` to ensure all deps are installed
- Delete `.next` folder and rebuild

### Port conflicts
- Change backend port in `run_api.py`
- Change frontend port: `npm run dev -- -p 3001`
- Update API URL accordingly

## Backwards Compatibility

The old Gradio UI is still available:
```bash
python run.py
```

However, it's marked as deprecated and will be removed in future versions.
