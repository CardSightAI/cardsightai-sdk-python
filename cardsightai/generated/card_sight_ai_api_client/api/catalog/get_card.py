from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_card_response import DetailedCardResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/catalog/cards/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DetailedCardResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DetailedCardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = DetailedCardResponse.from_dict(response.json())

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
) -> Response[Union[DetailedCardResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DetailedCardResponse, ErrorResponse]]:
    """Get complete card details

     Retrieve comprehensive information about a specific card including its release, set, attributes, and
    available parallel variants. Returns full card details with contextual information about where it
    belongs in the catalog hierarchy. Includes a count of parallel versions available and all attributes
    (Rookie, Autograph, etc.) associated with the card. Use this endpoint for detailed card views,
    collection management, or when you need complete card information.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DetailedCardResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DetailedCardResponse, ErrorResponse]]:
    """Get complete card details

     Retrieve comprehensive information about a specific card including its release, set, attributes, and
    available parallel variants. Returns full card details with contextual information about where it
    belongs in the catalog hierarchy. Includes a count of parallel versions available and all attributes
    (Rookie, Autograph, etc.) associated with the card. Use this endpoint for detailed card views,
    collection management, or when you need complete card information.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DetailedCardResponse, ErrorResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DetailedCardResponse, ErrorResponse]]:
    """Get complete card details

     Retrieve comprehensive information about a specific card including its release, set, attributes, and
    available parallel variants. Returns full card details with contextual information about where it
    belongs in the catalog hierarchy. Includes a count of parallel versions available and all attributes
    (Rookie, Autograph, etc.) associated with the card. Use this endpoint for detailed card views,
    collection management, or when you need complete card information.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DetailedCardResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DetailedCardResponse, ErrorResponse]]:
    """Get complete card details

     Retrieve comprehensive information about a specific card including its release, set, attributes, and
    available parallel variants. Returns full card details with contextual information about where it
    belongs in the catalog hierarchy. Includes a count of parallel versions available and all attributes
    (Rookie, Autograph, etc.) associated with the card. Use this endpoint for detailed card views,
    collection management, or when you need complete card information.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DetailedCardResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
