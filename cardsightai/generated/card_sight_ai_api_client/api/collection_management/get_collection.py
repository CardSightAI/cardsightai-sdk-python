from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Collection, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = Collection.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Collection.from_dict(response.json())

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
) -> Response[Union[Collection, ErrorResponse]]:
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
) -> Response[Union[Collection, ErrorResponse]]:
    """Get collection details

     Retrieve detailed information about a specific collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to retrieve

    **Response includes:**
    - Complete collection metadata
    - Collector information
    - Creation and update timestamps
    - Card count and value statistics
    - Collection type and privacy settings

    **Security:**
    - Only collections owned by your API key can be accessed
    - Attempting to access another client's collection returns 404

    **Use Cases:**
    - Display collection details page
    - Load collection for editing
    - Verify collection settings
    - Get collection statistics

    Args:
        collection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Collection, ErrorResponse]]:
    """Get collection details

     Retrieve detailed information about a specific collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to retrieve

    **Response includes:**
    - Complete collection metadata
    - Collector information
    - Creation and update timestamps
    - Card count and value statistics
    - Collection type and privacy settings

    **Security:**
    - Only collections owned by your API key can be accessed
    - Attempting to access another client's collection returns 404

    **Use Cases:**
    - Display collection details page
    - Load collection for editing
    - Verify collection settings
    - Get collection statistics

    Args:
        collection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Collection, ErrorResponse]]:
    """Get collection details

     Retrieve detailed information about a specific collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to retrieve

    **Response includes:**
    - Complete collection metadata
    - Collector information
    - Creation and update timestamps
    - Card count and value statistics
    - Collection type and privacy settings

    **Security:**
    - Only collections owned by your API key can be accessed
    - Attempting to access another client's collection returns 404

    **Use Cases:**
    - Display collection details page
    - Load collection for editing
    - Verify collection settings
    - Get collection statistics

    Args:
        collection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Collection, ErrorResponse]]:
    """Get collection details

     Retrieve detailed information about a specific collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to retrieve

    **Response includes:**
    - Complete collection metadata
    - Collector information
    - Creation and update timestamps
    - Card count and value statistics
    - Collection type and privacy settings

    **Security:**
    - Only collections owned by your API key can be accessed
    - Attempting to access another client's collection returns 404

    **Use Cases:**
    - Display collection details page
    - Load collection for editing
    - Verify collection settings
    - Get collection statistics

    Args:
        collection_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
