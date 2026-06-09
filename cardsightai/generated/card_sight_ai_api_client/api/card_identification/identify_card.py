from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.file_upload_input import FileUploadInput
from ...models.identify_card_response import IdentifyCardResponse
from ...types import Response


def _get_kwargs(
    *,
    body: FileUploadInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/identify/card",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, IdentifyCardResponse]]:
    if response.status_code == 200:
        response_200 = IdentifyCardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, IdentifyCardResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: FileUploadInput,
) -> Response[Union[ErrorResponse, IdentifyCardResponse]]:
    """Identifies card(s) from the submitted image (automatic segment detection)

     Identify one or more cards from an image. The segment (sport/category) of each card is detected
    automatically, so a single image may contain cards from different segments (e.g., baseball and
    basketball). To force a specific segment, use POST /card/:segment instead. Supports both
    multipart/form-data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size:
    20MB. Supported formats: JPEG, PNG, WebP, HEIF, HEIC.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IdentifyCardResponse]]
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
    body: FileUploadInput,
) -> Optional[Union[ErrorResponse, IdentifyCardResponse]]:
    """Identifies card(s) from the submitted image (automatic segment detection)

     Identify one or more cards from an image. The segment (sport/category) of each card is detected
    automatically, so a single image may contain cards from different segments (e.g., baseball and
    basketball). To force a specific segment, use POST /card/:segment instead. Supports both
    multipart/form-data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size:
    20MB. Supported formats: JPEG, PNG, WebP, HEIF, HEIC.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IdentifyCardResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FileUploadInput,
) -> Response[Union[ErrorResponse, IdentifyCardResponse]]:
    """Identifies card(s) from the submitted image (automatic segment detection)

     Identify one or more cards from an image. The segment (sport/category) of each card is detected
    automatically, so a single image may contain cards from different segments (e.g., baseball and
    basketball). To force a specific segment, use POST /card/:segment instead. Supports both
    multipart/form-data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size:
    20MB. Supported formats: JPEG, PNG, WebP, HEIF, HEIC.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, IdentifyCardResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FileUploadInput,
) -> Optional[Union[ErrorResponse, IdentifyCardResponse]]:
    """Identifies card(s) from the submitted image (automatic segment detection)

     Identify one or more cards from an image. The segment (sport/category) of each card is detected
    automatically, so a single image may contain cards from different segments (e.g., baseball and
    basketball). To force a specific segment, use POST /card/:segment instead. Supports both
    multipart/form-data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size:
    20MB. Supported formats: JPEG, PNG, WebP, HEIF, HEIC.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, IdentifyCardResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
