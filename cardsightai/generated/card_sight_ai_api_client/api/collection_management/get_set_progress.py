from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.set_progress import SetProgress
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    set_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/set-progress/{set_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SetProgress]]:
    if response.status_code == 200:
        response_200 = SetProgress.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SetProgress.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SetProgress]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    set_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SetProgress]]:
    """Get completion progress for specific set

     Get detailed completion progress for a specific set within your collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **setId**: UUID of the set to check progress for

    **Response includes:**
    - Set name, release name, and release year
    - Total cards in set vs owned cards
    - Completion percentage (0-100)
    - Array of missing card UUIDs

    **Use Cases:**
    - Check progress on a specific set
    - Get list of missing cards for targeted purchasing
    - Track progress toward set completion goal
    - Identify which cards are still needed

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Missing cards returned as UUIDs for easy card lookup
    - Returns 404 if set is not represented in collection

    Args:
        collection_id (UUID):
        set_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetProgress]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        set_id=set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    set_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SetProgress]]:
    """Get completion progress for specific set

     Get detailed completion progress for a specific set within your collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **setId**: UUID of the set to check progress for

    **Response includes:**
    - Set name, release name, and release year
    - Total cards in set vs owned cards
    - Completion percentage (0-100)
    - Array of missing card UUIDs

    **Use Cases:**
    - Check progress on a specific set
    - Get list of missing cards for targeted purchasing
    - Track progress toward set completion goal
    - Identify which cards are still needed

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Missing cards returned as UUIDs for easy card lookup
    - Returns 404 if set is not represented in collection

    Args:
        collection_id (UUID):
        set_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetProgress]
    """

    return sync_detailed(
        collection_id=collection_id,
        set_id=set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    set_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SetProgress]]:
    """Get completion progress for specific set

     Get detailed completion progress for a specific set within your collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **setId**: UUID of the set to check progress for

    **Response includes:**
    - Set name, release name, and release year
    - Total cards in set vs owned cards
    - Completion percentage (0-100)
    - Array of missing card UUIDs

    **Use Cases:**
    - Check progress on a specific set
    - Get list of missing cards for targeted purchasing
    - Track progress toward set completion goal
    - Identify which cards are still needed

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Missing cards returned as UUIDs for easy card lookup
    - Returns 404 if set is not represented in collection

    Args:
        collection_id (UUID):
        set_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetProgress]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        set_id=set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    set_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SetProgress]]:
    """Get completion progress for specific set

     Get detailed completion progress for a specific set within your collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **setId**: UUID of the set to check progress for

    **Response includes:**
    - Set name, release name, and release year
    - Total cards in set vs owned cards
    - Completion percentage (0-100)
    - Array of missing card UUIDs

    **Use Cases:**
    - Check progress on a specific set
    - Get list of missing cards for targeted purchasing
    - Track progress toward set completion goal
    - Identify which cards are still needed

    **Important Notes:**
    - Only base cards are considered (parallels excluded)
    - Missing cards returned as UUIDs for easy card lookup
    - Returns 404 if set is not represented in collection

    Args:
        collection_id (UUID):
        set_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetProgress]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            set_id=set_id,
            client=client,
        )
    ).parsed
