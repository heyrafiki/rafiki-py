from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.preauthorization import Preauthorization
from ...models.preauthorization_decision_input_type_0 import PreauthorizationDecisionInputType0
from ...models.preauthorization_decision_input_type_1 import PreauthorizationDecisionInputType1
from ...types import Response


def _get_kwargs(
    preauthorization_id: str,
    *,
    body: PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/preauthorizations/{preauthorization_id}/decisions".format(
            preauthorization_id=quote(str(preauthorization_id), safe=""),
        ),
    }

    if isinstance(body, PreauthorizationDecisionInputType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | Preauthorization | None:
    if response.status_code == 200:
        response_200 = Preauthorization.from_dict(response.json())

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
) -> Response[ErrorEnvelope | Preauthorization]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    preauthorization_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1,
    idempotency_key: str,
) -> Response[ErrorEnvelope | Preauthorization]:
    """Decide a pre-authorization

     Records the payer organization's decision and reserves the Benefit only when approved. Requires
    `benefits:decide`.

    Args:
        preauthorization_id (str):
        idempotency_key (str):
        body (PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Preauthorization]
    """

    kwargs = _get_kwargs(
        preauthorization_id=preauthorization_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    preauthorization_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1,
    idempotency_key: str,
) -> ErrorEnvelope | Preauthorization | None:
    """Decide a pre-authorization

     Records the payer organization's decision and reserves the Benefit only when approved. Requires
    `benefits:decide`.

    Args:
        preauthorization_id (str):
        idempotency_key (str):
        body (PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Preauthorization
    """

    return sync_detailed(
        preauthorization_id=preauthorization_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    preauthorization_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1,
    idempotency_key: str,
) -> Response[ErrorEnvelope | Preauthorization]:
    """Decide a pre-authorization

     Records the payer organization's decision and reserves the Benefit only when approved. Requires
    `benefits:decide`.

    Args:
        preauthorization_id (str):
        idempotency_key (str):
        body (PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Preauthorization]
    """

    kwargs = _get_kwargs(
        preauthorization_id=preauthorization_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    preauthorization_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1,
    idempotency_key: str,
) -> ErrorEnvelope | Preauthorization | None:
    """Decide a pre-authorization

     Records the payer organization's decision and reserves the Benefit only when approved. Requires
    `benefits:decide`.

    Args:
        preauthorization_id (str):
        idempotency_key (str):
        body (PreauthorizationDecisionInputType0 | PreauthorizationDecisionInputType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Preauthorization
    """

    return (
        await asyncio_detailed(
            preauthorization_id=preauthorization_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
