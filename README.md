# ASSETMCP HTTP on Vercel

HTTP wrapper around the upstream ASSETMCP server by evonar543.

MCP endpoint:

https://assetmcp-vercel-http.vercel.app/api/mcp

The endpoint uses Streamable HTTP in stateless JSON mode. Vercel routes /api/* to api/index.py, so the MCP transport is explicitly mounted at /api/mcp.

Runtime asset files are stored in /tmp because Vercel's function filesystem is ephemeral.
