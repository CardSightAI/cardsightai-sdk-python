from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_breakdown_response import CollectionBreakdownResponse
from ...models.error_response import ErrorResponse
from ...models.get_collection_breakdown_group_by import GetCollectionBreakdownGroupBy
from ...models.get_collection_breakdown_order import GetCollectionBreakdownOrder
from ...models.get_collection_breakdown_sort_by import GetCollectionBreakdownSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: UUID,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    group_by: GetCollectionBreakdownGroupBy,
    sort_by: Union[Unset, GetCollectionBreakdownSortBy] = GetCollectionBreakdownSortBy.COUNT,
    order: Union[Unset, GetCollectionBreakdownOrder] = GetCollectionBreakdownOrder.DESC,
    min_count: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    json_group_by = group_by.value
    params["groupBy"] = json_group_by

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["minCount"] = min_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/breakdown",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CollectionBreakdownResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CollectionBreakdownResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CollectionBreakdownResponse.from_dict(response.json())

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
) -> Response[Union[CollectionBreakdownResponse, ErrorResponse]]:
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
    group_by: GetCollectionBreakdownGroupBy,
    sort_by: Union[Unset, GetCollectionBreakdownSortBy] = GetCollectionBreakdownSortBy.COUNT,
    order: Union[Unset, GetCollectionBreakdownOrder] = GetCollectionBreakdownOrder.DESC,
    min_count: Union[Unset, float] = UNSET,
) -> Response[Union[CollectionBreakdownResponse, ErrorResponse]]:
    r"""Analyze collection breakdown

     Analyze your collection by different dimensions to understand composition and distribution.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **groupBy**: Dimension to analyze (release, year, grade, player, manufacturer)
    - **sortBy**: Sort groups by count or percentage (default: count)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCount**: Filter groups with minimum card count

    **Response includes:**
    - **Summary statistics**: Total groups, cards, and top categories
    - **Group breakdowns**: Each group with metrics and top cards
    - **Pagination metadata**: For large result sets

    **Analysis Dimensions:**
    - **release**: Group by product release (e.g., \"1989 Topps\", \"2023 Prizm\") to see release
    concentration
    - **year**: Group by release year to see temporal distribution
    - **grade**: Group by grade to analyze condition distribution
    - **player**: Group by player to see player concentration
    - **manufacturer**: Group by card manufacturer

    **Metrics per Group:**
    - Card count and unique card count
    - Total invested (sum of purchase prices)
    - Percentage of total collection
    - Top 5 cards in the group

    **Use Cases:**
    - Identify concentration in specific releases or players
    - Analyze grade distribution for grading decisions
    - Discover diversification opportunities
    - Understand collection composition

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        group_by (GetCollectionBreakdownGroupBy):
        sort_by (Union[Unset, GetCollectionBreakdownSortBy]):  Default:
            GetCollectionBreakdownSortBy.COUNT.
        order (Union[Unset, GetCollectionBreakdownOrder]):  Default:
            GetCollectionBreakdownOrder.DESC.
        min_count (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionBreakdownResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        group_by=group_by,
        sort_by=sort_by,
        order=order,
        min_count=min_count,
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
    group_by: GetCollectionBreakdownGroupBy,
    sort_by: Union[Unset, GetCollectionBreakdownSortBy] = GetCollectionBreakdownSortBy.COUNT,
    order: Union[Unset, GetCollectionBreakdownOrder] = GetCollectionBreakdownOrder.DESC,
    min_count: Union[Unset, float] = UNSET,
) -> Optional[Union[CollectionBreakdownResponse, ErrorResponse]]:
    r"""Analyze collection breakdown

     Analyze your collection by different dimensions to understand composition and distribution.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **groupBy**: Dimension to analyze (release, year, grade, player, manufacturer)
    - **sortBy**: Sort groups by count or percentage (default: count)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCount**: Filter groups with minimum card count

    **Response includes:**
    - **Summary statistics**: Total groups, cards, and top categories
    - **Group breakdowns**: Each group with metrics and top cards
    - **Pagination metadata**: For large result sets

    **Analysis Dimensions:**
    - **release**: Group by product release (e.g., \"1989 Topps\", \"2023 Prizm\") to see release
    concentration
    - **year**: Group by release year to see temporal distribution
    - **grade**: Group by grade to analyze condition distribution
    - **player**: Group by player to see player concentration
    - **manufacturer**: Group by card manufacturer

    **Metrics per Group:**
    - Card count and unique card count
    - Total invested (sum of purchase prices)
    - Percentage of total collection
    - Top 5 cards in the group

    **Use Cases:**
    - Identify concentration in specific releases or players
    - Analyze grade distribution for grading decisions
    - Discover diversification opportunities
    - Understand collection composition

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        group_by (GetCollectionBreakdownGroupBy):
        sort_by (Union[Unset, GetCollectionBreakdownSortBy]):  Default:
            GetCollectionBreakdownSortBy.COUNT.
        order (Union[Unset, GetCollectionBreakdownOrder]):  Default:
            GetCollectionBreakdownOrder.DESC.
        min_count (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CollectionBreakdownResponse, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        take=take,
        skip=skip,
        group_by=group_by,
        sort_by=sort_by,
        order=order,
        min_count=min_count,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    group_by: GetCollectionBreakdownGroupBy,
    sort_by: Union[Unset, GetCollectionBreakdownSortBy] = GetCollectionBreakdownSortBy.COUNT,
    order: Union[Unset, GetCollectionBreakdownOrder] = GetCollectionBreakdownOrder.DESC,
    min_count: Union[Unset, float] = UNSET,
) -> Response[Union[CollectionBreakdownResponse, ErrorResponse]]:
    r"""Analyze collection breakdown

     Analyze your collection by different dimensions to understand composition and distribution.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **groupBy**: Dimension to analyze (release, year, grade, player, manufacturer)
    - **sortBy**: Sort groups by count or percentage (default: count)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCount**: Filter groups with minimum card count

    **Response includes:**
    - **Summary statistics**: Total groups, cards, and top categories
    - **Group breakdowns**: Each group with metrics and top cards
    - **Pagination metadata**: For large result sets

    **Analysis Dimensions:**
    - **release**: Group by product release (e.g., \"1989 Topps\", \"2023 Prizm\") to see release
    concentration
    - **year**: Group by release year to see temporal distribution
    - **grade**: Group by grade to analyze condition distribution
    - **player**: Group by player to see player concentration
    - **manufacturer**: Group by card manufacturer

    **Metrics per Group:**
    - Card count and unique card count
    - Total invested (sum of purchase prices)
    - Percentage of total collection
    - Top 5 cards in the group

    **Use Cases:**
    - Identify concentration in specific releases or players
    - Analyze grade distribution for grading decisions
    - Discover diversification opportunities
    - Understand collection composition

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        group_by (GetCollectionBreakdownGroupBy):
        sort_by (Union[Unset, GetCollectionBreakdownSortBy]):  Default:
            GetCollectionBreakdownSortBy.COUNT.
        order (Union[Unset, GetCollectionBreakdownOrder]):  Default:
            GetCollectionBreakdownOrder.DESC.
        min_count (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionBreakdownResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        group_by=group_by,
        sort_by=sort_by,
        order=order,
        min_count=min_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    group_by: GetCollectionBreakdownGroupBy,
    sort_by: Union[Unset, GetCollectionBreakdownSortBy] = GetCollectionBreakdownSortBy.COUNT,
    order: Union[Unset, GetCollectionBreakdownOrder] = GetCollectionBreakdownOrder.DESC,
    min_count: Union[Unset, float] = UNSET,
) -> Optional[Union[CollectionBreakdownResponse, ErrorResponse]]:
    r"""Analyze collection breakdown

     Analyze your collection by different dimensions to understand composition and distribution.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **groupBy**: Dimension to analyze (release, year, grade, player, manufacturer)
    - **sortBy**: Sort groups by count or percentage (default: count)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCount**: Filter groups with minimum card count

    **Response includes:**
    - **Summary statistics**: Total groups, cards, and top categories
    - **Group breakdowns**: Each group with metrics and top cards
    - **Pagination metadata**: For large result sets

    **Analysis Dimensions:**
    - **release**: Group by product release (e.g., \"1989 Topps\", \"2023 Prizm\") to see release
    concentration
    - **year**: Group by release year to see temporal distribution
    - **grade**: Group by grade to analyze condition distribution
    - **player**: Group by player to see player concentration
    - **manufacturer**: Group by card manufacturer

    **Metrics per Group:**
    - Card count and unique card count
    - Total invested (sum of purchase prices)
    - Percentage of total collection
    - Top 5 cards in the group

    **Use Cases:**
    - Identify concentration in specific releases or players
    - Analyze grade distribution for grading decisions
    - Discover diversification opportunities
    - Understand collection composition

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        group_by (GetCollectionBreakdownGroupBy):
        sort_by (Union[Unset, GetCollectionBreakdownSortBy]):  Default:
            GetCollectionBreakdownSortBy.COUNT.
        order (Union[Unset, GetCollectionBreakdownOrder]):  Default:
            GetCollectionBreakdownOrder.DESC.
        min_count (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CollectionBreakdownResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            take=take,
            skip=skip,
            group_by=group_by,
            sort_by=sort_by,
            order=order,
            min_count=min_count,
        )
    ).parsed
