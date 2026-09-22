import os

# Vercel's function filesystem is ephemeral. Keep ASSETMCP's writable state in /tmp.
os.environ.setdefault("ASSETMCP_LIBRARY_DIR", "/tmp/assetmcp-assets")
os.environ.setdefault("ASSETMCP_PREVIEW_DIR", "/tmp/assetmcp-previews")

from mcp.server.transport_security import TransportSecuritySettings
from assetmcp.server import mcp, _ensure_roots

_ensure_roots()

_vercel_host = os.environ.get("VERCEL_URL")
if _vercel_host:
    _allowed_hosts = [_vercel_host, f"{_vercel_host}:*"]
else:
    _allowed_hosts = ["*.vercel.app", "*.vercel.app:*"]

# ASSETMCP already contains all of the tools. This only exposes the same
# FastMCP instance as a stateless Streamable HTTP ASGI application.
app = mcp.streamable_http_app(
    streamable_http_path="/mcp",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
        allowed_hosts=_allowed_hosts,
    ),
)
