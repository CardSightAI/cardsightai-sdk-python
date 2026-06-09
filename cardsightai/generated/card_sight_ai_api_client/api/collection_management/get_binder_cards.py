from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.paginated_binder_cards_response import PaginatedBinderCardsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: UUID,
    binder_id: UUID,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/binders/{binder_id}/cards",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedBinderCardsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedBinderCardsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
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
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
    """List binder cards

     Retrieve all cards organized within a specific binder.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, sortOrder)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names

    **Response includes:**
    - Full card details from catalog
    - Collection-specific metadata
    - Binder-specific sort order
    - Pagination metadata

    **Use Cases:**
    - View binder contents
    - Generate binder listings
    - Export binder inventory

    Args:
        collection_id (UUID):
        binder_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedBinderCardsResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        take=take,
        skip=skip,
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
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
    """List binder cards

     Retrieve all cards organized within a specific binder.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, sortOrder)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names

    **Response includes:**
    - Full card details from catalog
    - Collection-specific metadata
    - Binder-specific sort order
    - Pagination metadata

    **Use Cases:**
    - View binder contents
    - Generate binder listings
    - Export binder inventory

    Args:
        collection_id (UUID):
        binder_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedBinderCardsResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        binder_id=binder_id,
        client=client,
        take=take,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Response[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
    """List binder cards

     Retrieve all cards organized within a specific binder.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, sortOrder)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names

    **Response includes:**
    - Full card details from catalog
    - Collection-specific metadata
    - Binder-specific sort order
    - Pagination metadata

    **Use Cases:**
    - View binder contents
    - Generate binder listings
    - Export binder inventory

    Args:
        collection_id (UUID):
        binder_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedBinderCardsResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        binder_id=binder_id,
        take=take,
        skip=skip,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    binder_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
) -> Optional[Union[ErrorResponse, PaginatedBinderCardsResponse]]:
    """List binder cards

     Retrieve all cards organized within a specific binder.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection
    - **binderId**: UUID of the binder

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **sortBy**: Sort field (name, number, sortOrder)
    - **sortOrder**: asc or desc (default: asc)
    - **search**: Search card names

    **Response includes:**
    - Full card details from catalog
    - Collection-specific metadata
    - Binder-specific sort order
    - Pagination metadata

    **Use Cases:**
    - View binder contents
    - Generate binder listings
    - Export binder inventory

    Args:
        collection_id (UUID):
        binder_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedBinderCardsResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            binder_id=binder_id,
            client=client,
            take=take,
            skip=skip,
        )
    ).parsed
