from __future__ import annotations

from typing import Any, TypeVar, cast

from .models.error_envelope import ErrorEnvelope
from .types import Response

T = TypeVar("T")


class HeyrafikiApiError(Exception):
    """A documented Heyrafiki API error."""

    def __init__(
        self,
        *,
        status_code: int,
        code: str,
        message: str,
        request_id: str | None = None,
        docs: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.code = code
        self.request_id = request_id
        self.docs = docs


def _header(response: Response[Any], name: str) -> str | None:
    expected = name.casefold()
    for key, value in response.headers.items():
        if key.casefold() == expected:
            return value
    return None


def unwrap(response: Response[T | ErrorEnvelope]) -> T:
    """Return a successful parsed body or raise a stable API error."""

    if response.status_code >= 400:
        parsed = response.parsed
        if isinstance(parsed, ErrorEnvelope):
            error = parsed.error
            raise HeyrafikiApiError(
                status_code=response.status_code,
                code=error.code,
                message=error.message,
                request_id=_header(response, "x-request-id"),
                docs=cast(str | None, error.docs),
            )
        raise HeyrafikiApiError(
            status_code=response.status_code,
            code="request_failed",
            message="The Heyrafiki API request failed.",
            request_id=_header(response, "x-request-id"),
        )

    if response.parsed is None:
        raise HeyrafikiApiError(
            status_code=response.status_code,
            code="invalid_response",
            message="The Heyrafiki API returned an invalid response.",
            request_id=_header(response, "x-request-id"),
        )

    return cast(T, response.parsed)
