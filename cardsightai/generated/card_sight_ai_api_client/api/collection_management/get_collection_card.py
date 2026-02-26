from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_card import CollectionCard
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    card_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/cards/{card_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CollectionCard, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CollectionCard.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CollectionCard.from_dict(response.json())

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
) -> Response[Union[CollectionCard, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CollectionCard, ErrorResponse]]:
    """Get card details

     Retrieve complete details for a specific card in a collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry (not the catalog card ID)

    **Response includes:**
    - Complete catalog card information
    - All collection-specific metadata
    - Purchase and sale information
    - Grading details if applicable
    - Current market value
    - Historical price data (if available)
    - Personal notes

    **Use Cases:**
    - View full card details
    - Check card value and grade
    - Review purchase history
    - Prepare for sale listing

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        card_id=card_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CollectionCard, ErrorResponse]]:
    """Get card details

     Retrieve complete details for a specific card in a collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry (not the catalog card ID)

    **Response includes:**
    - Complete catalog card information
    - All collection-specific metadata
    - Purchase and sale information
    - Grading details if applicable
    - Current market value
    - Historical price data (if available)
    - Personal notes

    **Use Cases:**
    - View full card details
    - Check card value and grade
    - Review purchase history
    - Prepare for sale listing

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CollectionCard, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        card_id=card_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CollectionCard, ErrorResponse]]:
    """Get card details

     Retrieve complete details for a specific card in a collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry (not the catalog card ID)

    **Response includes:**
    - Complete catalog card information
    - All collection-specific metadata
    - Purchase and sale information
    - Grading details if applicable
    - Current market value
    - Historical price data (if available)
    - Personal notes

    **Use Cases:**
    - View full card details
    - Check card value and grade
    - Review purchase history
    - Prepare for sale listing

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        card_id=card_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CollectionCard, ErrorResponse]]:
    """Get card details

     Retrieve complete details for a specific card in a collection.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry (not the catalog card ID)

    **Response includes:**
    - Complete catalog card information
    - All collection-specific metadata
    - Purchase and sale information
    - Grading details if applicable
    - Current market value
    - Historical price data (if available)
    - Personal notes

    **Use Cases:**
    - View full card details
    - Check card value and grade
    - Review purchase history
    - Prepare for sale listing

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CollectionCard, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            card_id=card_id,
            client=client,
        )
    ).parsed
