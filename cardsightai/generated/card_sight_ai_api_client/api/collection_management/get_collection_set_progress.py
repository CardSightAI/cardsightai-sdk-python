from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_collection_set_progress_order import GetCollectionSetProgressOrder
from ...models.get_collection_set_progress_sort_by import GetCollectionSetProgressSortBy
from ...models.set_progress_list_response import SetProgressListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: UUID,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    sort_by: Union[Unset, GetCollectionSetProgressSortBy] = GetCollectionSetProgressSortBy.COMPLETION,
    order: Union[Unset, GetCollectionSetProgressOrder] = GetCollectionSetProgressOrder.DESC,
    min_completion: Union[Unset, float] = UNSET,
    near_complete: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["minCompletion"] = min_completion

    params["nearComplete"] = near_complete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/set-progress",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SetProgressListResponse]]:
    if response.status_code == 200:
        response_200 = SetProgressListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SetProgressListResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SetProgressListResponse]]:
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
    sort_by: Union[Unset, GetCollectionSetProgressSortBy] = GetCollectionSetProgressSortBy.COMPLETION,
    order: Union[Unset, GetCollectionSetProgressOrder] = GetCollectionSetProgressOrder.DESC,
    min_completion: Union[Unset, float] = UNSET,
    near_complete: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResponse, SetProgressListResponse]]:
    """Track set completion progress

     Track progress toward completing sets within your collection to focus acquisition efforts.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **sortBy**: Sort sets by completion, missing, cost, or difficulty (default: completion)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCompletion**: Filter sets with minimum completion percentage (0-100)
    - **nearComplete**: Filter for sets >80% complete (boolean)

    **Response includes:**

    **Summary statistics:**
    - Total sets represented in collection
    - Number of near-complete sets (>80%)
    - Number of fully complete sets (100%)
    - Total estimated cost to complete all sets

    **Per Set:**
    - Set name, release name, and release year for context
    - Total cards in set vs owned cards
    - Completion percentage
    - Missing card UUIDs (only included for sets >= 85% complete; empty array otherwise)
    - Estimated cost to complete (based on raw card market prices)
    - Difficulty score (based on card availability)

    **Use Cases:**
    - Identify which sets are close to completion
    - Calculate cost to complete specific sets
    - Focus buying decisions on near-complete sets
    - Track collection completion goals
    - Discover sets worth completing for investment

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Estimated costs based on raw (ungraded) card prices
    - Missing card UUIDs only returned for sets >= 85% complete (to avoid multi-thousand line responses)
    - For sets < 85% complete, use totalCards - ownedCards to get missing count
    - Sorted by completion percentage (highest first) by default

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        sort_by (Union[Unset, GetCollectionSetProgressSortBy]):  Default:
            GetCollectionSetProgressSortBy.COMPLETION.
        order (Union[Unset, GetCollectionSetProgressOrder]):  Default:
            GetCollectionSetProgressOrder.DESC.
        min_completion (Union[Unset, float]):
        near_complete (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetProgressListResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        sort_by=sort_by,
        order=order,
        min_completion=min_completion,
        near_complete=near_complete,
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
    sort_by: Union[Unset, GetCollectionSetProgressSortBy] = GetCollectionSetProgressSortBy.COMPLETION,
    order: Union[Unset, GetCollectionSetProgressOrder] = GetCollectionSetProgressOrder.DESC,
    min_completion: Union[Unset, float] = UNSET,
    near_complete: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResponse, SetProgressListResponse]]:
    """Track set completion progress

     Track progress toward completing sets within your collection to focus acquisition efforts.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **sortBy**: Sort sets by completion, missing, cost, or difficulty (default: completion)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCompletion**: Filter sets with minimum completion percentage (0-100)
    - **nearComplete**: Filter for sets >80% complete (boolean)

    **Response includes:**

    **Summary statistics:**
    - Total sets represented in collection
    - Number of near-complete sets (>80%)
    - Number of fully complete sets (100%)
    - Total estimated cost to complete all sets

    **Per Set:**
    - Set name, release name, and release year for context
    - Total cards in set vs owned cards
    - Completion percentage
    - Missing card UUIDs (only included for sets >= 85% complete; empty array otherwise)
    - Estimated cost to complete (based on raw card market prices)
    - Difficulty score (based on card availability)

    **Use Cases:**
    - Identify which sets are close to completion
    - Calculate cost to complete specific sets
    - Focus buying decisions on near-complete sets
    - Track collection completion goals
    - Discover sets worth completing for investment

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Estimated costs based on raw (ungraded) card prices
    - Missing card UUIDs only returned for sets >= 85% complete (to avoid multi-thousand line responses)
    - For sets < 85% complete, use totalCards - ownedCards to get missing count
    - Sorted by completion percentage (highest first) by default

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        sort_by (Union[Unset, GetCollectionSetProgressSortBy]):  Default:
            GetCollectionSetProgressSortBy.COMPLETION.
        order (Union[Unset, GetCollectionSetProgressOrder]):  Default:
            GetCollectionSetProgressOrder.DESC.
        min_completion (Union[Unset, float]):
        near_complete (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetProgressListResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        take=take,
        skip=skip,
        sort_by=sort_by,
        order=order,
        min_completion=min_completion,
        near_complete=near_complete,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    sort_by: Union[Unset, GetCollectionSetProgressSortBy] = GetCollectionSetProgressSortBy.COMPLETION,
    order: Union[Unset, GetCollectionSetProgressOrder] = GetCollectionSetProgressOrder.DESC,
    min_completion: Union[Unset, float] = UNSET,
    near_complete: Union[Unset, bool] = UNSET,
) -> Response[Union[ErrorResponse, SetProgressListResponse]]:
    """Track set completion progress

     Track progress toward completing sets within your collection to focus acquisition efforts.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **sortBy**: Sort sets by completion, missing, cost, or difficulty (default: completion)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCompletion**: Filter sets with minimum completion percentage (0-100)
    - **nearComplete**: Filter for sets >80% complete (boolean)

    **Response includes:**

    **Summary statistics:**
    - Total sets represented in collection
    - Number of near-complete sets (>80%)
    - Number of fully complete sets (100%)
    - Total estimated cost to complete all sets

    **Per Set:**
    - Set name, release name, and release year for context
    - Total cards in set vs owned cards
    - Completion percentage
    - Missing card UUIDs (only included for sets >= 85% complete; empty array otherwise)
    - Estimated cost to complete (based on raw card market prices)
    - Difficulty score (based on card availability)

    **Use Cases:**
    - Identify which sets are close to completion
    - Calculate cost to complete specific sets
    - Focus buying decisions on near-complete sets
    - Track collection completion goals
    - Discover sets worth completing for investment

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Estimated costs based on raw (ungraded) card prices
    - Missing card UUIDs only returned for sets >= 85% complete (to avoid multi-thousand line responses)
    - For sets < 85% complete, use totalCards - ownedCards to get missing count
    - Sorted by completion percentage (highest first) by default

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        sort_by (Union[Unset, GetCollectionSetProgressSortBy]):  Default:
            GetCollectionSetProgressSortBy.COMPLETION.
        order (Union[Unset, GetCollectionSetProgressOrder]):  Default:
            GetCollectionSetProgressOrder.DESC.
        min_completion (Union[Unset, float]):
        near_complete (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetProgressListResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        sort_by=sort_by,
        order=order,
        min_completion=min_completion,
        near_complete=near_complete,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    sort_by: Union[Unset, GetCollectionSetProgressSortBy] = GetCollectionSetProgressSortBy.COMPLETION,
    order: Union[Unset, GetCollectionSetProgressOrder] = GetCollectionSetProgressOrder.DESC,
    min_completion: Union[Unset, float] = UNSET,
    near_complete: Union[Unset, bool] = UNSET,
) -> Optional[Union[ErrorResponse, SetProgressListResponse]]:
    """Track set completion progress

     Track progress toward completing sets within your collection to focus acquisition efforts.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze

    **Query Parameters:**
    - **sortBy**: Sort sets by completion, missing, cost, or difficulty (default: completion)
    - **order**: Sort order - asc or desc (default: desc)
    - **page**: Page number for pagination (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **minCompletion**: Filter sets with minimum completion percentage (0-100)
    - **nearComplete**: Filter for sets >80% complete (boolean)

    **Response includes:**

    **Summary statistics:**
    - Total sets represented in collection
    - Number of near-complete sets (>80%)
    - Number of fully complete sets (100%)
    - Total estimated cost to complete all sets

    **Per Set:**
    - Set name, release name, and release year for context
    - Total cards in set vs owned cards
    - Completion percentage
    - Missing card UUIDs (only included for sets >= 85% complete; empty array otherwise)
    - Estimated cost to complete (based on raw card market prices)
    - Difficulty score (based on card availability)

    **Use Cases:**
    - Identify which sets are close to completion
    - Calculate cost to complete specific sets
    - Focus buying decisions on near-complete sets
    - Track collection completion goals
    - Discover sets worth completing for investment

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Estimated costs based on raw (ungraded) card prices
    - Missing card UUIDs only returned for sets >= 85% complete (to avoid multi-thousand line responses)
    - For sets < 85% complete, use totalCards - ownedCards to get missing count
    - Sorted by completion percentage (highest first) by default

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        sort_by (Union[Unset, GetCollectionSetProgressSortBy]):  Default:
            GetCollectionSetProgressSortBy.COMPLETION.
        order (Union[Unset, GetCollectionSetProgressOrder]):  Default:
            GetCollectionSetProgressOrder.DESC.
        min_completion (Union[Unset, float]):
        near_complete (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetProgressListResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            take=take,
            skip=skip,
            sort_by=sort_by,
            order=order,
            min_completion=min_completion,
            near_complete=near_complete,
        )
    ).parsed
