from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collector import Collector
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collector_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/collectors/{collector_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Collector, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = Collector.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Collector.from_dict(response.json())

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
) -> Response[Union[Collector, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collector_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Collector, ErrorResponse]]:
    """Get a specific collector

     Get details of a specific collector by ID

    Args:
        collector_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collector, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collector_id=collector_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collector_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Collector, ErrorResponse]]:
    """Get a specific collector

     Get details of a specific collector by ID

    Args:
        collector_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collector, ErrorResponse]
    """

    return sync_detailed(
        collector_id=collector_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collector_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Collector, ErrorResponse]]:
    """Get a specific collector

     Get details of a specific collector by ID

    Args:
        collector_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collector, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        collector_id=collector_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collector_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Collector, ErrorResponse]]:
    """Get a specific collector

     Get details of a specific collector by ID

    Args:
        collector_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collector, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            collector_id=collector_id,
            client=client,
        )
    ).parsed
