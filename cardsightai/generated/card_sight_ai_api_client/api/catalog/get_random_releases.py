from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_random_releases_is_identifiable import GetRandomReleasesIsIdentifiable
from ...models.get_random_releases_order import GetRandomReleasesOrder
from ...models.get_random_releases_sort import GetRandomReleasesSort
from ...models.random_releases_response import RandomReleasesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomReleasesIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomReleasesSort] = UNSET,
    order: Union[Unset, GetRandomReleasesOrder] = GetRandomReleasesOrder.ASC,
    count: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["segment"] = segment

    params["manufacturer"] = manufacturer

    params["year"] = year

    params["min_year"] = min_year

    params["max_year"] = max_year

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

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/releases/random",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, RandomReleasesResponse]]:
    if response.status_code == 200:
        response_200 = RandomReleasesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RandomReleasesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, RandomReleasesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomReleasesIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomReleasesSort] = UNSET,
    order: Union[Unset, GetRandomReleasesOrder] = GetRandomReleasesOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, RandomReleasesResponse]]:
    """Get random releases matching filters

     Returns random releases instead of paginated sorted results. Useful for discovery features, random
    browsing, or showcasing variety in the catalog. Supports all standard release filters including
    year, manufacturer, segment, and name search. If count exceeds available matching releases, returns
    all available releases.

    Args:
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomReleasesIsIdentifiable]):
        sort (Union[Unset, GetRandomReleasesSort]):
        order (Union[Unset, GetRandomReleasesOrder]):  Default: GetRandomReleasesOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomReleasesResponse]]
    """

    kwargs = _get_kwargs(
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        name=name,
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
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomReleasesIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomReleasesSort] = UNSET,
    order: Union[Unset, GetRandomReleasesOrder] = GetRandomReleasesOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, RandomReleasesResponse]]:
    """Get random releases matching filters

     Returns random releases instead of paginated sorted results. Useful for discovery features, random
    browsing, or showcasing variety in the catalog. Supports all standard release filters including
    year, manufacturer, segment, and name search. If count exceeds available matching releases, returns
    all available releases.

    Args:
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomReleasesIsIdentifiable]):
        sort (Union[Unset, GetRandomReleasesSort]):
        order (Union[Unset, GetRandomReleasesOrder]):  Default: GetRandomReleasesOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomReleasesResponse]
    """

    return sync_detailed(
        client=client,
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        name=name,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomReleasesIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomReleasesSort] = UNSET,
    order: Union[Unset, GetRandomReleasesOrder] = GetRandomReleasesOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Response[Union[ErrorResponse, RandomReleasesResponse]]:
    """Get random releases matching filters

     Returns random releases instead of paginated sorted results. Useful for discovery features, random
    browsing, or showcasing variety in the catalog. Supports all standard release filters including
    year, manufacturer, segment, and name search. If count exceeds available matching releases, returns
    all available releases.

    Args:
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomReleasesIsIdentifiable]):
        sort (Union[Unset, GetRandomReleasesSort]):
        order (Union[Unset, GetRandomReleasesOrder]):  Default: GetRandomReleasesOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RandomReleasesResponse]]
    """

    kwargs = _get_kwargs(
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        name=name,
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
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetRandomReleasesIsIdentifiable] = UNSET,
    sort: Union[Unset, GetRandomReleasesSort] = UNSET,
    order: Union[Unset, GetRandomReleasesOrder] = GetRandomReleasesOrder.ASC,
    count: Union[Unset, int] = 1,
) -> Optional[Union[ErrorResponse, RandomReleasesResponse]]:
    """Get random releases matching filters

     Returns random releases instead of paginated sorted results. Useful for discovery features, random
    browsing, or showcasing variety in the catalog. Supports all standard release filters including
    year, manufacturer, segment, and name search. If count exceeds available matching releases, returns
    all available releases.

    Args:
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        name (Union[Unset, str]):
        is_identifiable (Union[Unset, GetRandomReleasesIsIdentifiable]):
        sort (Union[Unset, GetRandomReleasesSort]):
        order (Union[Unset, GetRandomReleasesOrder]):  Default: GetRandomReleasesOrder.ASC.
        count (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, RandomReleasesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            segment=segment,
            manufacturer=manufacturer,
            year=year,
            min_year=min_year,
            max_year=max_year,
            name=name,
            is_identifiable=is_identifiable,
            sort=sort,
            order=order,
            count=count,
        )
    ).parsed
