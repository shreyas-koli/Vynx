# VYNX API

Minimal FastAPI service for local VYNX orchestration.

## Run locally

From this directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8765
```

The service exposes `GET /health` and does not download or process media yet.

