# chemfyi

[![PyPI version](https://agentgif.com/badge/pypi/chemfyi/version.svg)](https://pypi.org/project/chemfyi/)
[![Python](https://img.shields.io/pypi/pyversions/chemfyi)](https://pypi.org/project/chemfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.org/project/chemfyi/)

Python API client and CLI for the periodic table, chemical compounds, and reactions. Access 118 elements with full electron configurations and physical properties, 500 compounds with molecular formulas and IUPAC names, 371 chemical reactions with balanced equations, and 95 interactive experiments — all with zero dependencies.

Extracted from [ChemFYI](https://chemfyi.com/), a chemistry reference platform with 244 glossary terms, 250 educational guides, and interactive tools for students, educators, and developers exploring the periodic table and chemical sciences.

> **Explore chemistry at [chemfyi.com](https://chemfyi.com/)** — browse the [periodic table](https://chemfyi.com/elements/), look up [compounds](https://chemfyi.com/compounds/), study [reactions](https://chemfyi.com/reactions/), and read the [chemistry glossary](https://chemfyi.com/glossary/).

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/chemfyi/main/demo.gif" alt="chemfyi demo — periodic table lookup, element properties, and compound search in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You Can Do](#what-you-can-do)
  - [Periodic Table & Elements](#periodic-table--elements)
  - [Chemical Compounds](#chemical-compounds)
  - [Chemical Reactions](#chemical-reactions)
  - [Interactive Experiments](#interactive-experiments)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [API Reference](#api-reference)
- [Learn More About Chemistry](#learn-more-about-chemistry)
- [Also Available](#also-available)
- [Science FYI Family](#science-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install chemfyi                # Core (zero deps)
pip install "chemfyi[cli]"         # + Command-line interface (typer, rich)
pip install "chemfyi[mcp]"         # + MCP server for AI assistants
pip install "chemfyi[api]"         # + HTTP client for chemfyi.com API
pip install "chemfyi[all]"         # Everything
```

Or run instantly without installing:

```bash
uvx --from chemfyi chemfyi search oxygen
```

## Quick Start

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    # Look up any of the 118 elements by slug
    hydrogen = api.get_element("hydrogen")
    print(hydrogen["symbol"])                  # H
    print(hydrogen["atomic_number"])           # 1
    print(hydrogen["atomic_mass"])             # 1.008
    print(hydrogen["electron_configuration"])  # 1s1

    # Search across elements, compounds, and reactions
    results = api.search("carbon dioxide")
    print(results["count"])  # Number of matches

    # List all compounds with pagination
    compounds = api.list_compounds(limit=10)
    print(compounds["count"])  # 500 total compounds
```

## What You Can Do

### Periodic Table & Elements

The periodic table organizes all **118 confirmed elements** by atomic number, electron configuration, and recurring chemical properties. Elements are arranged in 18 groups (columns) and 7 periods (rows), with the lanthanides and actinides forming two additional rows. ChemFYI provides complete data for every element.

| Category | Count | Examples |
|----------|-------|---------|
| **Alkali Metals** | 6 | Lithium (Li), Sodium (Na), Potassium (K) |
| **Alkaline Earth Metals** | 6 | Beryllium (Be), Magnesium (Mg), Calcium (Ca) |
| **Transition Metals** | 38 | Iron (Fe), Copper (Cu), Gold (Au), Platinum (Pt) |
| **Post-Transition Metals** | 7 | Aluminum (Al), Tin (Sn), Lead (Pb) |
| **Metalloids** | 6 | Silicon (Si), Germanium (Ge), Arsenic (As) |
| **Nonmetals** | 7 | Carbon (C), Nitrogen (N), Oxygen (O), Sulfur (S) |
| **Halogens** | 5 | Fluorine (F), Chlorine (Cl), Bromine (Br), Iodine (I) |
| **Noble Gases** | 7 | Helium (He), Neon (Ne), Argon (Ar), Krypton (Kr) |
| **Lanthanides** | 15 | Cerium (Ce), Neodymium (Nd), Europium (Eu) |
| **Actinides** | 15 | Uranium (U), Plutonium (Pu), Thorium (Th) |

Each element includes atomic mass, density, melting/boiling points, electron configuration, electronegativity (Pauling scale), ionization energy, and electron affinity.

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    # Retrieve complete element data — all 118 elements available
    iron = api.get_element("iron")
    print(iron["symbol"])                  # Fe
    print(iron["atomic_number"])           # 26
    print(iron["atomic_mass"])             # 55.845
    print(iron["electron_configuration"])  # [Ar] 3d6 4s2
    print(iron["electronegativity"])       # 1.83
    print(iron["phase_at_stp"])            # Solid
    print(iron["block"])                   # d
    print(iron["group_number"])            # 8
    print(iron["period"])                  # 4
```

Learn more: [Periodic Table](https://chemfyi.com/elements/) · [Chemistry Glossary](https://chemfyi.com/glossary/) · [Chemistry Guides](https://chemfyi.com/guides/)

### Chemical Compounds

ChemFYI catalogs **500 chemical compounds** with molecular formulas, IUPAC nomenclature, structural information, and physical properties. Compounds span inorganic salts, organic molecules, acids, bases, and coordination complexes.

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    # Browse the compound database — 500 compounds indexed
    compounds = api.list_compounds(limit=5)
    for compound in compounds["results"]:
        print(compound["slug"], compound.get("name", ""))

    # Get detailed compound information
    detail = api.get_compound("sodium-chloride")
    print(detail)
```

Learn more: [Compounds Database](https://chemfyi.com/compounds/) · [Chemistry Guides](https://chemfyi.com/guides/)

### Chemical Reactions

Explore **371 chemical reactions** with balanced equations, reaction types (synthesis, decomposition, single replacement, double replacement, combustion, redox), and practical applications. Each reaction includes reactants, products, and conditions.

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    # Browse reactions — 371 reactions with balanced equations
    reactions = api.list_reactions(limit=5)
    for rxn in reactions["results"]:
        print(rxn["slug"])

    # Search for specific reaction types
    combustion = api.search("combustion")
    print(combustion["count"])
```

Learn more: [Reactions Database](https://chemfyi.com/reactions/) · [Chemistry Glossary](https://chemfyi.com/glossary/)

### Interactive Experiments

ChemFYI includes **95 interactive experiments** with step-by-step procedures, safety guidelines, and expected observations — designed for chemistry education from high school through university level.

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    # Browse 95 experiments with detailed procedures
    experiments = api.list_experiments(limit=5)
    for exp in experiments["results"]:
        print(exp["slug"])
```

Learn more: [Experiments](https://chemfyi.com/experiments/) · [Chemistry Guides](https://chemfyi.com/guides/)

## Command-Line Interface

```bash
pip install "chemfyi[cli]"

chemfyi search oxygen                # Search elements, compounds, reactions
chemfyi search "sulfuric acid"       # Search compounds by name
chemfyi search combustion            # Search reactions by type
```

## MCP Server (Claude, Cursor, Windsurf)

Add chemistry lookup tools to any AI assistant that supports [Model Context Protocol](https://modelcontextprotocol.io/).

```bash
pip install "chemfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "chemfyi": {
            "command": "uvx",
            "args": ["--from", "chemfyi[mcp]", "python", "-m", "chemfyi.mcp_server"]
        }
    }
}
```

## REST API Client

```bash
pip install "chemfyi[api]"
```

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    elements = api.list_elements()          # GET /api/v1/elements/
    hydrogen = api.get_element("hydrogen")  # GET /api/v1/elements/hydrogen/
    compounds = api.list_compounds()        # GET /api/v1/compounds/
    reactions = api.list_reactions()         # GET /api/v1/reactions/
    results = api.search("oxygen")          # GET /api/v1/search/?q=oxygen
```

### Example

```bash
curl -s "https://chemfyi.com/api/v1/elements/hydrogen/"
```

```json
{
  "atomic_number": 1,
  "symbol": "H",
  "slug": "hydrogen",
  "category": "nonmetal",
  "atomic_mass": 1.008,
  "electron_configuration": "1s1",
  "electronegativity": 2.2,
  "phase_at_stp": "Gas",
  "block": "s",
  "group_number": 1,
  "period": 1
}
```

Full API documentation at [chemfyi.com/developers/](https://chemfyi.com/developers/).

## API Reference

| Method | Description |
|--------|-------------|
| `list_elements(**params)` | List all 118 elements with pagination |
| `get_element(slug)` | Get element by slug (e.g., "hydrogen", "iron") |
| `list_compounds(**params)` | List all 500 compounds |
| `get_compound(slug)` | Get compound detail |
| `list_reactions(**params)` | List all 371 reactions |
| `get_reaction(slug)` | Get reaction detail with balanced equation |
| `list_experiments(**params)` | List all 95 experiments |
| `get_experiment(slug)` | Get experiment detail with procedures |
| `list_categories(**params)` | List element categories |
| `get_category(slug)` | Get category detail |
| `list_applications(**params)` | List industrial applications |
| `get_application(slug)` | Get application detail |
| `list_glossary(**params)` | List 244 chemistry glossary terms |
| `get_term(slug)` | Get glossary term definition |
| `list_guides(**params)` | List 250 educational guides |
| `get_guide(slug)` | Get guide content |
| `search(query)` | Search across all chemistry content |

## Learn More About Chemistry

- **Browse**: [Periodic Table](https://chemfyi.com/elements/) · [Compounds](https://chemfyi.com/compounds/) · [Reactions](https://chemfyi.com/reactions/) · [Experiments](https://chemfyi.com/experiments/)
- **Reference**: [Chemistry Glossary](https://chemfyi.com/glossary/) · [Element Categories](https://chemfyi.com/categories/)
- **Guides**: [Educational Guides](https://chemfyi.com/guides/)
- **API**: [REST API Docs](https://chemfyi.com/developers/) · [OpenAPI Spec](https://chemfyi.com/api/v1/)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install chemfyi` | [npm](https://www.npmjs.com/package/chemfyi) |
| **MCP** | `uvx --from "chemfyi[mcp]" python -m chemfyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Science FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem — physical sciences, chemistry, geology, astronomy, and materials.

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| **chemfyi** | [PyPI](https://pypi.org/project/chemfyi/) | [npm](https://www.npmjs.com/package/chemfyi) | **Periodic table, 500 compounds, 371 reactions — [chemfyi.com](https://chemfyi.com/)** |
| alloyfyi | [PyPI](https://pypi.org/project/alloyfyi/) | [npm](https://www.npmjs.com/package/alloyfyi) | 765 metal alloys, 12 families, compositions — [alloyfyi.com](https://alloyfyi.com/) |
| gemfyi | [PyPI](https://pypi.org/project/gemfyi/) | [npm](https://www.npmjs.com/package/gemfyi) | 442 gemstones, Mohs scale, grading — [gemfyi.com](https://gemfyi.com/) |
| starfyi | [PyPI](https://pypi.org/project/starfyi/) | [npm](https://www.npmjs.com/package/starfyi) | 119,602 stars, 6,128 exoplanets, 13,305 deep-sky objects — [starfyi.com](https://starfyi.com/) |
| mineralfyi | [PyPI](https://pypi.org/project/mineralfyi/) | [npm](https://www.npmjs.com/package/mineralfyi) | 6,215 minerals, 7 crystal systems — [mineralfyi.com](https://mineralfyi.com/) |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies — [colorfyi.com](https://colorfyi.com/) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis — [emojifyi.com](https://emojifyi.com/) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats — [symbolfyi.com](https://symbolfyi.com/) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings — [unicodefyi.com](https://unicodefyi.com/) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS — [fontfyi.com](https://fontfyi.com/) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times — [distancefyi.com](https://distancefyi.com/) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours — [timefyi.com](https://timefyi.com/) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements — [namefyi.com](https://namefyi.com/) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units — [unitfyi.com](https://unitfyi.com/) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation — [holidayfyi.com](https://holidayfyi.com/) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | — | Cocktail ABV, calories, flavor — [cocktailfyi.com](https://cocktailfyi.com/) |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | — | Unified CLI: `fyi chem info hydrogen` — [fyipedia.com](https://fyipedia.com/) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | — | Unified MCP hub for AI assistants — [fyipedia.com](https://fyipedia.com/) |

## Embed Widget

Embed [ChemFYI](https://chemfyi.com) widgets on any website with [chemfyi-embed](https://widget.chemfyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/chemfyi-embed@1/dist/embed.min.js"></script>
<div data-chemfyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.chemfyi.com)

## License

MIT
