from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_random_cards_order import GetRandomCardsOrder
from ...models.get_random_cards_sort import GetRandomCardsSort
from ...models.random_cards_response import RandomCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    set_id: Union[Unset, str] = UNSET,
    set_name: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    attribute_id: Union[Unset, str] = UNSET,
    attribute_short_name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetRandomCardsSort] = UNSET,
    order: Union[Unset, GetRandomCardsOrder] = GetRandomCardsOrder.ASC,
    count: Union[Unset, int] = 1,
    include_parallels: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["number"] = number

    params["releaseId"] = release_id

    params["releaseName"] = release_name

    params["year"] = year

    params["min_year"] = min_year

    params["max_year"] = max_year

    params["setId"] = set_id

    params["setName"] = set_name

    params["manufacturer"] = manufacturer

    params["attributeId"] = attribute_id

    params["attributeShortName"] = attribute_short_name

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["count"] = count

    params["includeParallels"] = include_parallels

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/cards/random",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, RandomCardsResponse]]:
    if response.status_code == 200:
        response_200 = RandomCardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RandomCardsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, RandomCardsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    set_id: Union[Unset, str] = UNSET,
    set_name: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    attribute_id: Union[Unset, str] = UNSET,
    attribute_short_name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetRandomCardsSort] = UNSET,
    order: Union[Unset, GetRandomCardsOrder] = GetRandomCardsOrder.ASC,
    count: Union[Unset, int] = 1,
    include_parallels: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, RandomCardsResponse]]:
    """Get random cards with optional parallel conversion

     Simulates pack opening experience by returning random cards from the catalog. When
    includeParallels=true, each card has a weighted probability of converting to a parallel based on the
    parallel's numberedTo value. Parallels are checked from rarest to most common using a cascading
    algorithm where lower numbered parallels (e.g., 1/1) are significantly rarer than higher numbered
    ones (e.g., /999), and unlimited parallels are the most common. Supports comprehensive filtering by
    set, release, player name, year, manufacturer, and card attributes. Note: setId and releaseId
    filters are mutually exclusive.

    Args:
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        set_id (Union[Unset, str]):
        set_name (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        attribute_id (Union[Unset, str]):
        attribute_short_name (Union[Unset, str]):
        sort (Union[Unset, GetRandomCardsSort]):
        order (Union[Unset, GetRandomCardsOrder]):  Default: GetRandomCardsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.
        include_parallels (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomCardsResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        number=number,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        set_id=set_id,
        set_name=set_name,
        manufacturer=manufacturer,
        attribute_id=attribute_id,
        attribute_short_name=attribute_short_name,
        sort=sort,
        order=order,
        count=count,
        include_parallels=include_parallels,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    set_id: Union[Unset, str] = UNSET,
    set_name: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    attribute_id: Union[Unset, str] = UNSET,
    attribute_short_name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetRandomCardsSort] = UNSET,
    order: Union[Unset, GetRandomCardsOrder] = GetRandomCardsOrder.ASC,
    count: Union[Unset, int] = 1,
    include_parallels: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, RandomCardsResponse]]:
    """Get random cards with optional parallel conversion

     Simulates pack opening experience by returning random cards from the catalog. When
    includeParallels=true, each card has a weighted probability of converting to a parallel based on the
    parallel's numberedTo value. Parallels are checked from rarest to most common using a cascading
    algorithm where lower numbered parallels (e.g., 1/1) are significantly rarer than higher numbered
    ones (e.g., /999), and unlimited parallels are the most common. Supports comprehensive filtering by
    set, release, player name, year, manufacturer, and card attributes. Note: setId and releaseId
    filters are mutually exclusive.

    Args:
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        set_id (Union[Unset, str]):
        set_name (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        attribute_id (Union[Unset, str]):
        attribute_short_name (Union[Unset, str]):
        sort (Union[Unset, GetRandomCardsSort]):
        order (Union[Unset, GetRandomCardsOrder]):  Default: GetRandomCardsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.
        include_parallels (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomCardsResponse]
    """

    return sync_detailed(
        client=client,
        name=name,
        number=number,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        set_id=set_id,
        set_name=set_name,
        manufacturer=manufacturer,
        attribute_id=attribute_id,
        attribute_short_name=attribute_short_name,
        sort=sort,
        order=order,
        count=count,
        include_parallels=include_parallels,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    set_id: Union[Unset, str] = UNSET,
    set_name: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    attribute_id: Union[Unset, str] = UNSET,
    attribute_short_name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetRandomCardsSort] = UNSET,
    order: Union[Unset, GetRandomCardsOrder] = GetRandomCardsOrder.ASC,
    count: Union[Unset, int] = 1,
    include_parallels: Union[Unset, bool] = False,
) -> Response[Union[ErrorResponse, RandomCardsResponse]]:
    """Get random cards with optional parallel conversion

     Simulates pack opening experience by returning random cards from the catalog. When
    includeParallels=true, each card has a weighted probability of converting to a parallel based on the
    parallel's numberedTo value. Parallels are checked from rarest to most common using a cascading
    algorithm where lower numbered parallels (e.g., 1/1) are significantly rarer than higher numbered
    ones (e.g., /999), and unlimited parallels are the most common. Supports comprehensive filtering by
    set, release, player name, year, manufacturer, and card attributes. Note: setId and releaseId
    filters are mutually exclusive.

    Args:
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        set_id (Union[Unset, str]):
        set_name (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        attribute_id (Union[Unset, str]):
        attribute_short_name (Union[Unset, str]):
        sort (Union[Unset, GetRandomCardsSort]):
        order (Union[Unset, GetRandomCardsOrder]):  Default: GetRandomCardsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.
        include_parallels (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomCardsResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        number=number,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        set_id=set_id,
        set_name=set_name,
        manufacturer=manufacturer,
        attribute_id=attribute_id,
        attribute_short_name=attribute_short_name,
        sort=sort,
        order=order,
        count=count,
        include_parallels=include_parallels,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    set_id: Union[Unset, str] = UNSET,
    set_name: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    attribute_id: Union[Unset, str] = UNSET,
    attribute_short_name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetRandomCardsSort] = UNSET,
    order: Union[Unset, GetRandomCardsOrder] = GetRandomCardsOrder.ASC,
    count: Union[Unset, int] = 1,
    include_parallels: Union[Unset, bool] = False,
) -> Optional[Union[ErrorResponse, RandomCardsResponse]]:
    """Get random cards with optional parallel conversion

     Simulates pack opening experience by returning random cards from the catalog. When
    includeParallels=true, each card has a weighted probability of converting to a parallel based on the
    parallel's numberedTo value. Parallels are checked from rarest to most common using a cascading
    algorithm where lower numbered parallels (e.g., 1/1) are significantly rarer than higher numbered
    ones (e.g., /999), and unlimited parallels are the most common. Supports comprehensive filtering by
    set, release, player name, year, manufacturer, and card attributes. Note: setId and releaseId
    filters are mutually exclusive.

    Args:
        name (Union[Unset, str]):
        number (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        set_id (Union[Unset, str]):
        set_name (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        attribute_id (Union[Unset, str]):
        attribute_short_name (Union[Unset, str]):
        sort (Union[Unset, GetRandomCardsSort]):
        order (Union[Unset, GetRandomCardsOrder]):  Default: GetRandomCardsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.
        include_parallels (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomCardsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            number=number,
            release_id=release_id,
            release_name=release_name,
            year=year,
            min_year=min_year,
            max_year=max_year,
            set_id=set_id,
            set_name=set_name,
            manufacturer=manufacturer,
            attribute_id=attribute_id,
            attribute_short_name=attribute_short_name,
            sort=sort,
            order=order,
            count=count,
            include_parallels=include_parallels,
        )
    ).parsed
