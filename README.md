# ASSETMCP HTTP on Vercel

HTTP wrapper around the upstream ASSETMCP server by evonar543.

MCP endpoint:

https://assetmcp-vercel-http.vercel.app/api/mcp

Health check:

https://assetmcp-vercel-http.vercel.app/api/health

The wrapper targets MCP 1.30.0 and configures Streamable HTTP through the upstream FastMCP settings API. The production and deployment Vercel host aliases are explicitly allowed by MCP DNS-rebinding protection. The generated Starlette application is exported directly so its own MCP session-manager lifespan is preserved on Vercel.

Runtime asset files are stored under /tmp because Vercel's function filesystem is ephemeral.
