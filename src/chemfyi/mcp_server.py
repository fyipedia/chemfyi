"""MCP server for chemfyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from chemfyi.api import ChemFYI

mcp = FastMCP("chemfyi")


@mcp.tool()
def search_chemfyi(query: str) -> dict[str, Any]:
    """Search chemfyi.com for content matching the query."""
    with ChemFYI() as api:
        return api.search(query)
