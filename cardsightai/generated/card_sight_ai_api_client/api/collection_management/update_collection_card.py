from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_card import CollectionCard
from ...models.error_response import ErrorResponse
from ...models.update_collection_card_input import UpdateCollectionCardInput
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    card_id: UUID,
    *,
    body: UpdateCollectionCardInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/collection/{collection_id}/cards/{card_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UpdateCollectionCardInput,
) -> Response[Union[CollectionCard, ErrorResponse]]:
    """Update card metadata

     Update collection-specific metadata for a card.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry

    **Updatable Fields:**
    - **quantity**: Adjust number of copies
    - **grade**: Update or add grading info
    - **gradeCompany**: Change grading service
    - **purchasePrice**: Correct purchase price
    - **purchaseDate**: Fix acquisition date
    - **purchaseFrom**: Update source information
    - **condition**: Change raw condition assessment
    - **notes**: Modify personal notes
    - **isForSale**: Toggle sale status
    - **salePrice**: Update asking price
    - **binderId**: Move to different binder

    **Important Notes:**
    - Cannot change the catalog card reference
    - Updates are immediate
    - Previous values are not retained (no history)
    - Only the collection owner can update

    **Use Cases:**
    - Update card after grading
    - Adjust quantities after sales
    - Add or modify notes
    - Change sale status

    Args:
        collection_id (UUID):
        card_id (UUID):
        body (UpdateCollectionCardInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        card_id=card_id,
        body=body,
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
    body: UpdateCollectionCardInput,
) -> Optional[Union[CollectionCard, ErrorResponse]]:
    """Update card metadata

     Update collection-specific metadata for a card.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry

    **Updatable Fields:**
    - **quantity**: Adjust number of copies
    - **grade**: Update or add grading info
    - **gradeCompany**: Change grading service
    - **purchasePrice**: Correct purchase price
    - **purchaseDate**: Fix acquisition date
    - **purchaseFrom**: Update source information
    - **condition**: Change raw condition assessment
    - **notes**: Modify personal notes
    - **isForSale**: Toggle sale status
    - **salePrice**: Update asking price
    - **binderId**: Move to different binder

    **Important Notes:**
    - Cannot change the catalog card reference
    - Updates are immediate
    - Previous values are not retained (no history)
    - Only the collection owner can update

    **Use Cases:**
    - Update card after grading
    - Adjust quantities after sales
    - Add or modify notes
    - Change sale status

    Args:
        collection_id (UUID):
        card_id (UUID):
        body (UpdateCollectionCardInput):

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
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateCollectionCardInput,
) -> Response[Union[CollectionCard, ErrorResponse]]:
    """Update card metadata

     Update collection-specific metadata for a card.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry

    **Updatable Fields:**
    - **quantity**: Adjust number of copies
    - **grade**: Update or add grading info
    - **gradeCompany**: Change grading service
    - **purchasePrice**: Correct purchase price
    - **purchaseDate**: Fix acquisition date
    - **purchaseFrom**: Update source information
    - **condition**: Change raw condition assessment
    - **notes**: Modify personal notes
    - **isForSale**: Toggle sale status
    - **salePrice**: Update asking price
    - **binderId**: Move to different binder

    **Important Notes:**
    - Cannot change the catalog card reference
    - Updates are immediate
    - Previous values are not retained (no history)
    - Only the collection owner can update

    **Use Cases:**
    - Update card after grading
    - Adjust quantities after sales
    - Add or modify notes
    - Change sale status

    Args:
        collection_id (UUID):
        card_id (UUID):
        body (UpdateCollectionCardInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CollectionCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        card_id=card_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    card_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateCollectionCardInput,
) -> Optional[Union[CollectionCard, ErrorResponse]]:
    """Update card metadata

     Update collection-specific metadata for a card.

    **Path Parameters:**
    - **collectionId**: UUID of the collection
    - **cardId**: UUID of the collection card entry

    **Updatable Fields:**
    - **quantity**: Adjust number of copies
    - **grade**: Update or add grading info
    - **gradeCompany**: Change grading service
    - **purchasePrice**: Correct purchase price
    - **purchaseDate**: Fix acquisition date
    - **purchaseFrom**: Update source information
    - **condition**: Change raw condition assessment
    - **notes**: Modify personal notes
    - **isForSale**: Toggle sale status
    - **salePrice**: Update asking price
    - **binderId**: Move to different binder

    **Important Notes:**
    - Cannot change the catalog card reference
    - Updates are immediate
    - Previous values are not retained (no history)
    - Only the collection owner can update

    **Use Cases:**
    - Update card after grading
    - Adjust quantities after sales
    - Add or modify notes
    - Change sale status

    Args:
        collection_id (UUID):
        card_id (UUID):
        body (UpdateCollectionCardInput):

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
            body=body,
        )
    ).parsed
