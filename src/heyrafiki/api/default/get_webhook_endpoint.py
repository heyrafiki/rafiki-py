from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.webhook_endpoint import WebhookEndpoint
from ...types import Response


def _get_kwargs(
    webhook_endpoint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook_endpoints/{webhook_endpoint_id}".format(
            webhook_endpoint_id=quote(str(webhook_endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | WebhookEndpoint | None:
    if response.status_code == 200:
        response_200 = WebhookEndpoint.from_dict(response.json())

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
) -> Response[ErrorEnvelope | WebhookEndpoint]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorEnvelope | WebhookEndpoint]:
    """Retrieve a Webhook endpoint

     Returns one Webhook endpoint. Requires `webhooks:read`.

    Args:
        webhook_endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | WebhookEndpoint]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorEnvelope | WebhookEndpoint | None:
    """Retrieve a Webhook endpoint

     Returns one Webhook endpoint. Requires `webhooks:read`.

    Args:
        webhook_endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | WebhookEndpoint
    """

    return sync_detailed(
        webhook_endpoint_id=webhook_endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorEnvelope | WebhookEndpoint]:
    """Retrieve a Webhook endpoint

     Returns one Webhook endpoint. Requires `webhooks:read`.

    Args:
        webhook_endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | WebhookEndpoint]
    """

    kwargs = _get_kwargs(
        webhook_endpoint_id=webhook_endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorEnvelope | WebhookEndpoint | None:
    """Retrieve a Webhook endpoint

     Returns one Webhook endpoint. Requires `webhooks:read`.

    Args:
        webhook_endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | WebhookEndpoint
    """

    return (
        await asyncio_detailed(
            webhook_endpoint_id=webhook_endpoint_id,
            client=client,
        )
    ).parsed
