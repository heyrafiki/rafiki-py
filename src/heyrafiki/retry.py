from __future__ import annotations

import asyncio
import email.utils
import random
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import datetime, timezone

import httpx

from .client import AuthenticatedClient

DEFAULT_BASE_URL = "https://api.heyrafiki.space/v1"
RETRYABLE_STATUS_CODES = frozenset({429, 503})
SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    """Bounded retry policy for safe reads and idempotent writes."""

    max_attempts: int = 3
    backoff_factor: float = 0.25
    max_delay: float = 8.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least 1.")
        if self.backoff_factor < 0:
            raise ValueError("backoff_factor cannot be negative.")
        if self.max_delay < 0:
            raise ValueError("max_delay cannot be negative.")


def _eligible(request: httpx.Request) -> bool:
    return request.method.upper() in SAFE_METHODS or "idempotency-key" in request.headers


def _retry_after(response: httpx.Response, *, now: datetime | None = None) -> float | None:
    value = response.headers.get("retry-after")
    if value is None:
        return None
    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        current = now or datetime.now(timezone.utc)
        return max(0.0, (parsed - current).total_seconds())


def _delay(policy: RetryPolicy, attempt: int, response: httpx.Response | None) -> float:
    if response is not None and (retry_after := _retry_after(response)) is not None:
        return min(retry_after, policy.max_delay)
    ceiling = min(policy.backoff_factor * (2 ** (attempt - 1)), policy.max_delay)
    return random.uniform(0.0, ceiling)


class RetryTransport(httpx.BaseTransport):
    """Sync transport that retries safe requests and keyed writes."""

    def __init__(
        self,
        *,
        policy: RetryPolicy,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._policy = policy
        self._transport = transport or httpx.HTTPTransport()
        self._sleep = sleep

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.read()
        eligible = _eligible(request)
        for attempt in range(1, self._policy.max_attempts + 1):
            response: httpx.Response | None = None
            try:
                response = self._transport.handle_request(request)
            except (httpx.NetworkError, httpx.TimeoutException):
                if not eligible or attempt == self._policy.max_attempts:
                    raise
            else:
                if (
                    not eligible
                    or response.status_code not in RETRYABLE_STATUS_CODES
                    or attempt == self._policy.max_attempts
                ):
                    return response
                response.close()
            self._sleep(_delay(self._policy, attempt, response))
        raise RuntimeError("Retry loop exhausted without returning or raising.")  # pragma: no cover

    def close(self) -> None:
        self._transport.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    """Async transport that retries safe requests and keyed writes."""

    def __init__(
        self,
        *,
        policy: RetryPolicy,
        transport: httpx.AsyncBaseTransport | None = None,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self._policy = policy
        self._transport = transport or httpx.AsyncHTTPTransport()
        self._sleep = sleep

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        await request.aread()
        eligible = _eligible(request)
        for attempt in range(1, self._policy.max_attempts + 1):
            response: httpx.Response | None = None
            try:
                response = await self._transport.handle_async_request(request)
            except (httpx.NetworkError, httpx.TimeoutException):
                if not eligible or attempt == self._policy.max_attempts:
                    raise
            else:
                if (
                    not eligible
                    or response.status_code not in RETRYABLE_STATUS_CODES
                    or attempt == self._policy.max_attempts
                ):
                    return response
                await response.aclose()
            delay = _delay(self._policy, attempt, response)
            await self._sleep(delay)
        raise RuntimeError("Retry loop exhausted without returning or raising.")  # pragma: no cover

    async def aclose(self) -> None:
        await self._transport.aclose()


def create_client(
    api_key: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    timeout: float = 30.0,
    retry_policy: RetryPolicy | None = None,
    sync_transport: httpx.BaseTransport | None = None,
    async_transport: httpx.AsyncBaseTransport | None = None,
) -> AuthenticatedClient:
    """Create an authenticated client with bounded retry behavior."""

    if not api_key.strip():
        raise ValueError("api_key is required.")
    normalized_base_url = base_url.rstrip("/")
    policy = retry_policy or RetryPolicy()
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_key}",
        "user-agent": "heyrafiki-python/0.1.0b1",
    }
    client = AuthenticatedClient(
        base_url=normalized_base_url,
        token=api_key,
        timeout=httpx.Timeout(timeout),
        raise_on_unexpected_status=True,
    )
    client.set_httpx_client(
        httpx.Client(
            base_url=normalized_base_url,
            headers=headers,
            timeout=timeout,
            transport=RetryTransport(policy=policy, transport=sync_transport),
        )
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(
            base_url=normalized_base_url,
            headers=headers,
            timeout=timeout,
            transport=AsyncRetryTransport(policy=policy, transport=async_transport),
        )
    )
    return client
