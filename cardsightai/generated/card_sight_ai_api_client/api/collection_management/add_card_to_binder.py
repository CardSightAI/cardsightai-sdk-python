from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_card_to_binder_input import AddCardToBinderInput
from ...models.binder_card import BinderCard
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    binder_id: UUID,
    *,
    body: AddCardToBinderInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/collection/{collection_id}/binders/{binder_id}/cards",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BinderCard, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = BinderCard.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BinderCard, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AddCardToBinderInput,
) -> Response[Union[BinderCard, ErrorResponse]]:
    """Add card to binder

     Add an existing collection card to a binder for organization.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the target binder

    **Request Body:**
    - **collectionCardId**: UUID of the collection card to add
    - **sortOrder**: Optional display order within binder
    - **notes**: Optional binder-specific notes

    **Important Notes:**
    - Card must already exist in the collection
    - Same card can be in multiple binders
    - Does not duplicate the card, just creates a link
    - Original card metadata is preserved

    **Use Cases:**
    - Organize cards into themed binders
    - Create sale or trade lots
    - Build showcases
    - Group cards for specific purposes

    Args:
        collection_id (UUID):
        binder_id (UUID):
        body (AddCardToBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BinderCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AddCardToBinderInput,
) -> Optional[Union[BinderCard, ErrorResponse]]:
    """Add card to binder

     Add an existing collection card to a binder for organization.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the target binder

    **Request Body:**
    - **collectionCardId**: UUID of the collection card to add
    - **sortOrder**: Optional display order within binder
    - **notes**: Optional binder-specific notes

    **Important Notes:**
    - Card must already exist in the collection
    - Same card can be in multiple binders
    - Does not duplicate the card, just creates a link
    - Original card metadata is preserved

    **Use Cases:**
    - Organize cards into themed binders
    - Create sale or trade lots
    - Build showcases
    - Group cards for specific purposes

    Args:
        collection_id (UUID):
        binder_id (UUID):
        body (AddCardToBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BinderCard, ErrorResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        binder_id=binder_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AddCardToBinderInput,
) -> Response[Union[BinderCard, ErrorResponse]]:
    """Add card to binder

     Add an existing collection card to a binder for organization.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the target binder

    **Request Body:**
    - **collectionCardId**: UUID of the collection card to add
    - **sortOrder**: Optional display order within binder
    - **notes**: Optional binder-specific notes

    **Important Notes:**
    - Card must already exist in the collection
    - Same card can be in multiple binders
    - Does not duplicate the card, just creates a link
    - Original card metadata is preserved

    **Use Cases:**
    - Organize cards into themed binders
    - Create sale or trade lots
    - Build showcases
    - Group cards for specific purposes

    Args:
        collection_id (UUID):
        binder_id (UUID):
        body (AddCardToBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BinderCard, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    body: AddCardToBinderInput,
) -> Optional[Union[BinderCard, ErrorResponse]]:
    """Add card to binder

     Add an existing collection card to a binder for organization.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the target binder

    **Request Body:**
    - **collectionCardId**: UUID of the collection card to add
    - **sortOrder**: Optional display order within binder
    - **notes**: Optional binder-specific notes

    **Important Notes:**
    - Card must already exist in the collection
    - Same card can be in multiple binders
    - Does not duplicate the card, just creates a link
    - Original card metadata is preserved

    **Use Cases:**
    - Organize cards into themed binders
    - Create sale or trade lots
    - Build showcases
    - Group cards for specific purposes

    Args:
        collection_id (UUID):
        binder_id (UUID):
        body (AddCardToBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BinderCard, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            binder_id=binder_id,
            client=client,
            body=body,
        )
    ).parsed
