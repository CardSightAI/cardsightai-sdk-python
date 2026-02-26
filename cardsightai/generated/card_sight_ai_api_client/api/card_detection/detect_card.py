from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detect_card_response import DetectCardResponse
from ...models.error_response import ErrorResponse
from ...models.file_upload_input import FileUploadInput
from ...types import Response


def _get_kwargs(
    *,
    body: FileUploadInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/detect/card",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DetectCardResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DetectCardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

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
) -> Response[Union[DetectCardResponse, ErrorResponse]]:
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
) -> Response[Union[DetectCardResponse, ErrorResponse]]:
    """Detect trading card presence in an image

     Checks whether one or more trading cards are present in the submitted image. Returns a boolean
    detected flag and card count. Does not identify or catalog the cards. Supports both multipart/form-
    data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size: 20MB.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DetectCardResponse, ErrorResponse]]
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
) -> Optional[Union[DetectCardResponse, ErrorResponse]]:
    """Detect trading card presence in an image

     Checks whether one or more trading cards are present in the submitted image. Returns a boolean
    detected flag and card count. Does not identify or catalog the cards. Supports both multipart/form-
    data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size: 20MB.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DetectCardResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FileUploadInput,
) -> Response[Union[DetectCardResponse, ErrorResponse]]:
    """Detect trading card presence in an image

     Checks whether one or more trading cards are present in the submitted image. Returns a boolean
    detected flag and card count. Does not identify or catalog the cards. Supports both multipart/form-
    data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size: 20MB.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DetectCardResponse, ErrorResponse]]
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
) -> Optional[Union[DetectCardResponse, ErrorResponse]]:
    """Detect trading card presence in an image

     Checks whether one or more trading cards are present in the submitted image. Returns a boolean
    detected flag and card count. Does not identify or catalog the cards. Supports both multipart/form-
    data and direct binary upload (image/jpeg, image/png, image/webp). Maximum file size: 20MB.

    Args:
        body (FileUploadInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DetectCardResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
