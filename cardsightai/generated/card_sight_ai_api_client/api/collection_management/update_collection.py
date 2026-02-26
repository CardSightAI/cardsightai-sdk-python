from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.error_response import ErrorResponse
from ...models.update_collection_input import UpdateCollectionInput
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    *,
    body: UpdateCollectionInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/collection/{collection_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateCollectionInput,
) -> Response[Union[Collection, ErrorResponse]]:
    """Update collection

     Update an existing collection's properties.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to update

    **Updatable Fields:**
    - **name**: New collection name (must be unique per collector)
    - **description**: Updated description text
    - **type**: Change collection type (personal, wishlist, for_sale, showcase)
    - **isPublic**: Toggle privacy setting

    **Important Notes:**
    - Only the collection owner can update it
    - Collection ID and collector cannot be changed
    - Name must remain unique within the collector's collections
    - Changes are immediately reflected in all queries

    **Use Cases:**
    - Rename a collection
    - Change collection visibility
    - Update collection purpose (e.g., personal to for_sale)
    - Add or modify description

    Args:
        collection_id (UUID):
        body (UpdateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateCollectionInput,
) -> Optional[Union[Collection, ErrorResponse]]:
    """Update collection

     Update an existing collection's properties.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to update

    **Updatable Fields:**
    - **name**: New collection name (must be unique per collector)
    - **description**: Updated description text
    - **type**: Change collection type (personal, wishlist, for_sale, showcase)
    - **isPublic**: Toggle privacy setting

    **Important Notes:**
    - Only the collection owner can update it
    - Collection ID and collector cannot be changed
    - Name must remain unique within the collector's collections
    - Changes are immediately reflected in all queries

    **Use Cases:**
    - Rename a collection
    - Change collection visibility
    - Update collection purpose (e.g., personal to for_sale)
    - Add or modify description

    Args:
        collection_id (UUID):
        body (UpdateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateCollectionInput,
) -> Response[Union[Collection, ErrorResponse]]:
    """Update collection

     Update an existing collection's properties.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to update

    **Updatable Fields:**
    - **name**: New collection name (must be unique per collector)
    - **description**: Updated description text
    - **type**: Change collection type (personal, wishlist, for_sale, showcase)
    - **isPublic**: Toggle privacy setting

    **Important Notes:**
    - Only the collection owner can update it
    - Collection ID and collector cannot be changed
    - Name must remain unique within the collector's collections
    - Changes are immediately reflected in all queries

    **Use Cases:**
    - Rename a collection
    - Change collection visibility
    - Update collection purpose (e.g., personal to for_sale)
    - Add or modify description

    Args:
        collection_id (UUID):
        body (UpdateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateCollectionInput,
) -> Optional[Union[Collection, ErrorResponse]]:
    """Update collection

     Update an existing collection's properties.

    **Path Parameters:**
    - **collectionId**: UUID of the collection to update

    **Updatable Fields:**
    - **name**: New collection name (must be unique per collector)
    - **description**: Updated description text
    - **type**: Change collection type (personal, wishlist, for_sale, showcase)
    - **isPublic**: Toggle privacy setting

    **Important Notes:**
    - Only the collection owner can update it
    - Collection ID and collector cannot be changed
    - Name must remain unique within the collector's collections
    - Changes are immediately reflected in all queries

    **Use Cases:**
    - Rename a collection
    - Change collection visibility
    - Update collection purpose (e.g., personal to for_sale)
    - Add or modify description

    Args:
        collection_id (UUID):
        body (UpdateCollectionInput):

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
            body=body,
        )
    ).parsed
