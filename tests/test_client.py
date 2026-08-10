from __future__ import annotations

import datetime as dt
import json
from collections.abc import Iterator
from http import HTTPStatus
from pathlib import Path
from typing import cast

import httpx
import pytest

from heyrafiki import HeyrafikiApiError, RetryPolicy, create_client, unwrap
from heyrafiki.api.default import create_booking, create_webhook_endpoint, list_practitioners
from heyrafiki.models import BookingInput, WebhookEndpointInput
from heyrafiki.models.practitioner_list import PractitionerList
from heyrafiki.retry import AsyncRetryTransport, RetryTransport, _delay, _retry_after
from heyrafiki.types import Response

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict[str, object]:
    return cast(dict[str, object], json.loads((FIXTURES / name).read_text(encoding="utf-8")))


@pytest.fixture
def practitioner_list() -> dict[str, object]:
    return load_fixture("practitioner-list.json")


@pytest.fixture
def booking() -> dict[str, object]:
    payload = load_fixture("booking-list.json")
    data = payload["data"]
    assert isinstance(data, list)
    item = data[0]
    assert isinstance(item, dict)
    return cast(dict[str, object], item)


def test_authenticates_and_parses_a_typed_response(
    practitioner_list: dict[str, object],
) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=practitioner_list)

    client = create_client(
        "test_api_key",
        base_url="https://sandbox.example/v1/",
        sync_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=1),
    )
    with client:
        result = unwrap(list_practitioners.sync_detailed(client=client, limit=5))

    assert isinstance(result, PractitionerList)
    assert result.data[0].id == "prc_2481"
    assert requests[0].url == "https://sandbox.example/v1/practitioners?limit=5"
    assert requests[0].headers["authorization"] == "Bearer test_api_key"
    assert requests[0].headers["user-agent"] == "rafiki-py/0.1.0b1"


def test_raises_the_shared_error_with_request_id() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            403,
            headers={"x-request-id": "req_123"},
            json={
                "error": {
                    "code": "permission_denied",
                    "message": "This key does not have access to this resource.",
                    "docs": "https://docs.heyrafiki.space/errors",
                }
            },
        )

    client = create_client(
        "test_api_key",
        sync_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=1),
    )
    with client, pytest.raises(HeyrafikiApiError) as caught:
        unwrap(list_practitioners.sync_detailed(client=client))

    assert caught.value.status_code == 403
    assert caught.value.code == "permission_denied"
    assert caught.value.request_id == "req_123"
    assert caught.value.docs == "https://docs.heyrafiki.space/errors"


def test_retries_a_safe_read_after_retry_after(
    practitioner_list: dict[str, object],
) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                503,
                headers={"retry-after": "0"},
                json={
                    "error": {
                        "code": "temporarily_unavailable",
                        "message": "Try again.",
                        "docs": "https://docs.heyrafiki.space/errors",
                    }
                },
            )
        return httpx.Response(200, json=practitioner_list)

    client = create_client(
        "test_api_key",
        sync_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=2, backoff_factor=0),
    )
    with client:
        result = unwrap(list_practitioners.sync_detailed(client=client))

    assert isinstance(result, PractitionerList)
    assert attempts == 2


def test_retries_a_write_only_with_an_idempotency_key(booking: dict[str, object]) -> None:
    attempts = 0
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        requests.append(request)
        if attempts == 1:
            return httpx.Response(
                503,
                headers={"retry-after": "0"},
                json={
                    "error": {
                        "code": "temporarily_unavailable",
                        "message": "Try again.",
                        "docs": "https://docs.heyrafiki.space/errors",
                    }
                },
            )
        return httpx.Response(201, json=booking)

    body = BookingInput(
        practitioner_id="prc_2481",
        starts_at=dt.datetime(2026, 8, 12, 7, tzinfo=dt.timezone.utc),
        ends_at=dt.datetime(2026, 8, 12, 8, tzinfo=dt.timezone.utc),
        format_="online",
        payment_source="covered",
    )
    client = create_client(
        "test_api_key",
        sync_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=2, backoff_factor=0),
    )
    with client:
        created = unwrap(
            create_booking.sync_detailed(
                client=client,
                body=body,
                idempotency_key="booking-demo-001",
            )
        )

    assert created.id == "bkg_demo_jubilee_001"
    assert attempts == 2
    assert all(item.headers["idempotency-key"] == "booking-demo-001" for item in requests)


def test_does_not_retry_an_unkeyed_write() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(
            503,
            json={
                "error": {
                    "code": "temporarily_unavailable",
                    "message": "Try again.",
                    "docs": "https://docs.heyrafiki.space/errors",
                }
            },
        )

    client = create_client(
        "test_api_key",
        sync_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=3, backoff_factor=0),
    )
    body = WebhookEndpointInput(
        url="https://hooks.example.com/heyrafiki",
        events=["sandbox.ping"],
    )
    with client, pytest.raises(HeyrafikiApiError):
        unwrap(create_webhook_endpoint.sync_detailed(client=client, body=body))

    assert attempts == 1


