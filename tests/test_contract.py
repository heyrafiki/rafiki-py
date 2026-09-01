from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from heyrafiki import __version__
from heyrafiki._generation import GENERATOR, OPENAPI_SHA256

ROOT = Path(__file__).parents[1]
CONTRACT = ROOT / "openapi" / "openapi.yaml"
API_MODULES = ROOT / "src" / "heyrafiki" / "api" / "default"


def snake_case(value: str) -> str:
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value).lower()


def operations(document: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for path_item in document["paths"].values():
        for method in ("get", "post", "put", "patch", "delete"):
            if operation := path_item.get(method):
                result.add(operation["operationId"])
    return result


def test_generated_operations_match_the_published_contract() -> None:
    document: dict[str, Any] = yaml.safe_load(CONTRACT.read_text(encoding="utf-8"))
    expected = {snake_case(value) for value in operations(document)}
    actual = {path.stem for path in API_MODULES.glob("*.py") if path.name != "__init__.py"}

    assert len(expected) == 31
    assert actual == expected
    assert "submit_claim_evidence" in actual
    assert "get_claim_valuation" in actual
    assert document["info"]["license"] == {
        "name": "Apache 2.0",
        "identifier": "Apache-2.0",
    }


def test_generation_provenance_matches_the_snapshot() -> None:
    canonical_contract = CONTRACT.read_text(encoding="utf-8").encode("utf-8")
    digest = hashlib.sha256(canonical_contract).hexdigest()

    assert digest == OPENAPI_SHA256
    assert GENERATOR == "openapi-python-client==0.29.0"
    assert __version__ == "0.1.0b2"
