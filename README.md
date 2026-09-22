# ASSETMCP on Vercel

This repository exposes the upstream [ASSETMCP](https://github.com/evonar543/ASSETMCP) server as a stateless Streamable HTTP MCP endpoint on Vercel.

## Endpoint

After deployment:

`https://<your-vercel-domain>/api/mcp`

## Source

The MCP implementation is installed directly from the upstream ASSETMCP repository. This wrapper does not fork or modify the upstream tool implementation.

## Important runtime behavior

Vercel's function filesystem is ephemeral, so downloaded assets and generated previews are stored under `/tmp`. They should not be treated as persistent storage.

The endpoint uses stateless Streamable HTTP with JSON responses because that mode is appropriate for serverless environments.
