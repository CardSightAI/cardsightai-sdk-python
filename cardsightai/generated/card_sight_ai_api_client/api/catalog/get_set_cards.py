from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_set_cards_order import GetSetCardsOrder
from ...models.get_set_cards_sort import GetSetCardsSort
from ...models.paginated_cards_response import PaginatedCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetSetCardsSort] = UNSET,
    order: Union[Unset, GetSetCardsOrder] = GetSetCardsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["name"] = name

    params["number"] = number

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
        "url": f"/v1/catalog/sets/{id}/cards",
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
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetSetCardsSort] = UNSET,
    order: Union[Unset, GetSetCardsOrder] = GetSetCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List cards within a set

     Retrieve a paginated list of all base cards within a specific set. Cards can be filtered by player
    name or card number, and sorted by number or name. This endpoint returns only the base versions of
    cards, not their parallel variants. Use this for building set checklists, finding specific cards
    within a set, or displaying complete set contents. Each card includes its number, name, and basic
    information.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        sort (Union[Unset, GetSetCardsSort]):
        order (Union[Unset, GetSetCardsOrder]):  Default: GetSetCardsOrder.ASC.

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
        name=name,
        number=number,
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
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetSetCardsSort] = UNSET,
    order: Union[Unset, GetSetCardsOrder] = GetSetCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List cards within a set

     Retrieve a paginated list of all base cards within a specific set. Cards can be filtered by player
    name or card number, and sorted by number or name. This endpoint returns only the base versions of
    cards, not their parallel variants. Use this for building set checklists, finding specific cards
    within a set, or displaying complete set contents. Each card includes its number, name, and basic
    information.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        sort (Union[Unset, GetSetCardsSort]):
        order (Union[Unset, GetSetCardsOrder]):  Default: GetSetCardsOrder.ASC.

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
        name=name,
        number=number,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetSetCardsSort] = UNSET,
    order: Union[Unset, GetSetCardsOrder] = GetSetCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List cards within a set

     Retrieve a paginated list of all base cards within a specific set. Cards can be filtered by player
    name or card number, and sorted by number or name. This endpoint returns only the base versions of
    cards, not their parallel variants. Use this for building set checklists, finding specific cards
    within a set, or displaying complete set contents. Each card includes its number, name, and basic
    information.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        sort (Union[Unset, GetSetCardsSort]):
        order (Union[Unset, GetSetCardsOrder]):  Default: GetSetCardsOrder.ASC.

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
        name=name,
        number=number,
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
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetSetCardsSort] = UNSET,
    order: Union[Unset, GetSetCardsOrder] = GetSetCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """List cards within a set

     Retrieve a paginated list of all base cards within a specific set. Cards can be filtered by player
    name or card number, and sorted by number or name. This endpoint returns only the base versions of
    cards, not their parallel variants. Use this for building set checklists, finding specific cards
    within a set, or displaying complete set contents. Each card includes its number, name, and basic
    information.

    Args:
        id (str):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        sort (Union[Unset, GetSetCardsSort]):
        order (Union[Unset, GetSetCardsOrder]):  Default: GetSetCardsOrder.ASC.

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
            name=name,
            number=number,
            sort=sort,
            order=order,
        )
    ).parsed
