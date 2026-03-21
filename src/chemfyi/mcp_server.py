"""MCP server for chemfyi — AI assistant tools for chemfyi.com.

Run: uvx --from "chemfyi[mcp]" python -m chemfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ChemFYI")


@mcp.tool()
def list_elements(limit: int = 20, offset: int = 0) -> str:
    """List elements from chemfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        data = api.list_elements(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No elements found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_element(slug: str) -> str:
    """Get detailed information about a specific element.

    Args:
        slug: URL slug identifier for the element.
    """
    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        data = api.get_element(slug)
        return str(data)


@mcp.tool()
def list_compounds(limit: int = 20, offset: int = 0) -> str:
    """List compounds from chemfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        data = api.list_compounds(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No compounds found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_chem(query: str) -> str:
    """Search chemfyi.com for chemical elements, compounds, and reactions.

    Args:
        query: Search query string.
    """
    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
