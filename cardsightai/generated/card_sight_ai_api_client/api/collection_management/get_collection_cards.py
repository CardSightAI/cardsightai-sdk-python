from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_collection_cards_order import GetCollectionCardsOrder
from ...models.get_collection_cards_sort import GetCollectionCardsSort
from ...models.paginated_collection_cards_response import PaginatedCollectionCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: UUID,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    card_id: Union[Unset, UUID] = UNSET,
    parallel_id: Union[Unset, UUID] = UNSET,
    grade_id: Union[Unset, UUID] = UNSET,
    has_sold: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetCollectionCardsSort] = UNSET,
    order: Union[Unset, GetCollectionCardsOrder] = GetCollectionCardsOrder.DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    json_card_id: Union[Unset, str] = UNSET
    if not isinstance(card_id, Unset):
        json_card_id = str(card_id)
    params["cardId"] = json_card_id

    json_parallel_id: Union[Unset, str] = UNSET
    if not isinstance(parallel_id, Unset):
        json_parallel_id = str(parallel_id)
    params["parallelId"] = json_parallel_id

    json_grade_id: Union[Unset, str] = UNSET
    if not isinstance(grade_id, Unset):
        json_grade_id = str(grade_id)
    params["gradeId"] = json_grade_id

    params["hasSold"] = has_sold

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
        "url": f"/v1/collection/{collection_id}/cards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedCollectionCardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedCollectionCardsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    card_id: Union[Unset, UUID] = UNSET,
    parallel_id: Union[Unset, UUID] = UNSET,
    grade_id: Union[Unset, UUID] = UNSET,
    has_sold: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetCollectionCardsSort] = UNSET,
    order: Union[Unset, GetCollectionCardsOrder] = GetCollectionCardsOrder.DESC,
) -> Response[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    """List collection cards

     Retrieve a paginated list of all cards in a specific collection with advanced filtering options.

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, value, purchaseDate, addedDate)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names and descriptions
    - **binderId**: Filter by specific binder
    - **graded**: Filter graded cards only (true/false)
    - **forSale**: Filter cards marked for sale
    - **minValue**: Minimum current value filter
    - **maxValue**: Maximum current value filter

    **Response includes:**
    - Full card catalog details (name, set, year, etc.)
    - Collection-specific metadata (quantity, grade, purchase info)
    - Current market values
    - Aggregated statistics (total value, card count)
    - Pagination metadata

    **Use Cases:**
    - Browse collection inventory
    - Search for specific cards
    - Filter high-value cards
    - Export collection data
    - Generate collection reports

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        card_id (Union[Unset, UUID]):
        parallel_id (Union[Unset, UUID]):
        grade_id (Union[Unset, UUID]):
        has_sold (Union[Unset, bool]):
        sort (Union[Unset, GetCollectionCardsSort]):
        order (Union[Unset, GetCollectionCardsOrder]):  Default: GetCollectionCardsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCollectionCardsResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        card_id=card_id,
        parallel_id=parallel_id,
        grade_id=grade_id,
        has_sold=has_sold,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    card_id: Union[Unset, UUID] = UNSET,
    parallel_id: Union[Unset, UUID] = UNSET,
    grade_id: Union[Unset, UUID] = UNSET,
    has_sold: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetCollectionCardsSort] = UNSET,
    order: Union[Unset, GetCollectionCardsOrder] = GetCollectionCardsOrder.DESC,
) -> Optional[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    """List collection cards

     Retrieve a paginated list of all cards in a specific collection with advanced filtering options.

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, value, purchaseDate, addedDate)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names and descriptions
    - **binderId**: Filter by specific binder
    - **graded**: Filter graded cards only (true/false)
    - **forSale**: Filter cards marked for sale
    - **minValue**: Minimum current value filter
    - **maxValue**: Maximum current value filter

    **Response includes:**
    - Full card catalog details (name, set, year, etc.)
    - Collection-specific metadata (quantity, grade, purchase info)
    - Current market values
    - Aggregated statistics (total value, card count)
    - Pagination metadata

    **Use Cases:**
    - Browse collection inventory
    - Search for specific cards
    - Filter high-value cards
    - Export collection data
    - Generate collection reports

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        card_id (Union[Unset, UUID]):
        parallel_id (Union[Unset, UUID]):
        grade_id (Union[Unset, UUID]):
        has_sold (Union[Unset, bool]):
        sort (Union[Unset, GetCollectionCardsSort]):
        order (Union[Unset, GetCollectionCardsOrder]):  Default: GetCollectionCardsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCollectionCardsResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        take=take,
        skip=skip,
        card_id=card_id,
        parallel_id=parallel_id,
        grade_id=grade_id,
        has_sold=has_sold,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    card_id: Union[Unset, UUID] = UNSET,
    parallel_id: Union[Unset, UUID] = UNSET,
    grade_id: Union[Unset, UUID] = UNSET,
    has_sold: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetCollectionCardsSort] = UNSET,
    order: Union[Unset, GetCollectionCardsOrder] = GetCollectionCardsOrder.DESC,
) -> Response[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    """List collection cards

     Retrieve a paginated list of all cards in a specific collection with advanced filtering options.

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, value, purchaseDate, addedDate)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names and descriptions
    - **binderId**: Filter by specific binder
    - **graded**: Filter graded cards only (true/false)
    - **forSale**: Filter cards marked for sale
    - **minValue**: Minimum current value filter
    - **maxValue**: Maximum current value filter

    **Response includes:**
    - Full card catalog details (name, set, year, etc.)
    - Collection-specific metadata (quantity, grade, purchase info)
    - Current market values
    - Aggregated statistics (total value, card count)
    - Pagination metadata

    **Use Cases:**
    - Browse collection inventory
    - Search for specific cards
    - Filter high-value cards
    - Export collection data
    - Generate collection reports

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        card_id (Union[Unset, UUID]):
        parallel_id (Union[Unset, UUID]):
        grade_id (Union[Unset, UUID]):
        has_sold (Union[Unset, bool]):
        sort (Union[Unset, GetCollectionCardsSort]):
        order (Union[Unset, GetCollectionCardsOrder]):  Default: GetCollectionCardsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedCollectionCardsResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        card_id=card_id,
        parallel_id=parallel_id,
        grade_id=grade_id,
        has_sold=has_sold,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    card_id: Union[Unset, UUID] = UNSET,
    parallel_id: Union[Unset, UUID] = UNSET,
    grade_id: Union[Unset, UUID] = UNSET,
    has_sold: Union[Unset, bool] = UNSET,
    sort: Union[Unset, GetCollectionCardsSort] = UNSET,
    order: Union[Unset, GetCollectionCardsOrder] = GetCollectionCardsOrder.DESC,
) -> Optional[Union[ErrorResponse, PaginatedCollectionCardsResponse]]:
    """List collection cards

     Retrieve a paginated list of all cards in a specific collection with advanced filtering options.

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, value, purchaseDate, addedDate)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names and descriptions
    - **binderId**: Filter by specific binder
    - **graded**: Filter graded cards only (true/false)
    - **forSale**: Filter cards marked for sale
    - **minValue**: Minimum current value filter
    - **maxValue**: Maximum current value filter

    **Response includes:**
    - Full card catalog details (name, set, year, etc.)
    - Collection-specific metadata (quantity, grade, purchase info)
    - Current market values
    - Aggregated statistics (total value, card count)
    - Pagination metadata

    **Use Cases:**
    - Browse collection inventory
    - Search for specific cards
    - Filter high-value cards
    - Export collection data
    - Generate collection reports

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        card_id (Union[Unset, UUID]):
        parallel_id (Union[Unset, UUID]):
        grade_id (Union[Unset, UUID]):
        has_sold (Union[Unset, bool]):
        sort (Union[Unset, GetCollectionCardsSort]):
        order (Union[Unset, GetCollectionCardsOrder]):  Default: GetCollectionCardsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedCollectionCardsResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            take=take,
            skip=skip,
            card_id=card_id,
            parallel_id=parallel_id,
            grade_id=grade_id,
            has_sold=has_sold,
            sort=sort,
            order=order,
        )
    ).parsed
