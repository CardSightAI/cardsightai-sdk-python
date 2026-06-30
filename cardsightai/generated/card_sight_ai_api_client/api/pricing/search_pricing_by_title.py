from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.pricing_search_response import PricingSearchResponse
from ...models.search_pricing_by_title_listing_type import SearchPricingByTitleListingType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    period: Union[Unset, str] = "all",
    listing_type: Union[Unset, SearchPricingByTitleListingType] = SearchPricingByTitleListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["period"] = period

    json_listing_type: Union[Unset, str] = UNSET
    if not isinstance(listing_type, Unset):
        json_listing_type = listing_type.value

    params["listing_type"] = json_listing_type

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/pricing/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PricingSearchResponse]]:
    if response.status_code == 200:
        response_200 = PricingSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PricingSearchResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PricingSearchResponse]]:
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
    period: Union[Unset, str] = "all",
    listing_type: Union[Unset, SearchPricingByTitleListingType] = SearchPricingByTitleListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PricingSearchResponse]]:
    r"""Search price history by listing title

     Free-text fuzzy search over marketplace listing titles for historical pricing — completed auction
    sales (the \"bid\" side) and Buy It Now asking prices (the \"ask\" side, not necessarily a completed
    sale). Surfaces raw listing data including listings that were never matched to a canonical card —
    useful for cards our matcher struggles with or sellers who use unusual titles. Returns a flat list
    of results ranked by title relevance; each result carries the canonical card it matched (when any).
    Supports filtering by listing type and time period.

    Args:
        q (str):
        period (Union[Unset, str]):  Default: 'all'.
        listing_type (Union[Unset, SearchPricingByTitleListingType]):  Default:
            SearchPricingByTitleListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PricingSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        period=period,
        listing_type=listing_type,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    period: Union[Unset, str] = "all",
    listing_type: Union[Unset, SearchPricingByTitleListingType] = SearchPricingByTitleListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PricingSearchResponse]]:
    r"""Search price history by listing title

     Free-text fuzzy search over marketplace listing titles for historical pricing — completed auction
    sales (the \"bid\" side) and Buy It Now asking prices (the \"ask\" side, not necessarily a completed
    sale). Surfaces raw listing data including listings that were never matched to a canonical card —
    useful for cards our matcher struggles with or sellers who use unusual titles. Returns a flat list
    of results ranked by title relevance; each result carries the canonical card it matched (when any).
    Supports filtering by listing type and time period.

    Args:
        q (str):
        period (Union[Unset, str]):  Default: 'all'.
        listing_type (Union[Unset, SearchPricingByTitleListingType]):  Default:
            SearchPricingByTitleListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PricingSearchResponse]
    """

    return sync_detailed(
        client=client,
        q=q,
        period=period,
        listing_type=listing_type,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    period: Union[Unset, str] = "all",
    listing_type: Union[Unset, SearchPricingByTitleListingType] = SearchPricingByTitleListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PricingSearchResponse]]:
    r"""Search price history by listing title

     Free-text fuzzy search over marketplace listing titles for historical pricing — completed auction
    sales (the \"bid\" side) and Buy It Now asking prices (the \"ask\" side, not necessarily a completed
    sale). Surfaces raw listing data including listings that were never matched to a canonical card —
    useful for cards our matcher struggles with or sellers who use unusual titles. Returns a flat list
    of results ranked by title relevance; each result carries the canonical card it matched (when any).
    Supports filtering by listing type and time period.

    Args:
        q (str):
        period (Union[Unset, str]):  Default: 'all'.
        listing_type (Union[Unset, SearchPricingByTitleListingType]):  Default:
            SearchPricingByTitleListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PricingSearchResponse]]
    """

    kwargs = _get_kwargs(
        q=q,
        period=period,
        listing_type=listing_type,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    period: Union[Unset, str] = "all",
    listing_type: Union[Unset, SearchPricingByTitleListingType] = SearchPricingByTitleListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PricingSearchResponse]]:
    r"""Search price history by listing title

     Free-text fuzzy search over marketplace listing titles for historical pricing — completed auction
    sales (the \"bid\" side) and Buy It Now asking prices (the \"ask\" side, not necessarily a completed
    sale). Surfaces raw listing data including listings that were never matched to a canonical card —
    useful for cards our matcher struggles with or sellers who use unusual titles. Returns a flat list
    of results ranked by title relevance; each result carries the canonical card it matched (when any).
    Supports filtering by listing type and time period.

    Args:
        q (str):
        period (Union[Unset, str]):  Default: 'all'.
        listing_type (Union[Unset, SearchPricingByTitleListingType]):  Default:
            SearchPricingByTitleListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PricingSearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            period=period,
            listing_type=listing_type,
            limit=limit,
        )
    ).parsed
