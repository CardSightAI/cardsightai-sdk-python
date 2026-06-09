from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.set_identifiable_response import SetIdentifiableResponse
from ...types import Response


def _get_kwargs(
    set_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/identify/check/set/{set_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SetIdentifiableResponse]]:
    if response.status_code == 200:
        response_200 = SetIdentifiableResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SetIdentifiableResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SetIdentifiableResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    set_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SetIdentifiableResponse]]:
    """Check if a set is identifiable (free)

     Given a set unique ID, reports whether that set is identifiable by the system. Returns 404 if no set
    exists with the provided ID. Use this to confirm support for a specific set before submitting an
    identify request. This is a free endpoint — calls do not count toward your billed API usage.

    Args:
        set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetIdentifiableResponse]]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    set_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SetIdentifiableResponse]]:
    """Check if a set is identifiable (free)

     Given a set unique ID, reports whether that set is identifiable by the system. Returns 404 if no set
    exists with the provided ID. Use this to confirm support for a specific set before submitting an
    identify request. This is a free endpoint — calls do not count toward your billed API usage.

    Args:
        set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetIdentifiableResponse]
    """

    return sync_detailed(
        set_id=set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    set_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SetIdentifiableResponse]]:
    """Check if a set is identifiable (free)

     Given a set unique ID, reports whether that set is identifiable by the system. Returns 404 if no set
    exists with the provided ID. Use this to confirm support for a specific set before submitting an
    identify request. This is a free endpoint — calls do not count toward your billed API usage.

    Args:
        set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetIdentifiableResponse]]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    set_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SetIdentifiableResponse]]:
    """Check if a set is identifiable (free)

     Given a set unique ID, reports whether that set is identifiable by the system. Returns 404 if no set
    exists with the provided ID. Use this to confirm support for a specific set before submitting an
    identify request. This is a free endpoint — calls do not count toward your billed API usage.

    Args:
        set_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetIdentifiableResponse]
    """

    return (
        await asyncio_detailed(
            set_id=set_id,
            client=client,
        )
    ).parsed
