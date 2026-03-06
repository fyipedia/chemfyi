# chemfyi

Periodic table and chemistry reference API client — [chemfyi.com](https://chemfyi.com)

## Install

```bash
pip install chemfyi
```

## Quick Start

```python
from chemfyi.api import ChemFYI

with ChemFYI() as api:
    results = api.search("oxygen")
    print(results)
```

## License

MIT
