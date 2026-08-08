# Contributing

Issues and pull requests are welcome. Use synthetic data in every test and example.

## Set up

Python 3.10 through 3.13 is supported.

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
```

## Change the contract surface

The public OpenAPI document owns endpoint names, parameters and models. Update the contract first, then replace `openapi/openapi.yaml`, review the provenance record and regenerate:

```bash
python scripts/generate.py
```

Do not hand-edit files under `src/heyrafiki/api` or `src/heyrafiki/models`.

## Check a change

```bash
python scripts/generate.py
ruff check .
ruff format --check .
mypy
pytest
python -m build
python -m twine check dist/*
```

Before opening a pull request, inspect the package contents and confirm that no credentials, personal data, health information or internal material is present.

By contributing, you agree that your contribution is licensed under Apache-2.0.
