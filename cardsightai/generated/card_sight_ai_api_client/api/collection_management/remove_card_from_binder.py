from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    binder_id: UUID,
    card_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/collection/{collection_id}/binders/{binder_id}/cards/{card_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    binder_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse]]:
    """Remove card from binder

     Remove a card's association with a binder without deleting it from the collection.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder
    - **cardId**: UUID of the binder-card association

    **Important Notes:**
    - Only removes the binder link, not the card itself
    - Card remains in the collection
    - Card can still be in other binders
    - This is reversible (card can be re-added)

    **Use Cases:**
    - Reorganize binder contents
    - Remove sold cards from sale binder
    - Clean up binder organization
    - Move cards between binders

    **Response:**
    - 204 No Content on success
    - No response body

    Args:
        collection_id (UUID):
        binder_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        card_id=card_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    binder_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse]]:
    """Remove card from binder

     Remove a card's association with a binder without deleting it from the collection.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder
    - **cardId**: UUID of the binder-card association

    **Important Notes:**
    - Only removes the binder link, not the card itself
    - Card remains in the collection
    - Card can still be in other binders
    - This is reversible (card can be re-added)

    **Use Cases:**
    - Reorganize binder contents
    - Remove sold cards from sale binder
    - Clean up binder organization
    - Move cards between binders

    **Response:**
    - 204 No Content on success
    - No response body

    Args:
        collection_id (UUID):
        binder_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        binder_id=binder_id,
        card_id=card_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    binder_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse]]:
    """Remove card from binder

     Remove a card's association with a binder without deleting it from the collection.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder
    - **cardId**: UUID of the binder-card association

    **Important Notes:**
    - Only removes the binder link, not the card itself
    - Card remains in the collection
    - Card can still be in other binders
    - This is reversible (card can be re-added)

    **Use Cases:**
    - Reorganize binder contents
    - Remove sold cards from sale binder
    - Clean up binder organization
    - Move cards between binders

    **Response:**
    - 204 No Content on success
    - No response body

    Args:
        collection_id (UUID):
        binder_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        card_id=card_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    binder_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse]]:
    """Remove card from binder

     Remove a card's association with a binder without deleting it from the collection.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder
    - **cardId**: UUID of the binder-card association

    **Important Notes:**
    - Only removes the binder link, not the card itself
    - Card remains in the collection
    - Card can still be in other binders
    - This is reversible (card can be re-added)

    **Use Cases:**
    - Reorganize binder contents
    - Remove sold cards from sale binder
    - Clean up binder organization
    - Move cards between binders

    **Response:**
    - 204 No Content on success
    - No response body

    Args:
        collection_id (UUID):
        binder_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            binder_id=binder_id,
            card_id=card_id,
            client=client,
        )
    ).parsed
