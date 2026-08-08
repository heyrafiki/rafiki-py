# Generation provenance

The typed models and operation modules are generated from the public Heyrafiki OpenAPI contract.

| Input | Value |
| --- | --- |
| Contract repository | `heyrafiki/openapi` |
| Contract commit | `327e0a70de92771d3930380ce552c00e0ed8fc52` |
| Contract SHA-256 | `e07f8f5bde590f826e1edb91b42ba30686a74ae4e6c0fdf1223efcd0749541ed` |
| Generator | `openapi-python-client==0.29.0` |
| Generated operations | 30 |

`openapi/openapi.yaml` is the unmodified source snapshot. The generator does not currently accept an array reference combined with `minItems` through `allOf`. `scripts/prepare_contract.py` replaces that single composition in `ClaimEvidenceInput.evidence_refs` with its equivalent resolved array schema before generation. The script verifies the source digest and the exact reviewed input before applying the transform.

Regenerate with:

```bash
python -m pip install -e ".[dev]"
python scripts/generate.py
```

CI regenerates the package and rejects any diff. Contract updates require a new reviewed snapshot, commit reference, digest and changelog entry.
