from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.autocomplete_response import AutocompleteResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    segment_id: Union[Unset, str] = UNSET,
    manufacturer_id: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["segmentId"] = segment_id

    params["manufacturerId"] = manufacturer_id

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/autocomplete/releases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AutocompleteResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AutocompleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = AutocompleteResponse.from_dict(response.json())

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
) -> Response[Union[AutocompleteResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    segment_id: Union[Unset, str] = UNSET,
    manufacturer_id: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
) -> Response[Union[AutocompleteResponse, ErrorResponse]]:
    """Release name autocomplete

     Get release name suggestions for autocomplete. Can filter by segment, manufacturer, and/or year.
    Returns up to 10 matching release names sorted alphabetically.

    Args:
        q (str):
        segment_id (Union[Unset, str]):
        manufacturer_id (Union[Unset, str]):
        year (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AutocompleteResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        segment_id=segment_id,
        manufacturer_id=manufacturer_id,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    segment_id: Union[Unset, str] = UNSET,
    manufacturer_id: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
) -> Optional[Union[AutocompleteResponse, ErrorResponse]]:
    """Release name autocomplete

     Get release name suggestions for autocomplete. Can filter by segment, manufacturer, and/or year.
    Returns up to 10 matching release names sorted alphabetically.

    Args:
        q (str):
        segment_id (Union[Unset, str]):
        manufacturer_id (Union[Unset, str]):
        year (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AutocompleteResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        q=q,
        segment_id=segment_id,
        manufacturer_id=manufacturer_id,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    segment_id: Union[Unset, str] = UNSET,
    manufacturer_id: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
) -> Response[Union[AutocompleteResponse, ErrorResponse]]:
    """Release name autocomplete

     Get release name suggestions for autocomplete. Can filter by segment, manufacturer, and/or year.
    Returns up to 10 matching release names sorted alphabetically.

    Args:
        q (str):
        segment_id (Union[Unset, str]):
        manufacturer_id (Union[Unset, str]):
        year (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AutocompleteResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        segment_id=segment_id,
        manufacturer_id=manufacturer_id,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    segment_id: Union[Unset, str] = UNSET,
    manufacturer_id: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
) -> Optional[Union[AutocompleteResponse, ErrorResponse]]:
    """Release name autocomplete

     Get release name suggestions for autocomplete. Can filter by segment, manufacturer, and/or year.
    Returns up to 10 matching release names sorted alphabetically.

    Args:
        q (str):
        segment_id (Union[Unset, str]):
        manufacturer_id (Union[Unset, str]):
        year (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AutocompleteResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            segment_id=segment_id,
            manufacturer_id=manufacturer_id,
            year=year,
        )
    ).parsed
