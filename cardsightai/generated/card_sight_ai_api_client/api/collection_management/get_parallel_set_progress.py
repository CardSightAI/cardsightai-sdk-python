from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.parallel_set_progress import ParallelSetProgress
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    set_id: UUID,
    parallel_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/set-progress/{set_id}/{parallel_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ParallelSetProgress]]:
    if response.status_code == 200:
        response_200 = ParallelSetProgress.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ParallelSetProgress.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ParallelSetProgress]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    set_id: UUID,
    parallel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, ParallelSetProgress]]:
    r"""Track parallel completion within a set

     Track progress toward completing a specific parallel variant within a set.

    This endpoint tracks completion for a specific parallel (e.g., all Refractors, all Gold parallels)
    within a set. Unlike the base set progress endpoint which counts any parallel as complete, this
    endpoint only counts cards where you own the specific parallel variant.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze
    - **setId**: UUID of the set to check progress for
    - **parallelId**: UUID of the specific parallel variant (e.g., Refractor, Gold, Silver, Prizm, etc.)

    **Response includes:**
    - Set name, release name, and release year for context
    - Parallel name (e.g., \"Refractor\", \"Gold Prizm\")
    - Total cards in set vs owned cards of this specific parallel
    - Completion percentage for this parallel variant (0-100)
    - Array of missing card UUIDs for this parallel (for targeted buying)
    - Estimated cost to complete this parallel variant (based on raw card prices)
    - Average card value for this parallel

    **How it differs from base set progress:**
    - **Base set progress** (/set-progress/:setId): Counts card #5 as owned if you have ANY parallel
    (base, refractor, gold, etc.)
    - **Parallel set progress** (this endpoint): Only counts card #5 if you own it as THIS specific
    parallel

    **Use Cases:**
    - Track completion of premium parallel sets (Refractors, numbered parallels)
    - Calculate exact cost to complete a specific parallel run
    - Focus buying decisions on specific parallel variants
    - Chase rare parallel variations (e.g., Gold /10, Orange /25)
    - Investment tracking for high-value parallels
    - Set collection goals for parallel variants

    **Example Scenario:**
    You're collecting all Refractor parallels from 2023 Prizm Basketball Base Set. You own 187 of 250
    Refractors. This endpoint returns:
    - 74.8% complete
    - List of 63 missing Refractor card UUIDs
    - Estimated $1,247.50 to complete the Refractor parallel set

    **Important Notes:**
    - Only base cards are considered (card variations where baseCardId IS NOT NULL are excluded)
    - Filters collection_cards by the specific parallelId provided
    - Estimated costs are based on raw (ungraded) card prices for this parallel
    - Returns 404 if parallel doesn't belong to the specified set
    - Missing cards are returned as UUIDs for easy lookup via the catalog API

    Args:
        collection_id (UUID):
        set_id (UUID):
        parallel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ParallelSetProgress]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        set_id=set_id,
        parallel_id=parallel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    set_id: UUID,
    parallel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, ParallelSetProgress]]:
    r"""Track parallel completion within a set

     Track progress toward completing a specific parallel variant within a set.

    This endpoint tracks completion for a specific parallel (e.g., all Refractors, all Gold parallels)
    within a set. Unlike the base set progress endpoint which counts any parallel as complete, this
    endpoint only counts cards where you own the specific parallel variant.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze
    - **setId**: UUID of the set to check progress for
    - **parallelId**: UUID of the specific parallel variant (e.g., Refractor, Gold, Silver, Prizm, etc.)

    **Response includes:**
    - Set name, release name, and release year for context
    - Parallel name (e.g., \"Refractor\", \"Gold Prizm\")
    - Total cards in set vs owned cards of this specific parallel
    - Completion percentage for this parallel variant (0-100)
    - Array of missing card UUIDs for this parallel (for targeted buying)
    - Estimated cost to complete this parallel variant (based on raw card prices)
    - Average card value for this parallel

    **How it differs from base set progress:**
    - **Base set progress** (/set-progress/:setId): Counts card #5 as owned if you have ANY parallel
    (base, refractor, gold, etc.)
    - **Parallel set progress** (this endpoint): Only counts card #5 if you own it as THIS specific
    parallel

    **Use Cases:**
    - Track completion of premium parallel sets (Refractors, numbered parallels)
    - Calculate exact cost to complete a specific parallel run
    - Focus buying decisions on specific parallel variants
    - Chase rare parallel variations (e.g., Gold /10, Orange /25)
    - Investment tracking for high-value parallels
    - Set collection goals for parallel variants

    **Example Scenario:**
    You're collecting all Refractor parallels from 2023 Prizm Basketball Base Set. You own 187 of 250
    Refractors. This endpoint returns:
    - 74.8% complete
    - List of 63 missing Refractor card UUIDs
    - Estimated $1,247.50 to complete the Refractor parallel set

    **Important Notes:**
    - Only base cards are considered (card variations where baseCardId IS NOT NULL are excluded)
    - Filters collection_cards by the specific parallelId provided
    - Estimated costs are based on raw (ungraded) card prices for this parallel
    - Returns 404 if parallel doesn't belong to the specified set
    - Missing cards are returned as UUIDs for easy lookup via the catalog API

    Args:
        collection_id (UUID):
        set_id (UUID):
        parallel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ParallelSetProgress]
    """

    return sync_detailed(
        collection_id=collection_id,
        set_id=set_id,
        parallel_id=parallel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    set_id: UUID,
    parallel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, ParallelSetProgress]]:
    r"""Track parallel completion within a set

     Track progress toward completing a specific parallel variant within a set.

    This endpoint tracks completion for a specific parallel (e.g., all Refractors, all Gold parallels)
    within a set. Unlike the base set progress endpoint which counts any parallel as complete, this
    endpoint only counts cards where you own the specific parallel variant.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze
    - **setId**: UUID of the set to check progress for
    - **parallelId**: UUID of the specific parallel variant (e.g., Refractor, Gold, Silver, Prizm, etc.)

    **Response includes:**
    - Set name, release name, and release year for context
    - Parallel name (e.g., \"Refractor\", \"Gold Prizm\")
    - Total cards in set vs owned cards of this specific parallel
    - Completion percentage for this parallel variant (0-100)
    - Array of missing card UUIDs for this parallel (for targeted buying)
    - Estimated cost to complete this parallel variant (based on raw card prices)
    - Average card value for this parallel

    **How it differs from base set progress:**
    - **Base set progress** (/set-progress/:setId): Counts card #5 as owned if you have ANY parallel
    (base, refractor, gold, etc.)
    - **Parallel set progress** (this endpoint): Only counts card #5 if you own it as THIS specific
    parallel

    **Use Cases:**
    - Track completion of premium parallel sets (Refractors, numbered parallels)
    - Calculate exact cost to complete a specific parallel run
    - Focus buying decisions on specific parallel variants
    - Chase rare parallel variations (e.g., Gold /10, Orange /25)
    - Investment tracking for high-value parallels
    - Set collection goals for parallel variants

    **Example Scenario:**
    You're collecting all Refractor parallels from 2023 Prizm Basketball Base Set. You own 187 of 250
    Refractors. This endpoint returns:
    - 74.8% complete
    - List of 63 missing Refractor card UUIDs
    - Estimated $1,247.50 to complete the Refractor parallel set

    **Important Notes:**
    - Only base cards are considered (card variations where baseCardId IS NOT NULL are excluded)
    - Filters collection_cards by the specific parallelId provided
    - Estimated costs are based on raw (ungraded) card prices for this parallel
    - Returns 404 if parallel doesn't belong to the specified set
    - Missing cards are returned as UUIDs for easy lookup via the catalog API

    Args:
        collection_id (UUID):
        set_id (UUID):
        parallel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ParallelSetProgress]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        set_id=set_id,
        parallel_id=parallel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    set_id: UUID,
    parallel_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, ParallelSetProgress]]:
    r"""Track parallel completion within a set

     Track progress toward completing a specific parallel variant within a set.

    This endpoint tracks completion for a specific parallel (e.g., all Refractors, all Gold parallels)
    within a set. Unlike the base set progress endpoint which counts any parallel as complete, this
    endpoint only counts cards where you own the specific parallel variant.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to analyze
    - **setId**: UUID of the set to check progress for
    - **parallelId**: UUID of the specific parallel variant (e.g., Refractor, Gold, Silver, Prizm, etc.)

    **Response includes:**
    - Set name, release name, and release year for context
    - Parallel name (e.g., \"Refractor\", \"Gold Prizm\")
    - Total cards in set vs owned cards of this specific parallel
    - Completion percentage for this parallel variant (0-100)
    - Array of missing card UUIDs for this parallel (for targeted buying)
    - Estimated cost to complete this parallel variant (based on raw card prices)
    - Average card value for this parallel

    **How it differs from base set progress:**
    - **Base set progress** (/set-progress/:setId): Counts card #5 as owned if you have ANY parallel
    (base, refractor, gold, etc.)
    - **Parallel set progress** (this endpoint): Only counts card #5 if you own it as THIS specific
    parallel

    **Use Cases:**
    - Track completion of premium parallel sets (Refractors, numbered parallels)
    - Calculate exact cost to complete a specific parallel run
    - Focus buying decisions on specific parallel variants
    - Chase rare parallel variations (e.g., Gold /10, Orange /25)
    - Investment tracking for high-value parallels
    - Set collection goals for parallel variants

    **Example Scenario:**
    You're collecting all Refractor parallels from 2023 Prizm Basketball Base Set. You own 187 of 250
    Refractors. This endpoint returns:
    - 74.8% complete
    - List of 63 missing Refractor card UUIDs
    - Estimated $1,247.50 to complete the Refractor parallel set

    **Important Notes:**
    - Only base cards are considered (card variations where baseCardId IS NOT NULL are excluded)
    - Filters collection_cards by the specific parallelId provided
    - Estimated costs are based on raw (ungraded) card prices for this parallel
    - Returns 404 if parallel doesn't belong to the specified set
    - Missing cards are returned as UUIDs for easy lookup via the catalog API

    Args:
        collection_id (UUID):
        set_id (UUID):
        parallel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ParallelSetProgress]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            set_id=set_id,
            parallel_id=parallel_id,
            client=client,
        )
    ).parsed
