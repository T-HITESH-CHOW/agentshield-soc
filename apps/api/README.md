# AgentShield SOC API

Minimal FastAPI backend for AgentShield SOC.

Day 2 provides application bootstrap, configuration, and a deterministic `GET /health` endpoint. SOC features, databases, authentication, and AI are not implemented yet.

## Requirements

- Python 3.11 or newer

## Virtual environment

From `apps/api`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Settings are loaded from environment variables (and an optional local `.env` file) via pydantic-settings:

| Variable | Default | Purpose |
|---|---|---|
| `APP_NAME` | `AgentShield SOC API` | FastAPI title |
| `ENVIRONMENT` | `development` | Deployment label |
| `DEBUG` | `false` | FastAPI debug flag |

Do not put secrets in source code. Copy names from the repository root `.env.example` if you add a local `.env`.

## Run the server

From `apps/api` with the virtual environment activated:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Then open:

- API: http://127.0.0.1:8000
- Health: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Run tests

From `apps/api` with the virtual environment activated:

```powershell
pytest
```

## Current HTTP surface

| Method | Path | Status |
|---|---|---|
| `GET` | `/health` | Implemented |
| | `/api/v1/` | Router reserved; no SOC endpoints yet |
