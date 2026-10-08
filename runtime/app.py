"""Minimal read-only ASGI application; no external dependencies required.

FastAPI integration will be added after authentication and permission design.
"""
import json
from typing import Callable


async def app(scope: dict, receive: Callable, send: Callable) -> None:
    if scope["type"] != "http":
        return
    method = scope.get("method", "")
    path = scope.get("path", "")
    if method == "GET" and path == "/health":
        status, body = 200, {"status": "ok"}
    elif path == "/health":
        status, body = 405, {"error": "method_not_allowed"}
    else:
        status, body = 404, {"error": "not_found"}
    payload = json.dumps(body, separators=(",", ":")).encode("utf-8")
    await send({"type": "http.response.start", "status": status,
                "headers": [(b"content-type", b"application/json"),
                            (b"content-length", str(len(payload)).encode("ascii")),
                            (b"cache-control", b"no-store")]})
    await send({"type": "http.response.body", "body": payload})
