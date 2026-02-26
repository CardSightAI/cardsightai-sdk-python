from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    card_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collection/{collection_id}/cards/{card_id}/image",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
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
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get collection card image

     Retrieve the full-resolution image added for the specified card within the collection.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get collection card image

     Retrieve the full-resolution image added for the specified card within the collection.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
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
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get collection card image

     Retrieve the full-resolution image added for the specified card within the collection.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get collection card image

     Retrieve the full-resolution image added for the specified card within the collection.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            card_id=card_id,
            client=client,
        )
    ).parsed
