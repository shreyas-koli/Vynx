# VYNX

VYNX is a local-first media utility for analyzing permitted media URLs and,
in later phases, downloading and processing video and audio. It is intended
only for content the user owns, has permission to download, or that the
relevant service and license permit downloading. VYNX will not bypass DRM,
paywalls, authentication, or other access controls.

## Planned architecture

- **FastAPI API** in `services/api/` for local orchestration and health checks.
- **Downloader core** in `core/downloader/` for future yt-dlp and FFmpeg integration.
- **Next.js dashboard** in `apps/web/`.
- **Chromium extension** in `apps/extension/`.
- **Local data** in `data/`, with SQLite planned for a later phase.

## Repository structure

```text
apps/
  web/             Next.js dashboard placeholder
  extension/       Chromium Manifest V3 placeholder
services/
  api/             FastAPI service
core/
  downloader/      Future media integration package
data/              Local application data (currently empty)
docs/              Project documentation
scripts/           Development scripts
tests/             Cross-project tests
```

## Development prerequisites

- Windows, Git, Python 3.11+, Node.js LTS, and npm
- Uvicorn/FastAPI dependencies from `services/api/requirements.txt`
- Optional globally installed `yt-dlp` and FFmpeg for future phases

## Start the FastAPI backend

From the API directory:

```powershell
cd services\api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8765
```

The health check is available at <http://127.0.0.1:8765/health>.

## Start the Next.js frontend

From the web directory:

```powershell
cd apps\web
npm install
npm run dev
```

Open <http://localhost:3000>.

## Load the extension manually

1. Open `chrome://extensions` or `edge://extensions`.
2. Enable **Developer mode**.
3. Select **Load unpacked**.
4. Choose the `apps\extension` directory.
5. Open the extension popup to see the Phase 0 confirmation.

## Current project status

**Phase 0: Project Foundation** is the current scope. The API health endpoint,
frontend placeholder, extension placeholder, package layout, and documentation
are established. No media downloading or URL extraction is implemented.

## Future phases

1. API contracts and media URL analysis
2. Downloader and FFmpeg integration
3. Download queue, progress, history, and local persistence
4. Dashboard workflows and API integration
5. Browser extension URL handoff and IDM-style actions
6. Windows packaging and release hardening

