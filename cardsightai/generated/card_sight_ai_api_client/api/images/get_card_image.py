from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_card_image_default import GetCardImageDefault
from ...models.get_card_image_format import GetCardImageFormat
from ...models.image_json_response import ImageJsonResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    format_: Union[Unset, GetCardImageFormat] = GetCardImageFormat.RAW,
    default: Union[Unset, GetCardImageDefault] = GetCardImageDefault.FALSE,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_default: Union[Unset, str] = UNSET
    if not isinstance(default, Unset):
        json_default = default.value

    params["default"] = json_default

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/images/cards/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ImageJsonResponse]]:
    if response.status_code == 200:
        response_200 = ImageJsonResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ImageJsonResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetCardImageFormat] = GetCardImageFormat.RAW,
    default: Union[Unset, GetCardImageDefault] = GetCardImageDefault.FALSE,
) -> Response[Union[ErrorResponse, ImageJsonResponse]]:
    """Get card image

     Retrieve a card image by ID. Returns either raw JPEG (format=raw) or JSON with base64 data
    (format=json).

    Args:
        id (UUID):
        format_ (Union[Unset, GetCardImageFormat]):  Default: GetCardImageFormat.RAW.
        default (Union[Unset, GetCardImageDefault]):  Default: GetCardImageDefault.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ImageJsonResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
        default=default,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetCardImageFormat] = GetCardImageFormat.RAW,
    default: Union[Unset, GetCardImageDefault] = GetCardImageDefault.FALSE,
) -> Optional[Union[ErrorResponse, ImageJsonResponse]]:
    """Get card image

     Retrieve a card image by ID. Returns either raw JPEG (format=raw) or JSON with base64 data
    (format=json).

    Args:
        id (UUID):
        format_ (Union[Unset, GetCardImageFormat]):  Default: GetCardImageFormat.RAW.
        default (Union[Unset, GetCardImageDefault]):  Default: GetCardImageDefault.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ImageJsonResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
        default=default,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetCardImageFormat] = GetCardImageFormat.RAW,
    default: Union[Unset, GetCardImageDefault] = GetCardImageDefault.FALSE,
) -> Response[Union[ErrorResponse, ImageJsonResponse]]:
    """Get card image

     Retrieve a card image by ID. Returns either raw JPEG (format=raw) or JSON with base64 data
    (format=json).

    Args:
        id (UUID):
        format_ (Union[Unset, GetCardImageFormat]):  Default: GetCardImageFormat.RAW.
        default (Union[Unset, GetCardImageDefault]):  Default: GetCardImageDefault.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ImageJsonResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
        default=default,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    format_: Union[Unset, GetCardImageFormat] = GetCardImageFormat.RAW,
    default: Union[Unset, GetCardImageDefault] = GetCardImageDefault.FALSE,
) -> Optional[Union[ErrorResponse, ImageJsonResponse]]:
    """Get card image

     Retrieve a card image by ID. Returns either raw JPEG (format=raw) or JSON with base64 data
    (format=json).

    Args:
        id (UUID):
        format_ (Union[Unset, GetCardImageFormat]):  Default: GetCardImageFormat.RAW.
        default (Union[Unset, GetCardImageDefault]):  Default: GetCardImageDefault.FALSE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ImageJsonResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
            default=default,
        )
    ).parsed
