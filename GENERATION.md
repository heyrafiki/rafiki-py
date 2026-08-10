# Generation provenance

The typed models and operation modules are generated from the public Heyrafiki OpenAPI contract.

| Input | Value |
| --- | --- |
| Contract repository | `heyrafiki/contract` |
| Contract commit | `e629a129462d82534a5e3ed16035da863305d283` |
| Contract SHA-256 | `d1c7349246e766aaf961e11c591a32de0afcc5900649be462e3656059722b211` |
| Generator | `openapi-python-client==0.29.0` |
| Generated operations | 30 |

`openapi/openapi.yaml` is the unmodified source snapshot. The generator does not currently accept an array reference combined with `minItems` through `allOf`. `scripts/prepare_contract.py` replaces that single composition in `ClaimEvidenceInput.evidence_refs` with its equivalent resolved array schema before generation. The generation step also routes RFC 3339 timestamp parsing through the Python 3.10 compatibility helper. The scripts verify the source digest and reviewed inputs before applying either transform.

Regenerate with:

```bash
python -m pip install -e ".[dev,generation]"
python scripts/generate.py
```

Generation requires Python 3.11 or newer. The generated client supports Python 3.10.

CI regenerates the package and rejects any diff. Contract updates require a new reviewed snapshot, commit reference, digest and changelog entry.
