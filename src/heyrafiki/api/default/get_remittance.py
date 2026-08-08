from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.remittance import Remittance
from ...types import Response


def _get_kwargs(
    remittance_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/remittances/{remittance_id}".format(
            remittance_id=quote(str(remittance_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | Remittance | None:
    if response.status_code == 200:
        response_200 = Remittance.from_dict(response.json())

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
) -> Response[ErrorEnvelope | Remittance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    remittance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorEnvelope | Remittance]:
    """Retrieve a remittance

     Returns one project-scoped remittance. Requires `remittances:read`.

    Args:
        remittance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Remittance]
    """

    kwargs = _get_kwargs(
        remittance_id=remittance_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    remittance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorEnvelope | Remittance | None:
    """Retrieve a remittance

     Returns one project-scoped remittance. Requires `remittances:read`.

    Args:
        remittance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Remittance
    """

    return sync_detailed(
        remittance_id=remittance_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    remittance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorEnvelope | Remittance]:
    """Retrieve a remittance

     Returns one project-scoped remittance. Requires `remittances:read`.

    Args:
        remittance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Remittance]
    """

    kwargs = _get_kwargs(
        remittance_id=remittance_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    remittance_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorEnvelope | Remittance | None:
    """Retrieve a remittance

     Returns one project-scoped remittance. Requires `remittances:read`.

    Args:
        remittance_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Remittance
    """

    return (
        await asyncio_detailed(
            remittance_id=remittance_id,
            client=client,
        )
    ).parsed
