from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.claim import Claim
from ...models.claim_information_request_input import ClaimInformationRequestInput
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def _get_kwargs(
    claim_id: str,
    *,
    body: ClaimInformationRequestInput,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/claims/{claim_id}/information_requests".format(
            claim_id=quote(str(claim_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Claim | ErrorEnvelope | None:
    if response.status_code == 201:
        response_201 = Claim.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

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
) -> Response[Claim | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimInformationRequestInput,
    idempotency_key: str,
) -> Response[Claim | ErrorEnvelope]:
    """Request Claim information

     Records a payer request for supporting evidence. Requires `claims:adjudicate`.

    Args:
        claim_id (str):
        idempotency_key (str):
        body (ClaimInformationRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Claim | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        claim_id=claim_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimInformationRequestInput,
    idempotency_key: str,
) -> Claim | ErrorEnvelope | None:
    """Request Claim information

     Records a payer request for supporting evidence. Requires `claims:adjudicate`.

    Args:
        claim_id (str):
        idempotency_key (str):
        body (ClaimInformationRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Claim | ErrorEnvelope
    """

    return sync_detailed(
        claim_id=claim_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimInformationRequestInput,
    idempotency_key: str,
) -> Response[Claim | ErrorEnvelope]:
    """Request Claim information

     Records a payer request for supporting evidence. Requires `claims:adjudicate`.

    Args:
        claim_id (str):
        idempotency_key (str):
        body (ClaimInformationRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Claim | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        claim_id=claim_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ClaimInformationRequestInput,
    idempotency_key: str,
) -> Claim | ErrorEnvelope | None:
    """Request Claim information

     Records a payer request for supporting evidence. Requires `claims:adjudicate`.

    Args:
        claim_id (str):
        idempotency_key (str):
        body (ClaimInformationRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Claim | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            claim_id=claim_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
