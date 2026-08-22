# Heyrafiki Python SDK

Typed Python client for the Heyrafiki API.

## Where this fits

This SDK is the typed Python entrypoint to Heyrafiki's versioned REST contract.
It helps applications participate in governed Mental Healthcare workflows while
authorization, Consent, clinical authority and financial decisions remain
server-owned.

## Install from source

Python 3.10 or newer is required. Keep API keys on the server.

```bash
git clone https://github.com/heyrafiki/rafiki-py.git
cd rafiki-py
python -m pip install -e .
```

The client connects to Sandbox projects with typed sync and async operations,
caller-owned idempotency keys, bounded retries and the shared API error
envelope.

## First request

```python
import os

from heyrafiki import create_client, unwrap
from heyrafiki.api.default import list_practitioners


with create_client(os.environ["HEYRAFIKI_API_KEY"]) as client:
    response = list_practitioners.sync_detailed(client=client, limit=5)
    practitioners = unwrap(response)

for practitioner in practitioners.data:
    print(practitioner.name)
```

Sandbox keys return synthetic data.

## Covered Care

Writes that require idempotency expose `idempotency_key` as a required argument.

```python
import datetime as dt
import os
import uuid

from heyrafiki import create_client, unwrap
from heyrafiki.api.default import create_booking
from heyrafiki.models import BookingInput


starts_at = dt.datetime.now(dt.timezone.utc) + dt.timedelta(days=1)
ends_at = starts_at + dt.timedelta(hours=1)

booking = BookingInput(
    practitioner_id="prc_2481",
    starts_at=starts_at,
    ends_at=ends_at,
    format_="online",
    payment_source="covered",
)

with create_client(os.environ["HEYRAFIKI_API_KEY"]) as client:
    response = create_booking.sync_detailed(
        client=client,
        body=booking,
        idempotency_key=str(uuid.uuid4()),
    )
    created = unwrap(response)
```

Amounts use the currency's minor unit.

## Errors and retries

`unwrap` raises `HeyrafikiApiError` for documented API errors and retains the request ID.

```python
from heyrafiki import HeyrafikiApiError

try:
    created = unwrap(response)
except HeyrafikiApiError as error:
    print(error.status_code, error.code, error.request_id)
```

The default retry policy is bounded to three attempts. It retries 429 and 503 responses for safe reads and for writes carrying an `Idempotency-Key`. Unkeyed writes are never retried automatically.

## Sync and async

Every generated operation provides `sync`, `sync_detailed`, `asyncio` and `asyncio_detailed` functions. Use the detailed variants with `unwrap` when you want consistent error handling.

## Contract

The client is generated from the public [OpenAPI 3.1 contract](https://github.com/heyrafiki/contract). [`GENERATION.md`](./GENERATION.md) records the contract revision, SHA-256 digest, generator version and the reviewed compatibility transform.

## Develop

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
mypy
pytest
python -m build
python -m twine check dist/*
```

Contract generation requires Python 3.11 or newer. See [`GENERATION.md`](./GENERATION.md).

## Resources

- [Documentation](https://docs.heyrafiki.space)
- [API contract](https://github.com/heyrafiki/contract)
- [Open insurance assurance benchmark](https://github.com/heyrafiki/proving-ground)
- [SDK roadmap](https://docs.heyrafiki.space/sdks)
- [Security](https://github.com/heyrafiki/.github/security/policy)

## License

Licensed under the [Apache License 2.0](./LICENSE).
