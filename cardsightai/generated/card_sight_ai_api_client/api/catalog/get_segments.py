from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_segments_is_identifiable import GetSegmentsIsIdentifiable
from ...models.get_segments_order import GetSegmentsOrder
from ...models.get_segments_sort import GetSegmentsSort
from ...models.paginated_segments_response import PaginatedSegmentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSegmentsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSegmentsSort] = UNSET,
    order: Union[Unset, GetSegmentsOrder] = GetSegmentsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["name"] = name

    json_is_identifiable: Union[Unset, str] = UNSET
    if not isinstance(is_identifiable, Unset):
        json_is_identifiable = is_identifiable.value

    params["is_identifiable"] = json_is_identifiable

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
        "url": "/v1/catalog/segments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedSegmentsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedSegmentsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedSegmentsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedSegmentsResponse]]:
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
    is_identifiable: Union[Unset, GetSegmentsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSegmentsSort] = UNSET,
    order: Union[Unset, GetSegmentsOrder] = GetSegmentsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedSegmentsResponse]]:
    """List market segments

     Retrieve a paginated list of market segments (categories) for trading cards. Segments are the
    highest level of organization, representing markets like Baseball, Pokemon, Magic The Gathering,
    etc. Use this endpoint to get available segments for filtering releases or building category
    navigation. Segments can be searched by name and sorted alphabetically. Each segment may contain
    multiple manufacturers and releases.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSegmentsIsIdentifiable]):
        sort (Union[Unset, GetSegmentsSort]):
        order (Union[Unset, GetSegmentsOrder]):  Default: GetSegmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedSegmentsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        name=name,
        is_identifiable=is_identifiable,
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
    is_identifiable: Union[Unset, GetSegmentsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSegmentsSort] = UNSET,
    order: Union[Unset, GetSegmentsOrder] = GetSegmentsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedSegmentsResponse]]:
    """List market segments

     Retrieve a paginated list of market segments (categories) for trading cards. Segments are the
    highest level of organization, representing markets like Baseball, Pokemon, Magic The Gathering,
    etc. Use this endpoint to get available segments for filtering releases or building category
    navigation. Segments can be searched by name and sorted alphabetically. Each segment may contain
    multiple manufacturers and releases.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSegmentsIsIdentifiable]):
        sort (Union[Unset, GetSegmentsSort]):
        order (Union[Unset, GetSegmentsOrder]):  Default: GetSegmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedSegmentsResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
        name=name,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSegmentsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSegmentsSort] = UNSET,
    order: Union[Unset, GetSegmentsOrder] = GetSegmentsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedSegmentsResponse]]:
    """List market segments

     Retrieve a paginated list of market segments (categories) for trading cards. Segments are the
    highest level of organization, representing markets like Baseball, Pokemon, Magic The Gathering,
    etc. Use this endpoint to get available segments for filtering releases or building category
    navigation. Segments can be searched by name and sorted alphabetically. Each segment may contain
    multiple manufacturers and releases.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSegmentsIsIdentifiable]):
        sort (Union[Unset, GetSegmentsSort]):
        order (Union[Unset, GetSegmentsOrder]):  Default: GetSegmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedSegmentsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        name=name,
        is_identifiable=is_identifiable,
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
    is_identifiable: Union[Unset, GetSegmentsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSegmentsSort] = UNSET,
    order: Union[Unset, GetSegmentsOrder] = GetSegmentsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedSegmentsResponse]]:
    """List market segments

     Retrieve a paginated list of market segments (categories) for trading cards. Segments are the
    highest level of organization, representing markets like Baseball, Pokemon, Magic The Gathering,
    etc. Use this endpoint to get available segments for filtering releases or building category
    navigation. Segments can be searched by name and sorted alphabetically. Each segment may contain
    multiple manufacturers and releases.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSegmentsIsIdentifiable]):
        sort (Union[Unset, GetSegmentsSort]):
        order (Union[Unset, GetSegmentsOrder]):  Default: GetSegmentsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedSegmentsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
            name=name,
            is_identifiable=is_identifiable,
            sort=sort,
            order=order,
        )
    ).parsed
