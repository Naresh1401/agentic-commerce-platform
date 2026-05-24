# Setup

## Docker

```bash
docker compose up --build
```

## Local Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Local Frontend

```bash
cd frontend
npm install
npm run dev
```

## Local MCP

```bash
cd mcp-server
pip install -r requirements.txt
python server.py
```
