import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.claim_valuation import ClaimValuation
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response


def _get_kwargs(
    claim_id: str,
    *,
    valuation_at: datetime.datetime,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_valuation_at = valuation_at.isoformat()
    params["valuation_at"] = json_valuation_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/claims/{claim_id}/valuation".format(
            claim_id=quote(str(claim_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClaimValuation | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = ClaimValuation.from_dict(response.json())

        return response_200

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
) -> Response[ClaimValuation | ErrorEnvelope]:
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
    valuation_at: datetime.datetime,
) -> Response[ClaimValuation | ErrorEnvelope]:
    """Reproduce a Claim valuation

     Returns the synthetic Claim state and financial amounts known at an explicit cutoff. Both business
    time and knowledge time must fall on or before `valuation_at`. Requires `claims:read`.

    Args:
        claim_id (str):
        valuation_at (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClaimValuation | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        claim_id=claim_id,
        valuation_at=valuation_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    valuation_at: datetime.datetime,
) -> ClaimValuation | ErrorEnvelope | None:
    """Reproduce a Claim valuation

     Returns the synthetic Claim state and financial amounts known at an explicit cutoff. Both business
    time and knowledge time must fall on or before `valuation_at`. Requires `claims:read`.

    Args:
        claim_id (str):
        valuation_at (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClaimValuation | ErrorEnvelope
    """

    return sync_detailed(
        claim_id=claim_id,
        client=client,
        valuation_at=valuation_at,
    ).parsed


async def asyncio_detailed(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    valuation_at: datetime.datetime,
) -> Response[ClaimValuation | ErrorEnvelope]:
    """Reproduce a Claim valuation

     Returns the synthetic Claim state and financial amounts known at an explicit cutoff. Both business
    time and knowledge time must fall on or before `valuation_at`. Requires `claims:read`.

    Args:
        claim_id (str):
        valuation_at (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClaimValuation | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        claim_id=claim_id,
        valuation_at=valuation_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    claim_id: str,
    *,
    client: AuthenticatedClient | Client,
    valuation_at: datetime.datetime,
) -> ClaimValuation | ErrorEnvelope | None:
    """Reproduce a Claim valuation

     Returns the synthetic Claim state and financial amounts known at an explicit cutoff. Both business
    time and knowledge time must fall on or before `valuation_at`. Requires `claims:read`.

    Args:
        claim_id (str):
        valuation_at (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClaimValuation | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            claim_id=claim_id,
            client=client,
            valuation_at=valuation_at,
        )
    ).parsed
