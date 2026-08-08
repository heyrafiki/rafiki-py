from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.eligibility_check import EligibilityCheck
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def _get_kwargs(
    eligibility_check_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/eligibility_checks/{eligibility_check_id}".format(
            eligibility_check_id=quote(str(eligibility_check_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EligibilityCheck | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = EligibilityCheck.from_dict(response.json())

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
) -> Response[EligibilityCheck | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    eligibility_check_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EligibilityCheck | ErrorEnvelope]:
    """Retrieve an eligibility check

     Returns one tenant-scoped synthetic eligibility decision. Requires `benefits:read`.

    Args:
        eligibility_check_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibilityCheck | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        eligibility_check_id=eligibility_check_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    eligibility_check_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EligibilityCheck | ErrorEnvelope | None:
    """Retrieve an eligibility check

     Returns one tenant-scoped synthetic eligibility decision. Requires `benefits:read`.

    Args:
        eligibility_check_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibilityCheck | ErrorEnvelope
    """

    return sync_detailed(
        eligibility_check_id=eligibility_check_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    eligibility_check_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EligibilityCheck | ErrorEnvelope]:
    """Retrieve an eligibility check

     Returns one tenant-scoped synthetic eligibility decision. Requires `benefits:read`.

    Args:
        eligibility_check_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibilityCheck | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        eligibility_check_id=eligibility_check_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    eligibility_check_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EligibilityCheck | ErrorEnvelope | None:
    """Retrieve an eligibility check

     Returns one tenant-scoped synthetic eligibility decision. Requires `benefits:read`.

    Args:
        eligibility_check_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibilityCheck | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            eligibility_check_id=eligibility_check_id,
            client=client,
        )
    ).parsed
