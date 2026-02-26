from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_cards_order import GetCardsOrder
from ...models.get_cards_sort import GetCardsSort
from ...models.paginated_cards_response import PaginatedCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
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
    sort: Union[Unset, GetCardsSort] = UNSET,
    order: Union[Unset, GetCardsOrder] = GetCardsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/cards",
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
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
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
    sort: Union[Unset, GetCardsSort] = UNSET,
    order: Union[Unset, GetCardsOrder] = GetCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """Search cards across entire catalog

     Global search endpoint for finding base cards across all releases, sets, and manufacturers. Supports
    complex filtering by player name, card number, release, set, year range, manufacturer, and
    attributes. Results include card details with release and set information. This is the primary
    endpoint for card discovery, player collections, and cross-product searches. Use specific release or
    set endpoints for more focused searches.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
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
        sort (Union[Unset, GetCardsSort]):
        order (Union[Unset, GetCardsOrder]):  Default: GetCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCardsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
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
    sort: Union[Unset, GetCardsSort] = UNSET,
    order: Union[Unset, GetCardsOrder] = GetCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """Search cards across entire catalog

     Global search endpoint for finding base cards across all releases, sets, and manufacturers. Supports
    complex filtering by player name, card number, release, set, year range, manufacturer, and
    attributes. Results include card details with release and set information. This is the primary
    endpoint for card discovery, player collections, and cross-product searches. Use specific release or
    set endpoints for more focused searches.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
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
        sort (Union[Unset, GetCardsSort]):
        order (Union[Unset, GetCardsOrder]):  Default: GetCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCardsResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
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
    sort: Union[Unset, GetCardsSort] = UNSET,
    order: Union[Unset, GetCardsOrder] = GetCardsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedCardsResponse]]:
    """Search cards across entire catalog

     Global search endpoint for finding base cards across all releases, sets, and manufacturers. Supports
    complex filtering by player name, card number, release, set, year range, manufacturer, and
    attributes. Results include card details with release and set information. This is the primary
    endpoint for card discovery, player collections, and cross-product searches. Use specific release or
    set endpoints for more focused searches.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
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
        sort (Union[Unset, GetCardsSort]):
        order (Union[Unset, GetCardsOrder]):  Default: GetCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCardsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
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
    sort: Union[Unset, GetCardsSort] = UNSET,
    order: Union[Unset, GetCardsOrder] = GetCardsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedCardsResponse]]:
    """Search cards across entire catalog

     Global search endpoint for finding base cards across all releases, sets, and manufacturers. Supports
    complex filtering by player name, card number, release, set, year range, manufacturer, and
    attributes. Results include card details with release and set information. This is the primary
    endpoint for card discovery, player collections, and cross-product searches. Use specific release or
    set endpoints for more focused searches.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
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
        sort (Union[Unset, GetCardsSort]):
        order (Union[Unset, GetCardsOrder]):  Default: GetCardsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCardsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
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
        )
    ).parsed
