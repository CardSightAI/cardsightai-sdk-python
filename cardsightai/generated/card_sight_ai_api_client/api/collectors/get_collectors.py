from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.paginated_collectors_response import PaginatedCollectorsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collectors/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedCollectorsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedCollectorsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    """Get all collectors

     Get all collectors for the authenticated client with pagination

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCollectorsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    """Get all collectors

     Get all collectors for the authenticated client with pagination

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCollectorsResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    """Get all collectors

     Get all collectors for the authenticated client with pagination

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCollectorsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedCollectorsResponse]]:
    """Get all collectors

     Get all collectors for the authenticated client with pagination

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCollectorsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
        )
    ).parsed
