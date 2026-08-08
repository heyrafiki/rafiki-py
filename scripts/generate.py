from __future__ import annotations

import importlib.metadata
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from prepare_contract import EXPECTED_SOURCE_SHA256, prepare

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / ".build"
GENERATOR_INPUT = BUILD / "openapi.generator.yaml"
GENERATED = BUILD / "generated"
PACKAGE = ROOT / "src" / "heyrafiki"
GENERATOR_VERSION = "0.29.0"
GENERATED_DIRECTORIES = ("api", "models")
GENERATED_FILES = ("client.py", "errors.py", "types.py")


def snake_case(value: str) -> str:
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value).lower()


def operation_ids(document: dict[str, Any]) -> set[str]:
    operations: set[str] = set()
    for path_item in document["paths"].values():
        for method in ("get", "post", "put", "patch", "delete"):
            if operation := path_item.get(method):
                operations.add(operation["operationId"])
    return operations


def write_package_init() -> None:
    (PACKAGE / "__init__.py").write_text(
        '"""Typed Python client for the Heyrafiki API."""\n\n'
        "from .client import AuthenticatedClient, Client\n"
        "from .retry import RetryPolicy, create_client\n"
        "from .runtime import HeyrafikiApiError, unwrap\n\n"
        '__version__ = "0.1.0b1"\n\n'
        "__all__ = (\n"
        '    "AuthenticatedClient",\n'
        '    "Client",\n'
        '    "HeyrafikiApiError",\n'
        '    "RetryPolicy",\n'
        '    "create_client",\n'
        '    "unwrap",\n'
        ")\n",
        encoding="utf-8",
    )


def normalize_generated_copy() -> None:
    """Apply public-copy rules to generated comments without changing behavior."""
    for path in PACKAGE.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        normalized = source.replace("—", "; ").replace("–", "-")
        if normalized != source:
            path.write_text(normalized, encoding="utf-8")


def main() -> None:
    installed = importlib.metadata.version("openapi-python-client")
    if installed != GENERATOR_VERSION:
        raise RuntimeError(f"Use openapi-python-client {GENERATOR_VERSION}; found {installed}.")

    if BUILD.exists():
        shutil.rmtree(BUILD)
    prepare(GENERATOR_INPUT)

    subprocess.run(
        [
            sys.executable,
            "-m",
            "openapi_python_client",
            "generate",
            "--path",
            str(GENERATOR_INPUT),
            "--config",
            str(ROOT / "openapi-python-client.yaml"),
            "--meta",
            "none",
            "--output-path",
            str(GENERATED),
            "--fail-on-warning",
        ],
        cwd=ROOT,
        check=True,
    )

    document: dict[str, Any] = yaml.safe_load(GENERATOR_INPUT.read_text(encoding="utf-8"))
    expected_modules = {snake_case(item) for item in operation_ids(document)}
    actual_modules = {path.stem for path in (GENERATED / "api" / "default").glob("*.py")}
    actual_modules.discard("__init__")
    if expected_modules != actual_modules:
        missing = sorted(expected_modules - actual_modules)
        extra = sorted(actual_modules - expected_modules)
        raise RuntimeError(
            f"Generated operation coverage mismatch: missing={missing}, extra={extra}"
        )

    PACKAGE.mkdir(parents=True, exist_ok=True)
    for name in GENERATED_DIRECTORIES:
        destination = PACKAGE / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(GENERATED / name, destination)
    for name in GENERATED_FILES:
        shutil.copy2(GENERATED / name, PACKAGE / name)
    write_package_init()
    normalize_generated_copy()

    (PACKAGE / "py.typed").touch()
    provenance = PACKAGE / "_generation.py"
    provenance.write_text(
        "# Generated provenance. Do not edit by hand.\n"
        f'OPENAPI_SHA256 = "{EXPECTED_SOURCE_SHA256}"\n'
        f'GENERATOR = "openapi-python-client=={GENERATOR_VERSION}"\n',
        encoding="utf-8",
    )

    subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--fix", "src/heyrafiki"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "ruff", "format", "src/heyrafiki"],
        cwd=ROOT,
        check=True,
    )


if __name__ == "__main__":
    main()
