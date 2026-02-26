from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.paginated_list_cards_response import PaginatedListCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    list_id: str,
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
        "url": f"/v1/lists/{list_id}/cards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedListCardsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedListCardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedListCardsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedListCardsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedListCardsResponse]]:
    """Get all cards in a list

     Get all cards in a specific list with pagination

    Args:
        list_id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedListCardsResponse]]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        take=take,
        skip=skip,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedListCardsResponse]]:
    """Get all cards in a list

     Get all cards in a specific list with pagination

    Args:
        list_id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedListCardsResponse]
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        take=take,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedListCardsResponse]]:
    """Get all cards in a list

     Get all cards in a specific list with pagination

    Args:
        list_id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedListCardsResponse]]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        take=take,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedListCardsResponse]]:
    """Get all cards in a list

     Get all cards in a specific list with pagination

    Args:
        list_id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedListCardsResponse]
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            take=take,
            skip=skip,
        )
    ).parsed
