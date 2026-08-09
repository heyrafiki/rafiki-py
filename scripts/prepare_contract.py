from __future__ import annotations

import argparse
import copy
import hashlib
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "openapi" / "openapi.yaml"
EXPECTED_SOURCE_SHA256 = "d1c7349246e766aaf961e11c591a32de0afcc5900649be462e3656059722b211"


def source_digest() -> str:
    canonical_source = SOURCE.read_text(encoding="utf-8").encode("utf-8")
    return hashlib.sha256(canonical_source).hexdigest()


def prepare(target: Path) -> None:
    digest = source_digest()
    if digest != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(
            "The OpenAPI snapshot changed. Review the contract and update generation provenance "
            f"before regenerating (expected {EXPECTED_SOURCE_SHA256}, found {digest})."
        )

    document: dict[str, Any] = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    schemas = document["components"]["schemas"]
    evidence_references = schemas["EvidenceReferences"]
    evidence_property = schemas["ClaimEvidenceInput"]["properties"]["evidence_refs"]

    expected = [
        {"$ref": "#/components/schemas/EvidenceReferences"},
        {"minItems": 1},
    ]
    if evidence_property.get("allOf") != expected:
        raise RuntimeError(
            "The reviewed ClaimEvidenceInput normalization no longer matches the contract."
        )

    normalized = copy.deepcopy(evidence_references)
    normalized["minItems"] = 1
    schemas["ClaimEvidenceInput"]["properties"]["evidence_refs"] = normalized

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        yaml.safe_dump(document, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare the reviewed, generator-compatible OpenAPI document."
    )
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    prepare(args.target)


if __name__ == "__main__":
    main()
