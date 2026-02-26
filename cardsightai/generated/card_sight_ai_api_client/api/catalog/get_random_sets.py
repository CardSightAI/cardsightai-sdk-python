from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_random_sets_is_identifiable import GetRandomSetsIsIdentifiable
from ...models.get_random_sets_order import GetRandomSetsOrder
from ...models.get_random_sets_sort import GetRandomSetsSort
from ...models.random_sets_response import RandomSetsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomSetsSort] = UNSET,
    order: Union[Unset, GetRandomSetsOrder] = GetRandomSetsOrder.ASC,
    count: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["releaseId"] = release_id

    params["name"] = name

    params["year"] = year

    params["min_year"] = min_year

    params["max_year"] = max_year

    params["manufacturer"] = manufacturer

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

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/sets/random",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, RandomSetsResponse]]:
    if response.status_code == 200:
        response_200 = RandomSetsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RandomSetsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, RandomSetsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomSetsSort] = UNSET,
    order: Union[Unset, GetRandomSetsOrder] = GetRandomSetsOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, RandomSetsResponse]]:
    """Get random sets matching filters

     Returns random sets instead of paginated sorted results. Useful for discovery features or showcasing
    catalog variety. Supports all standard set filters including release, year range, manufacturer, and
    name search. Each set includes its release context and card/parallel counts. If count exceeds
    available matching sets, returns all available sets.

    Args:
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomSetsIsIdentifiable]):
        sort (Union[Unset, GetRandomSetsSort]):
        order (Union[Unset, GetRandomSetsOrder]):  Default: GetRandomSetsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomSetsResponse]]
    """

    kwargs = _get_kwargs(
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomSetsSort] = UNSET,
    order: Union[Unset, GetRandomSetsOrder] = GetRandomSetsOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, RandomSetsResponse]]:
    """Get random sets matching filters

     Returns random sets instead of paginated sorted results. Useful for discovery features or showcasing
    catalog variety. Supports all standard set filters including release, year range, manufacturer, and
    name search. Each set includes its release context and card/parallel counts. If count exceeds
    available matching sets, returns all available sets.

    Args:
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomSetsIsIdentifiable]):
        sort (Union[Unset, GetRandomSetsSort]):
        order (Union[Unset, GetRandomSetsOrder]):  Default: GetRandomSetsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomSetsResponse]
    """

    return sync_detailed(
        client=client,
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomSetsSort] = UNSET,
    order: Union[Unset, GetRandomSetsOrder] = GetRandomSetsOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, RandomSetsResponse]]:
    """Get random sets matching filters

     Returns random sets instead of paginated sorted results. Useful for discovery features or showcasing
    catalog variety. Supports all standard set filters including release, year range, manufacturer, and
    name search. Each set includes its release context and card/parallel counts. If count exceeds
    available matching sets, returns all available sets.

    Args:
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomSetsIsIdentifiable]):
        sort (Union[Unset, GetRandomSetsSort]):
        order (Union[Unset, GetRandomSetsOrder]):  Default: GetRandomSetsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomSetsResponse]]
    """

    kwargs = _get_kwargs(
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomSetsSort] = UNSET,
    order: Union[Unset, GetRandomSetsOrder] = GetRandomSetsOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, RandomSetsResponse]]:
    """Get random sets matching filters

     Returns random sets instead of paginated sorted results. Useful for discovery features or showcasing
    catalog variety. Supports all standard set filters including release, year range, manufacturer, and
    name search. Each set includes its release context and card/parallel counts. If count exceeds
    available matching sets, returns all available sets.

    Args:
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomSetsIsIdentifiable]):
        sort (Union[Unset, GetRandomSetsSort]):
        order (Union[Unset, GetRandomSetsOrder]):  Default: GetRandomSetsOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomSetsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            release_id=release_id,
            name=name,
            year=year,
            min_year=min_year,
            max_year=max_year,
            manufacturer=manufacturer,
            is_identifiable=is_identifiable,
            sort=sort,
            order=order,
            count=count,
        )
    ).parsed
