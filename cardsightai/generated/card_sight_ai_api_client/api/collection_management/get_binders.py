from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_binders_order import GetBindersOrder
from ...models.get_binders_sort import GetBindersSort
from ...models.paginated_binders_response import PaginatedBindersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: UUID,
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetBindersSort] = UNSET,
    order: Union[Unset, GetBindersOrder] = GetBindersOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["name"] = name

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/binders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedBindersResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedBindersResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedBindersResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedBindersResponse]]:
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
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetBindersSort] = UNSET,
    order: Union[Unset, GetBindersOrder] = GetBindersOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedBindersResponse]]:
    """List collection binders

     Retrieve all binders within a specific collection with pagination and filtering.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **type**: Filter by binder type (showcase, for_sale, for_trade, organizing)
    - **isPublic**: Filter by visibility (true/false)
    - **sortBy**: Sort field (name, createdAt, cardCount, sortOrder)
    - **sortOrder**: asc or desc (default: asc)

    **Response includes:**
    - Binder metadata (name, type, description)
    - Card count per binder
    - Creation and update timestamps
    - Pagination metadata

    **Use Cases:**
    - Display binder overview
    - Navigate collection structure
    - Find specific binder types
    - Generate binder statistics

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        sort (Union[Unset, GetBindersSort]):
        order (Union[Unset, GetBindersOrder]):  Default: GetBindersOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedBindersResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        name=name,
        sort=sort,
        order=order,
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
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetBindersSort] = UNSET,
    order: Union[Unset, GetBindersOrder] = GetBindersOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedBindersResponse]]:
    """List collection binders

     Retrieve all binders within a specific collection with pagination and filtering.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **type**: Filter by binder type (showcase, for_sale, for_trade, organizing)
    - **isPublic**: Filter by visibility (true/false)
    - **sortBy**: Sort field (name, createdAt, cardCount, sortOrder)
    - **sortOrder**: asc or desc (default: asc)

    **Response includes:**
    - Binder metadata (name, type, description)
    - Card count per binder
    - Creation and update timestamps
    - Pagination metadata

    **Use Cases:**
    - Display binder overview
    - Navigate collection structure
    - Find specific binder types
    - Generate binder statistics

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        sort (Union[Unset, GetBindersSort]):
        order (Union[Unset, GetBindersOrder]):  Default: GetBindersOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedBindersResponse]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        take=take,
        skip=skip,
        name=name,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetBindersSort] = UNSET,
    order: Union[Unset, GetBindersOrder] = GetBindersOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedBindersResponse]]:
    """List collection binders

     Retrieve all binders within a specific collection with pagination and filtering.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **type**: Filter by binder type (showcase, for_sale, for_trade, organizing)
    - **isPublic**: Filter by visibility (true/false)
    - **sortBy**: Sort field (name, createdAt, cardCount, sortOrder)
    - **sortOrder**: asc or desc (default: asc)

    **Response includes:**
    - Binder metadata (name, type, description)
    - Card count per binder
    - Creation and update timestamps
    - Pagination metadata

    **Use Cases:**
    - Display binder overview
    - Navigate collection structure
    - Find specific binder types
    - Generate binder statistics

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        sort (Union[Unset, GetBindersSort]):
        order (Union[Unset, GetBindersOrder]):  Default: GetBindersOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedBindersResponse]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        take=take,
        skip=skip,
        name=name,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetBindersSort] = UNSET,
    order: Union[Unset, GetBindersOrder] = GetBindersOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedBindersResponse]]:
    """List collection binders

     Retrieve all binders within a specific collection with pagination and filtering.

    **Path Parameters:**
    - **collectionId**: UUID of the parent collection

    **Query Parameters:**
    - **page**: Page number (default: 1)
    - **limit**: Items per page (default: 20, max: 100)
    - **type**: Filter by binder type (showcase, for_sale, for_trade, organizing)
    - **isPublic**: Filter by visibility (true/false)
    - **sortBy**: Sort field (name, createdAt, cardCount, sortOrder)
    - **sortOrder**: asc or desc (default: asc)

    **Response includes:**
    - Binder metadata (name, type, description)
    - Card count per binder
    - Creation and update timestamps
    - Pagination metadata

    **Use Cases:**
    - Display binder overview
    - Navigate collection structure
    - Find specific binder types
    - Generate binder statistics

    Args:
        collection_id (UUID):
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        sort (Union[Unset, GetBindersSort]):
        order (Union[Unset, GetBindersOrder]):  Default: GetBindersOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedBindersResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            take=take,
            skip=skip,
            name=name,
            sort=sort,
            order=order,
        )
    ).parsed
