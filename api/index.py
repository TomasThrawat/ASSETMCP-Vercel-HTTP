import os

# Vercel functions are ephemeral. ASSETMCP keeps its writable runtime state in /tmp.
os.environ.setdefault("ASSETMCP_LIBRARY_DIR", "/tmp/assetmcp-assets")
os.environ.setdefault("ASSETMCP_PREVIEW_DIR", "/tmp/assetmcp-previews")

from mcp.server.transport_security import TransportSecuritySettings
from assetmcp.server import mcp, _ensure_roots

_ensure_roots()

_vercel_host = os.environ.get("VERCEL_URL", "assetmcp-vercel-http.vercel.app")
_allowed_hosts = [
    _vercel_host,
    f"{_vercel_host}:*",
    "*.vercel.app",
    "*.vercel.app:*",
]

# Vercel sends /api/* requests to api/index.py without stripping the /api prefix.
# Therefore the MCP transport path must include /api.
app = mcp.streamable_http_app(
    streamable_http_path="/api/mcp",
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(
        allowed_hosts=_allowed_hosts,
    ),
)
