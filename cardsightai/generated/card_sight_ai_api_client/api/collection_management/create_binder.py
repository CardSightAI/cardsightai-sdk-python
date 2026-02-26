from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.binder import Binder
from ...models.create_binder_input import CreateBinderInput
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    *,
    body: CreateBinderInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/collection/{collection_id}/binders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Binder, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = Binder.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Binder.from_dict(response.json())

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
) -> Response[Union[Binder, ErrorResponse]]:
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
    body: CreateBinderInput,
) -> Response[Union[Binder, ErrorResponse]]:
    r"""Create a binder

     Create a new binder within a collection to organize subsets of cards.

    A binder is a virtual container for grouping cards, similar to physical card binders or pages. Use
    binders to:
    - Organize cards by theme or set
    - Create sale lots or trade packages
    - Build showcase presentations
    - Group cards for specific purposes

    **Binder Properties:**
    - **name**: Descriptive name (e.g., \"1989 Rookies\", \"For Sale - PSA 10s\")
    - **description**: Optional detailed description
    - **type**: Purpose designation (showcase, for_sale, for_trade, organizing)
    - **sortOrder**: Display order within collection
    - **isPublic**: Visibility setting for sharing

    **Important Notes:**
    - Binders belong to a single collection
    - Cards can exist in multiple binders
    - Binder names must be unique within the collection
    - Empty binders are allowed

    **Use Cases:**
    - Create themed showcases
    - Organize cards for sale
    - Build trade packages
    - Separate graded from raw cards

    Args:
        collection_id (UUID):
        body (CreateBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Binder, ErrorResponse]]
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
    body: CreateBinderInput,
) -> Optional[Union[Binder, ErrorResponse]]:
    r"""Create a binder

     Create a new binder within a collection to organize subsets of cards.

    A binder is a virtual container for grouping cards, similar to physical card binders or pages. Use
    binders to:
    - Organize cards by theme or set
    - Create sale lots or trade packages
    - Build showcase presentations
    - Group cards for specific purposes

    **Binder Properties:**
    - **name**: Descriptive name (e.g., \"1989 Rookies\", \"For Sale - PSA 10s\")
    - **description**: Optional detailed description
    - **type**: Purpose designation (showcase, for_sale, for_trade, organizing)
    - **sortOrder**: Display order within collection
    - **isPublic**: Visibility setting for sharing

    **Important Notes:**
    - Binders belong to a single collection
    - Cards can exist in multiple binders
    - Binder names must be unique within the collection
    - Empty binders are allowed

    **Use Cases:**
    - Create themed showcases
    - Organize cards for sale
    - Build trade packages
    - Separate graded from raw cards

    Args:
        collection_id (UUID):
        body (CreateBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Binder, ErrorResponse]
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
    body: CreateBinderInput,
) -> Response[Union[Binder, ErrorResponse]]:
    r"""Create a binder

     Create a new binder within a collection to organize subsets of cards.

    A binder is a virtual container for grouping cards, similar to physical card binders or pages. Use
    binders to:
    - Organize cards by theme or set
    - Create sale lots or trade packages
    - Build showcase presentations
    - Group cards for specific purposes

    **Binder Properties:**
    - **name**: Descriptive name (e.g., \"1989 Rookies\", \"For Sale - PSA 10s\")
    - **description**: Optional detailed description
    - **type**: Purpose designation (showcase, for_sale, for_trade, organizing)
    - **sortOrder**: Display order within collection
    - **isPublic**: Visibility setting for sharing

    **Important Notes:**
    - Binders belong to a single collection
    - Cards can exist in multiple binders
    - Binder names must be unique within the collection
    - Empty binders are allowed

    **Use Cases:**
    - Create themed showcases
    - Organize cards for sale
    - Build trade packages
    - Separate graded from raw cards

    Args:
        collection_id (UUID):
        body (CreateBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Binder, ErrorResponse]]
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
    body: CreateBinderInput,
) -> Optional[Union[Binder, ErrorResponse]]:
    r"""Create a binder

     Create a new binder within a collection to organize subsets of cards.

    A binder is a virtual container for grouping cards, similar to physical card binders or pages. Use
    binders to:
    - Organize cards by theme or set
    - Create sale lots or trade packages
    - Build showcase presentations
    - Group cards for specific purposes

    **Binder Properties:**
    - **name**: Descriptive name (e.g., \"1989 Rookies\", \"For Sale - PSA 10s\")
    - **description**: Optional detailed description
    - **type**: Purpose designation (showcase, for_sale, for_trade, organizing)
    - **sortOrder**: Display order within collection
    - **isPublic**: Visibility setting for sharing

    **Important Notes:**
    - Binders belong to a single collection
    - Cards can exist in multiple binders
    - Binder names must be unique within the collection
    - Empty binders are allowed

    **Use Cases:**
    - Create themed showcases
    - Organize cards for sale
    - Build trade packages
    - Separate graded from raw cards

    Args:
        collection_id (UUID):
        body (CreateBinderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Binder, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
