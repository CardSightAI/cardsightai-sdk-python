from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_release_cards_order import GetReleaseCardsOrder
from ...models.get_release_cards_sort import GetReleaseCardsSort
from ...models.paginated_cards_response import PaginatedCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    set_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetReleaseCardsSort] = UNSET,
    order: Union[Unset, GetReleaseCardsOrder] = GetReleaseCardsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["setId"] = set_id

    params["name"] = name

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/catalog/releases/{id}/cards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedCardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedCardsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    set_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetReleaseCardsSort] = UNSET,
    order: Union[Unset, GetReleaseCardsOrder] = GetReleaseCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List all cards in a release

     Retrieve a paginated list of all base cards (not parallels) within a specific release across all its
    sets. Use the optional setId parameter to filter to a specific set within the release. Cards can be
    searched by player name and sorted by card number or name. This endpoint is ideal for building
    complete checklists, player searches within a release, or browsing all cards in a product.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        set_id (Union[Unset, str]):
        name (Union[Unset, str]):
        sort (Union[Unset, GetReleaseCardsSort]):
        order (Union[Unset, GetReleaseCardsOrder]):  Default: GetReleaseCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCardsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        take=take,
        skip=skip,
        set_id=set_id,
        name=name,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    set_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetReleaseCardsSort] = UNSET,
    order: Union[Unset, GetReleaseCardsOrder] = GetReleaseCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List all cards in a release

     Retrieve a paginated list of all base cards (not parallels) within a specific release across all its
    sets. Use the optional setId parameter to filter to a specific set within the release. Cards can be
    searched by player name and sorted by card number or name. This endpoint is ideal for building
    complete checklists, player searches within a release, or browsing all cards in a product.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        set_id (Union[Unset, str]):
        name (Union[Unset, str]):
        sort (Union[Unset, GetReleaseCardsSort]):
        order (Union[Unset, GetReleaseCardsOrder]):  Default: GetReleaseCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCardsResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        take=take,
        skip=skip,
        set_id=set_id,
        name=name,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    set_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetReleaseCardsSort] = UNSET,
    order: Union[Unset, GetReleaseCardsOrder] = GetReleaseCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List all cards in a release

     Retrieve a paginated list of all base cards (not parallels) within a specific release across all its
    sets. Use the optional setId parameter to filter to a specific set within the release. Cards can be
    searched by player name and sorted by card number or name. This endpoint is ideal for building
    complete checklists, player searches within a release, or browsing all cards in a product.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        set_id (Union[Unset, str]):
        name (Union[Unset, str]):
        sort (Union[Unset, GetReleaseCardsSort]):
        order (Union[Unset, GetReleaseCardsOrder]):  Default: GetReleaseCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCardsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        take=take,
        skip=skip,
        set_id=set_id,
        name=name,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    set_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetReleaseCardsSort] = UNSET,
    order: Union[Unset, GetReleaseCardsOrder] = GetReleaseCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List all cards in a release

     Retrieve a paginated list of all base cards (not parallels) within a specific release across all its
    sets. Use the optional setId parameter to filter to a specific set within the release. Cards can be
    searched by player name and sorted by card number or name. This endpoint is ideal for building
    complete checklists, player searches within a release, or browsing all cards in a product.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        set_id (Union[Unset, str]):
        name (Union[Unset, str]):
        sort (Union[Unset, GetReleaseCardsSort]):
        order (Union[Unset, GetReleaseCardsOrder]):  Default: GetReleaseCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCardsResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            take=take,
            skip=skip,
            set_id=set_id,
            name=name,
            sort=sort,
            order=order,
        )
    ).parsed
