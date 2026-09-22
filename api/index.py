import os
from contextlib import asynccontextmanager

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

# Vercel Functions have an ephemeral writable filesystem.
os.environ.setdefault("ASSETMCP_LIBRARY_DIR", "/tmp/assetmcp-assets")
os.environ.setdefault("ASSETMCP_PREVIEW_DIR", "/tmp/assetmcp-previews")

from mcp.server.transport_security import TransportSecuritySettings
from assetmcp.server import mcp, _ensure_roots

_ensure_roots()

_vercel_host = os.environ.get("VERCEL_URL", "assetmcp-vercel-http.vercel.app")
_allowed_hosts = [
    _vercel_host,
    f"{_vercel_host}:*",
]

mcp_app = mcp.streamable_http_app(
    streamable_http_path="/api/mcp",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
        allowed_hosts=_allowed_hosts,
    ),
)


@asynccontextmanager
async def lifespan(_app: Starlette):
    # Mounting an MCP ASGI app disables its own lifespan. Start the
    # session manager from the top-level app instead.
    async with mcp.session_manager.run():
        yield


async def health(_request):
    return JSONResponse({"status": "ok", "server": "ASSETMCP"})


app = Starlette(
    routes=[
        Route("/api/health", health, methods=["GET"]),
        Mount("/", app=mcp_app),
    ],
    lifespan=lifespan,
)
