from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.create_collection_input import CreateCollectionInput
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCollectionInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collection/",
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
    *,
    client: AuthenticatedClient,
    body: CreateCollectionInput,
) -> Response[Union[Collection, ErrorResponse]]:
    r"""Create a new collection

     Create a new collection for organizing trading cards.

    A collection is a container for organizing cards, similar to a physical binder or box. Each
    collection belongs to a specific collector and can be customized with:
    - A descriptive name
    - Type designation (personal, wishlist, for_sale, showcase)
    - Privacy settings (public or private)
    - Optional description

    **Use Cases:**
    - Organize cards by theme (e.g., \"1990s Rookies\", \"Hall of Famers\")
    - Track different collection goals (wishlist vs owned)
    - Separate cards for sale from personal collection
    - Create showcases of prized cards

    **Important Notes:**
    - Collections are isolated by API key (multi-tenant)
    - Each collector can have multiple collections
    - Collection names must be unique per collector

    Args:
        body (CreateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateCollectionInput,
) -> Optional[Union[Collection, ErrorResponse]]:
    r"""Create a new collection

     Create a new collection for organizing trading cards.

    A collection is a container for organizing cards, similar to a physical binder or box. Each
    collection belongs to a specific collector and can be customized with:
    - A descriptive name
    - Type designation (personal, wishlist, for_sale, showcase)
    - Privacy settings (public or private)
    - Optional description

    **Use Cases:**
    - Organize cards by theme (e.g., \"1990s Rookies\", \"Hall of Famers\")
    - Track different collection goals (wishlist vs owned)
    - Separate cards for sale from personal collection
    - Create showcases of prized cards

    **Important Notes:**
    - Collections are isolated by API key (multi-tenant)
    - Each collector can have multiple collections
    - Collection names must be unique per collector

    Args:
        body (CreateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCollectionInput,
) -> Response[Union[Collection, ErrorResponse]]:
    r"""Create a new collection

     Create a new collection for organizing trading cards.

    A collection is a container for organizing cards, similar to a physical binder or box. Each
    collection belongs to a specific collector and can be customized with:
    - A descriptive name
    - Type designation (personal, wishlist, for_sale, showcase)
    - Privacy settings (public or private)
    - Optional description

    **Use Cases:**
    - Organize cards by theme (e.g., \"1990s Rookies\", \"Hall of Famers\")
    - Track different collection goals (wishlist vs owned)
    - Separate cards for sale from personal collection
    - Create showcases of prized cards

    **Important Notes:**
    - Collections are isolated by API key (multi-tenant)
    - Each collector can have multiple collections
    - Collection names must be unique per collector

    Args:
        body (CreateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCollectionInput,
) -> Optional[Union[Collection, ErrorResponse]]:
    r"""Create a new collection

     Create a new collection for organizing trading cards.

    A collection is a container for organizing cards, similar to a physical binder or box. Each
    collection belongs to a specific collector and can be customized with:
    - A descriptive name
    - Type designation (personal, wishlist, for_sale, showcase)
    - Privacy settings (public or private)
    - Optional description

    **Use Cases:**
    - Organize cards by theme (e.g., \"1990s Rookies\", \"Hall of Famers\")
    - Track different collection goals (wishlist vs owned)
    - Separate cards for sale from personal collection
    - Create showcases of prized cards

    **Important Notes:**
    - Collections are isolated by API key (multi-tenant)
    - Each collector can have multiple collections
    - Collection names must be unique per collector

    Args:
        body (CreateCollectionInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
