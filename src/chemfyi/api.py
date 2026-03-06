"""HTTP API client for chemfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install chemfyi[api]``

Usage::

    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        results = api.search("oxygen")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class ChemFYI:
    """API client for the chemfyi.com REST API.

    Args:
        base_url: API base URL. Defaults to ``https://chemfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://chemfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    def search(self, query: str) -> dict[str, Any]:
        """Search across all content.

        Args:
            query: Search term (e.g. ``"oxygen"``).
        """
        return self._get("/api/search/", q=query)

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> ChemFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
