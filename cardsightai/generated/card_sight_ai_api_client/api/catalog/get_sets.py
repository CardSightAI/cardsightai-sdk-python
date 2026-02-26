from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_sets_is_identifiable import GetSetsIsIdentifiable
from ...models.get_sets_order import GetSetsOrder
from ...models.get_sets_sort import GetSetsSort
from ...models.paginated_sets_response import PaginatedSetsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSetsSort] = UNSET,
    order: Union[Unset, GetSetsOrder] = GetSetsOrder.ASC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/sets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PaginatedSetsResponse]]:
    if response.status_code == 200:
        response_200 = PaginatedSetsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PaginatedSetsResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PaginatedSetsResponse]]:
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
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSetsSort] = UNSET,
    order: Union[Unset, GetSetsOrder] = GetSetsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedSetsResponse]]:
    r"""List and search card sets

     Retrieve a paginated list of card sets across all releases. Sets represent collections within
    releases (e.g., \"Base Set\", \"Rookie Autographs\"). Filter by release, year range, manufacturer,
    or search by name. Results include card and parallel counts for each set. Use this endpoint to
    explore available sets, build set checklists, or filter sets by specific criteria. Each set belongs
    to exactly one release.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSetsIsIdentifiable]):
        sort (Union[Unset, GetSetsSort]):
        order (Union[Unset, GetSetsOrder]):  Default: GetSetsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedSetsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
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
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSetsSort] = UNSET,
    order: Union[Unset, GetSetsOrder] = GetSetsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedSetsResponse]]:
    r"""List and search card sets

     Retrieve a paginated list of card sets across all releases. Sets represent collections within
    releases (e.g., \"Base Set\", \"Rookie Autographs\"). Filter by release, year range, manufacturer,
    or search by name. Results include card and parallel counts for each set. Use this endpoint to
    explore available sets, build set checklists, or filter sets by specific criteria. Each set belongs
    to exactly one release.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSetsIsIdentifiable]):
        sort (Union[Unset, GetSetsSort]):
        order (Union[Unset, GetSetsOrder]):  Default: GetSetsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedSetsResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
        is_identifiable=is_identifiable,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSetsSort] = UNSET,
    order: Union[Unset, GetSetsOrder] = GetSetsOrder.ASC,
) -> Response[Union[ErrorResponse, PaginatedSetsResponse]]:
    r"""List and search card sets

     Retrieve a paginated list of card sets across all releases. Sets represent collections within
    releases (e.g., \"Base Set\", \"Rookie Autographs\"). Filter by release, year range, manufacturer,
    or search by name. Results include card and parallel counts for each set. Use this endpoint to
    explore available sets, build set checklists, or filter sets by specific criteria. Each set belongs
    to exactly one release.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSetsIsIdentifiable]):
        sort (Union[Unset, GetSetsSort]):
        order (Union[Unset, GetSetsOrder]):  Default: GetSetsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PaginatedSetsResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        release_id=release_id,
        name=name,
        year=year,
        min_year=min_year,
        max_year=max_year,
        manufacturer=manufacturer,
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
    release_id: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    is_identifiable: Union[Unset, GetSetsIsIdentifiable] = UNSET,
    sort: Union[Unset, GetSetsSort] = UNSET,
    order: Union[Unset, GetSetsOrder] = GetSetsOrder.ASC,
) -> Optional[Union[ErrorResponse, PaginatedSetsResponse]]:
    r"""List and search card sets

     Retrieve a paginated list of card sets across all releases. Sets represent collections within
    releases (e.g., \"Base Set\", \"Rookie Autographs\"). Filter by release, year range, manufacturer,
    or search by name. Results include card and parallel counts for each set. Use this endpoint to
    explore available sets, build set checklists, or filter sets by specific criteria. Each set belongs
    to exactly one release.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        release_id (Union[Unset, str]):
        name (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        is_identifiable (Union[Unset, GetSetsIsIdentifiable]):
        sort (Union[Unset, GetSetsSort]):
        order (Union[Unset, GetSetsOrder]):  Default: GetSetsOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PaginatedSetsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
            release_id=release_id,
            name=name,
            year=year,
            min_year=min_year,
            max_year=max_year,
            manufacturer=manufacturer,
            is_identifiable=is_identifiable,
            sort=sort,
            order=order,
        )
    ).parsed
