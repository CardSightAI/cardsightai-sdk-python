from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_collection_card_image_response import UploadCollectionCardImageResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    card_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/collection/{collection_id}/cards/{card_id}/image",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UploadCollectionCardImageResponse]:
    if response.status_code == 200:
        response_200 = UploadCollectionCardImageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UploadCollectionCardImageResponse]:
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
) -> Response[UploadCollectionCardImageResponse]:
    """Upload collection card image

     Upload a photo of a card in your collection. Maximum file size: 2MB. Accepts JPEG, PNG, WebP, and
    HEIC formats.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadCollectionCardImageResponse]
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
) -> Optional[UploadCollectionCardImageResponse]:
    """Upload collection card image

     Upload a photo of a card in your collection. Maximum file size: 2MB. Accepts JPEG, PNG, WebP, and
    HEIC formats.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadCollectionCardImageResponse
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
) -> Response[UploadCollectionCardImageResponse]:
    """Upload collection card image

     Upload a photo of a card in your collection. Maximum file size: 2MB. Accepts JPEG, PNG, WebP, and
    HEIC formats.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadCollectionCardImageResponse]
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
) -> Optional[UploadCollectionCardImageResponse]:
    """Upload collection card image

     Upload a photo of a card in your collection. Maximum file size: 2MB. Accepts JPEG, PNG, WebP, and
    HEIC formats.

    Args:
        collection_id (UUID):
        card_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadCollectionCardImageResponse
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            card_id=card_id,
            client=client,
        )
    ).parsed
