from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.coverage_batch_input import CoverageBatchInput
from ...models.coverage_batch_result import CoverageBatchResult
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: CoverageBatchInput,
    idempotency_key: str,
    x_heyrafiki_artifact_reference: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    headers["X-Heyrafiki-Artifact-Reference"] = x_heyrafiki_artifact_reference

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/coverage_batches",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CoverageBatchResult | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = CoverageBatchResult.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CoverageBatchResult.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = ErrorEnvelope.from_dict(response.json())

        return response_413

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
) -> Response[CoverageBatchResult | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CoverageBatchInput,
    idempotency_key: str,
    x_heyrafiki_artifact_reference: str,
) -> Response[CoverageBatchResult | ErrorEnvelope]:
    """Record a Coverage batch

     Validates and records a versioned payer Coverage batch. Requires `coverages:write`.

    Args:
        idempotency_key (str):
        x_heyrafiki_artifact_reference (str):
        body (CoverageBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoverageBatchResult | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        x_heyrafiki_artifact_reference=x_heyrafiki_artifact_reference,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CoverageBatchInput,
    idempotency_key: str,
    x_heyrafiki_artifact_reference: str,
) -> CoverageBatchResult | ErrorEnvelope | None:
    """Record a Coverage batch

     Validates and records a versioned payer Coverage batch. Requires `coverages:write`.

    Args:
        idempotency_key (str):
        x_heyrafiki_artifact_reference (str):
        body (CoverageBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoverageBatchResult | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        x_heyrafiki_artifact_reference=x_heyrafiki_artifact_reference,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CoverageBatchInput,
    idempotency_key: str,
    x_heyrafiki_artifact_reference: str,
) -> Response[CoverageBatchResult | ErrorEnvelope]:
    """Record a Coverage batch

     Validates and records a versioned payer Coverage batch. Requires `coverages:write`.

    Args:
        idempotency_key (str):
        x_heyrafiki_artifact_reference (str):
        body (CoverageBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CoverageBatchResult | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
        x_heyrafiki_artifact_reference=x_heyrafiki_artifact_reference,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CoverageBatchInput,
    idempotency_key: str,
    x_heyrafiki_artifact_reference: str,
) -> CoverageBatchResult | ErrorEnvelope | None:
    """Record a Coverage batch

     Validates and records a versioned payer Coverage batch. Requires `coverages:write`.

    Args:
        idempotency_key (str):
        x_heyrafiki_artifact_reference (str):
        body (CoverageBatchInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CoverageBatchResult | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            x_heyrafiki_artifact_reference=x_heyrafiki_artifact_reference,
        )
    ).parsed
