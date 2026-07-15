from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_parallels_order import GetParallelsOrder
from ...models.get_parallels_sort import GetParallelsSort
from ...models.paginated_parallels_response import PaginatedParallelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetParallelsSort] = UNSET,
    order: Union[Unset, GetParallelsOrder] = GetParallelsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["name"] = name

    params["releaseId"] = release_id

    params["releaseName"] = release_name

    params["year"] = year

    params["min_year"] = min_year

    params["max_year"] = max_year

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/parallels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedParallelsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedParallelsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedParallelsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedParallelsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetParallelsSort] = UNSET,
    order: Union[Unset, GetParallelsOrder] = GetParallelsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedParallelsResponse]]:
    """Search for parallels across sets and releases (free)

     Search for parallels by name and filter by release. Returns all sets containing the parallel with
    release information

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        sort (Union[Unset, GetParallelsSort]):
        order (Union[Unset, GetParallelsOrder]):  Default: GetParallelsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedParallelsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        name=name,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetParallelsSort] = UNSET,
    order: Union[Unset, GetParallelsOrder] = GetParallelsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedParallelsResponse]]:
    """Search for parallels across sets and releases (free)

     Search for parallels by name and filter by release. Returns all sets containing the parallel with
    release information

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        sort (Union[Unset, GetParallelsSort]):
        order (Union[Unset, GetParallelsOrder]):  Default: GetParallelsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedParallelsResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
        name=name,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetParallelsSort] = UNSET,
    order: Union[Unset, GetParallelsOrder] = GetParallelsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedParallelsResponse]]:
    """Search for parallels across sets and releases (free)

     Search for parallels by name and filter by release. Returns all sets containing the parallel with
    release information

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        sort (Union[Unset, GetParallelsSort]):
        order (Union[Unset, GetParallelsOrder]):  Default: GetParallelsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedParallelsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        name=name,
        release_id=release_id,
        release_name=release_name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    release_id: Union[Unset, str] = UNSET,
    release_name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    sort: Union[Unset, GetParallelsSort] = UNSET,
    order: Union[Unset, GetParallelsOrder] = GetParallelsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedParallelsResponse]]:
    """Search for parallels across sets and releases (free)

     Search for parallels by name and filter by release. Returns all sets containing the parallel with
    release information

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        release_id (Union[Unset, str]):
        release_name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        sort (Union[Unset, GetParallelsSort]):
        order (Union[Unset, GetParallelsOrder]):  Default: GetParallelsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedParallelsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
            name=name,
            release_id=release_id,
            release_name=release_name,
            year=year,
            min_year=min_year,
            max_year=max_year,
            sort=sort,
            order=order,
        )
    ).parsed
