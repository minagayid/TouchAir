from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse, HTMLResponse
import asyncio
import importlib_metadata as metadata

app = FastAPI(title="TouchAir API", version="0.1.0")


@app.get("/api/health")
async def health_check():
    """Basic liveness probe for orchestrators and load balancers."""
    return {"status": "ok", "version": app.version}


@app.get("/api/system/info")
async def system_info():
    """Return build / environment metadata for diagnostics."""
    return {
        "name": app.title,
        "version": app.version,
        "fastapi": metadata.version("fastapi"),
    }


@app.websocket("/ws/spatial")
async def spatial_stream(websocket: WebSocket):
    """
    WebSocket entry-point for real-time spatial events.
    Expects JSON blobs: {"event": "hand_pose", "payload": {...}}.
    Replies with the same payload echoed + server timestamp.
    """
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_json()
            message["server_ts"] = asyncio.get_event_loop().time()
            await websocket.send_json(message)
    except Exception:
        await websocket.close()


# -- Static demo HTML served at root -----------------------------------------


@app.get("/", response_class=HTMLResponse)
async def demo():
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>TouchAir</title><style>body{font-family:system-ui;text-align:center;padding:2rem}
</style></head><body>
<h1>TouchAir API</h1><p>Spatial OS backend is running.</p>
<a href="/docs">API Docs</a> | <a href="/api/health">Health</a>
</body></html>"""
