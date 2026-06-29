# TouchAir OS – Spatial Interactive Holographic Computing Platform

**Status:** Phase-1 Prototype · Core backend skeleton ready

## Quick Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Docker

```bash
docker compose up --build
```

Endpoints
- `GET  /` – Dashboard / landing page  
- `GET  /api/health` – Health & liveness  
- `GET  /api/system/info` – Build metadata  
- `GET  /docs` – Auto-generated Swagger  
- `WS   /ws/spatial` – Real-time spatial events WebSocket

## Architecture

```text
User
 ↓
Cameras + Sensors
 ↓
Spatial Engine  ←── you are here (backend entry-point)
 ↓
Interaction Engine
 ↓
Rendering / Holography
```
