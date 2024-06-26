# MP Biopath Pathway Generator

Generate denormalized pathways for MP Biopath.

## Setup

### Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/reactome/mp-biopath-pathway-generator.git
   ```

2. Generate the files:
   ```bash
   poetry run python create-denormalized-pathways.py
  ```

### Run Mypy

```bash
poetry run mypy --ignore-missing-imports .
```

### Run fake8

```bash
poetry run flake8 .
```

### Create db-id-name-mapping-file.tsv

```bash
python src/create-db-id-name-mapping-file.py
```
