## Change

Describe the behavior and contract surface changed.

## Compatibility

State the minimum Python, API and type compatibility impact.

## Checks

- [ ] `python scripts/generate.py`
- [ ] `ruff check . && ruff format --check .`
- [ ] `mypy && pytest`
- [ ] `python -m build && python -m twine check dist/*`
- [ ] Examples and fixtures contain synthetic data only
