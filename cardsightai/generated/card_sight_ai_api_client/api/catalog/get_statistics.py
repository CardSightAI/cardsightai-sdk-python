from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_statistics_response import CatalogStatisticsResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/statistics",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CatalogStatisticsResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CatalogStatisticsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CatalogStatisticsResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CatalogStatisticsResponse, ErrorResponse]]:
    """Get comprehensive catalog statistics


    # Catalog Statistics

    This endpoint provides comprehensive statistics about the entire card catalog database.

    **Purpose:**
    Collectors can view high-level metrics to understand the scope and breadth of the CardSight AI
    catalog. This helps inform collecting strategies by showing:
    - What segments and manufacturers are available
    - How many releases exist per year
    - The depth of card data (base cards vs parallels vs variations)
    - AI identification capabilities

    **Response Structure:**

    **Segments:**
    - Total count of sports/card segments
    - Breakdown showing each segment name with release count

    **Manufacturers:**
    - Total count of card manufacturers
    - All manufacturers with their release counts

    **Releases:**
    - Total count across all years
    - Breakdown by segment with total releases per segment
    - Within each segment, year-by-year breakdown of release counts

    **Sets:**
    - Total count of card sets
    - Count of identifiable sets (sets that can be recognized by AI)

    **Cards:**
    - Total count of all cards in catalog
    - Count of base cards (original cards)
    - Count of variations (alternate versions of base cards)

    **Parallels:**
    - Total count of parallel types
    - Count of full set parallels (apply to entire set)
    - Count of partial parallels (apply to specific cards only)

    **Caching:**
    This endpoint is cached for 1 hour to optimize performance since catalog statistics change
    infrequently.

    **Use Cases:**
    - Understanding catalog coverage before starting a collection
    - Identifying which manufacturers have the most complete data
    - Seeing historical trends in releases by year
    - Gauging AI identification capabilities for specific sets

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CatalogStatisticsResponse, ErrorResponse]]:
    """Get comprehensive catalog statistics


    # Catalog Statistics

    This endpoint provides comprehensive statistics about the entire card catalog database.

    **Purpose:**
    Collectors can view high-level metrics to understand the scope and breadth of the CardSight AI
    catalog. This helps inform collecting strategies by showing:
    - What segments and manufacturers are available
    - How many releases exist per year
    - The depth of card data (base cards vs parallels vs variations)
    - AI identification capabilities

    **Response Structure:**

    **Segments:**
    - Total count of sports/card segments
    - Breakdown showing each segment name with release count

    **Manufacturers:**
    - Total count of card manufacturers
    - All manufacturers with their release counts

    **Releases:**
    - Total count across all years
    - Breakdown by segment with total releases per segment
    - Within each segment, year-by-year breakdown of release counts

    **Sets:**
    - Total count of card sets
    - Count of identifiable sets (sets that can be recognized by AI)

    **Cards:**
    - Total count of all cards in catalog
    - Count of base cards (original cards)
    - Count of variations (alternate versions of base cards)

    **Parallels:**
    - Total count of parallel types
    - Count of full set parallels (apply to entire set)
    - Count of partial parallels (apply to specific cards only)

    **Caching:**
    This endpoint is cached for 1 hour to optimize performance since catalog statistics change
    infrequently.

    **Use Cases:**
    - Understanding catalog coverage before starting a collection
    - Identifying which manufacturers have the most complete data
    - Seeing historical trends in releases by year
    - Gauging AI identification capabilities for specific sets

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogStatisticsResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CatalogStatisticsResponse, ErrorResponse]]:
    """Get comprehensive catalog statistics


    # Catalog Statistics

    This endpoint provides comprehensive statistics about the entire card catalog database.

    **Purpose:**
    Collectors can view high-level metrics to understand the scope and breadth of the CardSight AI
    catalog. This helps inform collecting strategies by showing:
    - What segments and manufacturers are available
    - How many releases exist per year
    - The depth of card data (base cards vs parallels vs variations)
    - AI identification capabilities

    **Response Structure:**

    **Segments:**
    - Total count of sports/card segments
    - Breakdown showing each segment name with release count

    **Manufacturers:**
    - Total count of card manufacturers
    - All manufacturers with their release counts

    **Releases:**
    - Total count across all years
    - Breakdown by segment with total releases per segment
    - Within each segment, year-by-year breakdown of release counts

    **Sets:**
    - Total count of card sets
    - Count of identifiable sets (sets that can be recognized by AI)

    **Cards:**
    - Total count of all cards in catalog
    - Count of base cards (original cards)
    - Count of variations (alternate versions of base cards)

    **Parallels:**
    - Total count of parallel types
    - Count of full set parallels (apply to entire set)
    - Count of partial parallels (apply to specific cards only)

    **Caching:**
    This endpoint is cached for 1 hour to optimize performance since catalog statistics change
    infrequently.

    **Use Cases:**
    - Understanding catalog coverage before starting a collection
    - Identifying which manufacturers have the most complete data
    - Seeing historical trends in releases by year
    - Gauging AI identification capabilities for specific sets

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogStatisticsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CatalogStatisticsResponse, ErrorResponse]]:
    """Get comprehensive catalog statistics


    # Catalog Statistics

    This endpoint provides comprehensive statistics about the entire card catalog database.

    **Purpose:**
    Collectors can view high-level metrics to understand the scope and breadth of the CardSight AI
    catalog. This helps inform collecting strategies by showing:
    - What segments and manufacturers are available
    - How many releases exist per year
    - The depth of card data (base cards vs parallels vs variations)
    - AI identification capabilities

    **Response Structure:**

    **Segments:**
    - Total count of sports/card segments
    - Breakdown showing each segment name with release count

    **Manufacturers:**
    - Total count of card manufacturers
    - All manufacturers with their release counts

    **Releases:**
    - Total count across all years
    - Breakdown by segment with total releases per segment
    - Within each segment, year-by-year breakdown of release counts

    **Sets:**
    - Total count of card sets
    - Count of identifiable sets (sets that can be recognized by AI)

    **Cards:**
    - Total count of all cards in catalog
    - Count of base cards (original cards)
    - Count of variations (alternate versions of base cards)

    **Parallels:**
    - Total count of parallel types
    - Count of full set parallels (apply to entire set)
    - Count of partial parallels (apply to specific cards only)

    **Caching:**
    This endpoint is cached for 1 hour to optimize performance since catalog statistics change
    infrequently.

    **Use Cases:**
    - Understanding catalog coverage before starting a collection
    - Identifying which manufacturers have the most complete data
    - Seeing historical trends in releases by year
    - Gauging AI identification capabilities for specific sets

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogStatisticsResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
