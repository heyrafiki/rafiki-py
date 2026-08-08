from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.eligibility_check import EligibilityCheck
from ...models.eligibility_check_input import EligibilityCheckInput
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: EligibilityCheckInput,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/eligibility_checks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EligibilityCheck | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = EligibilityCheck.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = EligibilityCheck.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEnvelope.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ErrorEnvelope.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = ErrorEnvelope.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EligibilityCheck | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EligibilityCheckInput,
    idempotency_key: str,
) -> Response[EligibilityCheck | ErrorEnvelope]:
    """Check Benefit eligibility

     Evaluates synthetic Cover for a scheduled service. Requires `benefits:write`.

    Args:
        idempotency_key (str):
        body (EligibilityCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibilityCheck | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EligibilityCheckInput,
    idempotency_key: str,
) -> EligibilityCheck | ErrorEnvelope | None:
    """Check Benefit eligibility

     Evaluates synthetic Cover for a scheduled service. Requires `benefits:write`.

    Args:
        idempotency_key (str):
        body (EligibilityCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibilityCheck | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EligibilityCheckInput,
    idempotency_key: str,
) -> Response[EligibilityCheck | ErrorEnvelope]:
    """Check Benefit eligibility

     Evaluates synthetic Cover for a scheduled service. Requires `benefits:write`.

    Args:
        idempotency_key (str):
        body (EligibilityCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibilityCheck | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EligibilityCheckInput,
    idempotency_key: str,
) -> EligibilityCheck | ErrorEnvelope | None:
    """Check Benefit eligibility

     Evaluates synthetic Cover for a scheduled service. Requires `benefits:write`.

    Args:
        idempotency_key (str):
        body (EligibilityCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibilityCheck | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
