"""Command-line interface for chemfyi."""

from __future__ import annotations

import json

import typer

from chemfyi.api import ChemFYI

app = typer.Typer(help="ChemFYI — Periodic table and chemistry reference API client.")


@app.command()
def search(query: str) -> None:
    """Search chemfyi.com."""
    with ChemFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
