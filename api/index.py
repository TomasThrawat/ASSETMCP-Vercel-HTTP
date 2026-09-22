import os

from starlette.requests import Request
from starlette.responses import JSONResponse

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
    "assetmcp-vercel-http.vercel.app",
    "assetmcp-vercel-http.vercel.app:*",
    "assetmcp-vercel-http-hyouka1.vercel.app",
    "assetmcp-vercel-http-hyouka1.vercel.app:*",
    "assetmcp-vercel-http-git-main-hyouka1.vercel.app",
    "assetmcp-vercel-http-git-main-hyouka1.vercel.app:*",
]

mcp.settings.streamable_http_path = "/api/mcp"
mcp.settings.stateless_http = True
mcp.settings.json_response = True
mcp.settings.transport_security = TransportSecuritySettings(
    allowed_hosts=_allowed_hosts,
)


@mcp.custom_route("/api/health", methods=["GET"])
async def health(_request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "server": "ASSETMCP"})


# MCP 1.30.0 reads Streamable HTTP options from FastMCP.settings.
# Its generated Starlette app owns the MCP session-manager lifespan,
# so export it directly instead of mounting a second ASGI application.
app = mcp.streamable_http_app()
