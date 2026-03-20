"""HTTP API client for chemfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install chemfyi[api]``

Usage::

    from chemfyi.api import ChemFYI

    with ChemFYI() as api:
        items = api.list_applications()
        detail = api.get_application("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class ChemFYI:
    """API client for the chemfyi.com REST API.

    Provides typed access to all chemfyi.com endpoints including
    list, detail, and search operations.

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
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_applications(self, **params: Any) -> dict[str, Any]:
        """List all applications."""
        return self._get("/api/v1/applications/", **params)

    def get_application(self, slug: str) -> dict[str, Any]:
        """Get application by slug."""
        return self._get(f"/api/v1/applications/" + slug + "/")

    def list_categories(self, **params: Any) -> dict[str, Any]:
        """List all categories."""
        return self._get("/api/v1/categories/", **params)

    def get_category(self, slug: str) -> dict[str, Any]:
        """Get category by slug."""
        return self._get(f"/api/v1/categories/" + slug + "/")

    def list_compounds(self, **params: Any) -> dict[str, Any]:
        """List all compounds."""
        return self._get("/api/v1/compounds/", **params)

    def get_compound(self, slug: str) -> dict[str, Any]:
        """Get compound by slug."""
        return self._get(f"/api/v1/compounds/" + slug + "/")

    def list_elements(self, **params: Any) -> dict[str, Any]:
        """List all elements."""
        return self._get("/api/v1/elements/", **params)

    def get_element(self, slug: str) -> dict[str, Any]:
        """Get element by slug."""
        return self._get(f"/api/v1/elements/" + slug + "/")

    def list_experiments(self, **params: Any) -> dict[str, Any]:
        """List all experiments."""
        return self._get("/api/v1/experiments/", **params)

    def get_experiment(self, slug: str) -> dict[str, Any]:
        """Get experiment by slug."""
        return self._get(f"/api/v1/experiments/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_glossary_categories(self, **params: Any) -> dict[str, Any]:
        """List all glossary categories."""
        return self._get("/api/v1/glossary-categories/", **params)

    def get_glossary_category(self, slug: str) -> dict[str, Any]:
        """Get glossary category by slug."""
        return self._get(f"/api/v1/glossary-categories/" + slug + "/")

    def list_guide_series(self, **params: Any) -> dict[str, Any]:
        """List all guide series."""
        return self._get("/api/v1/guide-series/", **params)

    def get_guide_sery(self, slug: str) -> dict[str, Any]:
        """Get guide sery by slug."""
        return self._get(f"/api/v1/guide-series/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_reactions(self, **params: Any) -> dict[str, Any]:
        """List all reactions."""
        return self._get("/api/v1/reactions/", **params)

    def get_reaction(self, slug: str) -> dict[str, Any]:
        """Get reaction by slug."""
        return self._get(f"/api/v1/reactions/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> ChemFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