def test_rejects_invalid_client_and_retry_configuration() -> None:
    with pytest.raises(ValueError, match="api_key"):
        create_client(" ")
    with pytest.raises(ValueError, match="max_attempts"):
        RetryPolicy(max_attempts=0)
    with pytest.raises(ValueError, match="backoff_factor"):
        RetryPolicy(backoff_factor=-1)
    with pytest.raises(ValueError, match="max_delay"):
        RetryPolicy(max_delay=-1)


def test_retry_after_and_fallback_delay(monkeypatch: pytest.MonkeyPatch) -> None:
    response = httpx.Response(503)
    assert _retry_after(response) is None

    invalid = httpx.Response(503, headers={"retry-after": "not-a-date"})
    assert _retry_after(invalid) is None

    now = dt.datetime(2026, 8, 9, 12, tzinfo=dt.timezone.utc)
    dated = httpx.Response(503, headers={"retry-after": "Sun, 09 Aug 2026 12:00:05 GMT"})
    assert _retry_after(dated, now=now) == 5.0

    monkeypatch.setattr("heyrafiki.retry.random.uniform", lambda start, end: end)
    assert _delay(RetryPolicy(backoff_factor=0.5, max_delay=3), 3, response) == 2.0


def test_retries_a_transient_network_error() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ConnectError("connection failed", request=request)
        return httpx.Response(200, json={"ok": True})

    transport = RetryTransport(
        policy=RetryPolicy(max_attempts=2, backoff_factor=0),
        transport=httpx.MockTransport(handler),
    )
    with httpx.Client(transport=transport) as client:
        assert client.get("https://example.com").json() == {"ok": True}
    assert attempts == 2


def test_does_not_retry_an_unkeyed_network_error() -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.ReadTimeout("timed out", request=request)

    transport = RetryTransport(
        policy=RetryPolicy(max_attempts=3, backoff_factor=0),
        transport=httpx.MockTransport(handler),
    )
    with httpx.Client(transport=transport) as client, pytest.raises(httpx.ReadTimeout):
        client.post("https://example.com", json={"synthetic": True})
    assert attempts == 1


def test_unwrap_rejects_missing_error_and_success_bodies() -> None:
    with pytest.raises(HeyrafikiApiError) as request_failed:
        unwrap(
            Response[object](
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                content=b"",
                headers={},
                parsed=None,
            )
        )
    assert request_failed.value.code == "request_failed"

    with pytest.raises(HeyrafikiApiError) as invalid_response:
        unwrap(
            Response[object](
                status_code=HTTPStatus.OK,
                content=b"",
                headers={},
                parsed=None,
            )
        )
    assert invalid_response.value.code == "invalid_response"


@pytest.mark.asyncio
async def test_async_client_retries_safe_reads(
    practitioner_list: dict[str, object],
) -> None:
    responses: Iterator[int] = iter((503, 200))

    async def handler(request: httpx.Request) -> httpx.Response:
        status = next(responses)
        if status == 503:
            return httpx.Response(
                status,
                headers={"retry-after": "0"},
                json={
                    "error": {
                        "code": "temporarily_unavailable",
                        "message": "Try again.",
                        "docs": "https://docs.heyrafiki.space/errors",
                    }
                },
            )
        return httpx.Response(status, json=practitioner_list)

    client = create_client(
        "test_api_key",
        async_transport=httpx.MockTransport(handler),
        retry_policy=RetryPolicy(max_attempts=2, backoff_factor=0),
    )
    async with client:
        response = await list_practitioners.asyncio_detailed(client=client)
        result = unwrap(response)

    assert isinstance(result, PractitionerList)


@pytest.mark.asyncio
async def test_async_transport_retries_a_network_error() -> None:
    attempts = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ConnectError("connection failed", request=request)
        return httpx.Response(200, json={"ok": True})

    async def no_sleep(delay: float) -> None:
        assert delay == 0

    transport = AsyncRetryTransport(
        policy=RetryPolicy(max_attempts=2, backoff_factor=0),
        transport=httpx.MockTransport(handler),
        sleep=no_sleep,
    )
    async with httpx.AsyncClient(transport=transport) as client:
        assert (await client.get("https://example.com")).json() == {"ok": True}
    assert attempts == 2


@pytest.mark.asyncio
async def test_async_transport_does_not_retry_an_unkeyed_timeout() -> None:
    attempts = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.ReadTimeout("timed out", request=request)

    transport = AsyncRetryTransport(
        policy=RetryPolicy(max_attempts=3, backoff_factor=0),
        transport=httpx.MockTransport(handler),
    )
    async with httpx.AsyncClient(transport=transport) as client:
        with pytest.raises(httpx.ReadTimeout):
            await client.post("https://example.com", json={"synthetic": True})
    assert attempts == 1
