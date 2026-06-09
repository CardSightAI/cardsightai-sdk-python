from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_search_response import CatalogSearchResponse
from ...models.error_response import ErrorResponse
from ...models.search_catalog_type import SearchCatalogType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    q: str,
    type_: Union[Unset, SearchCatalogType] = UNSET,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    field: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["take"] = take

    params["skip"] = skip

    params["q"] = q

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["segment"] = segment

    params["manufacturer"] = manufacturer

    params["year"] = year

    params["min_year"] = min_year

    params["max_year"] = max_year

    json_field: Union[Unset, list[str]] = UNSET
    if not isinstance(field, Unset):
        json_field = field

    params["field"] = json_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CatalogSearchResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CatalogSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CatalogSearchResponse.from_dict(response.json())

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
) -> Response[Union[CatalogSearchResponse, ErrorResponse]]:
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
    q: str,
    type_: Union[Unset, SearchCatalogType] = UNSET,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    field: Union[Unset, list[str]] = UNSET,
) -> Response[Union[CatalogSearchResponse, ErrorResponse]]:
    r"""Search across cards, sets, releases, and parallels

     Global fuzzy search endpoint that searches across card names, set names, release names, parallel
    names, manufacturer names, and years simultaneously. Supports multi-word queries like \"aaron judge
    topps\", \"1952 mickey mantle\", or \"refractor\". Uses PostgreSQL full-text search combined with
    trigram similarity for typo-tolerant matching. Results are ranked by relevance and returned as a
    mixed list of cards, sets, releases, and parallels. Cards and sets that match a parallel name (e.g.,
    \"Refractor\") are boosted in relevance and include the matching parallelName in the response. Use
    the \"type\" parameter to filter to a specific entity type.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        q (str):
        type_ (Union[Unset, SearchCatalogType]):
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        field (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogSearchResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        q=q,
        type_=type_,
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        field=field,
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
    q: str,
    type_: Union[Unset, SearchCatalogType] = UNSET,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    field: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[CatalogSearchResponse, ErrorResponse]]:
    r"""Search across cards, sets, releases, and parallels

     Global fuzzy search endpoint that searches across card names, set names, release names, parallel
    names, manufacturer names, and years simultaneously. Supports multi-word queries like \"aaron judge
    topps\", \"1952 mickey mantle\", or \"refractor\". Uses PostgreSQL full-text search combined with
    trigram similarity for typo-tolerant matching. Results are ranked by relevance and returned as a
    mixed list of cards, sets, releases, and parallels. Cards and sets that match a parallel name (e.g.,
    \"Refractor\") are boosted in relevance and include the matching parallelName in the response. Use
    the \"type\" parameter to filter to a specific entity type.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        q (str):
        type_ (Union[Unset, SearchCatalogType]):
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        field (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogSearchResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        take=take,
        skip=skip,
        q=q,
        type_=type_,
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        field=field,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    q: str,
    type_: Union[Unset, SearchCatalogType] = UNSET,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    field: Union[Unset, list[str]] = UNSET,
) -> Response[Union[CatalogSearchResponse, ErrorResponse]]:
    r"""Search across cards, sets, releases, and parallels

     Global fuzzy search endpoint that searches across card names, set names, release names, parallel
    names, manufacturer names, and years simultaneously. Supports multi-word queries like \"aaron judge
    topps\", \"1952 mickey mantle\", or \"refractor\". Uses PostgreSQL full-text search combined with
    trigram similarity for typo-tolerant matching. Results are ranked by relevance and returned as a
    mixed list of cards, sets, releases, and parallels. Cards and sets that match a parallel name (e.g.,
    \"Refractor\") are boosted in relevance and include the matching parallelName in the response. Use
    the \"type\" parameter to filter to a specific entity type.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        q (str):
        type_ (Union[Unset, SearchCatalogType]):
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        field (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CatalogSearchResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        take=take,
        skip=skip,
        q=q,
        type_=type_,
        segment=segment,
        manufacturer=manufacturer,
        year=year,
        min_year=min_year,
        max_year=max_year,
        field=field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    take: Union[Unset, int] = 20,
    skip: Union[Unset, int] = 0,
    q: str,
    type_: Union[Unset, SearchCatalogType] = UNSET,
    segment: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    year: Union[Unset, str] = UNSET,
    min_year: Union[Unset, str] = UNSET,
    max_year: Union[Unset, str] = UNSET,
    field: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[CatalogSearchResponse, ErrorResponse]]:
    r"""Search across cards, sets, releases, and parallels

     Global fuzzy search endpoint that searches across card names, set names, release names, parallel
    names, manufacturer names, and years simultaneously. Supports multi-word queries like \"aaron judge
    topps\", \"1952 mickey mantle\", or \"refractor\". Uses PostgreSQL full-text search combined with
    trigram similarity for typo-tolerant matching. Results are ranked by relevance and returned as a
    mixed list of cards, sets, releases, and parallels. Cards and sets that match a parallel name (e.g.,
    \"Refractor\") are boosted in relevance and include the matching parallelName in the response. Use
    the \"type\" parameter to filter to a specific entity type.

    Args:
        take (Union[Unset, int]):  Default: 20.
        skip (Union[Unset, int]):  Default: 0.
        q (str):
        type_ (Union[Unset, SearchCatalogType]):
        segment (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        year (Union[Unset, str]):
        min_year (Union[Unset, str]):
        max_year (Union[Unset, str]):
        field (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CatalogSearchResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            take=take,
            skip=skip,
            q=q,
            type_=type_,
            segment=segment,
            manufacturer=manufacturer,
            year=year,
            min_year=min_year,
            max_year=max_year,
            field=field,
        )
    ).parsed
