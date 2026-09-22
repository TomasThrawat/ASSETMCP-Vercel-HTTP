# ASSETMCP HTTP on Vercel

HTTP wrapper around the upstream ASSETMCP server by evonar543.

MCP endpoint:

https://assetmcp-vercel-http.vercel.app/api/mcp

Health check:

https://assetmcp-vercel-http.vercel.app/api/health

The wrapper uses Streamable HTTP in stateless JSON mode, with the MCP session manager started by the top-level ASGI lifespan for Vercel compatibility.

Runtime asset files are stored under /tmp because Vercel's function filesystem is ephemeral.
