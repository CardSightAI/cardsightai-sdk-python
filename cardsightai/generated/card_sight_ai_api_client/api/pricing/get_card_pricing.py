from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_card_pricing_listing_type import GetCardPricingListingType
from ...models.pricing_response import PricingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    card_id: str,
    *,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = "all",
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingListingType] = GetCardPricingListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["parallel_id"] = parallel_id

    params["grade_id"] = grade_id

    params["period"] = period

    params["as_of_date"] = as_of_date

    json_listing_type: Union[Unset, str] = UNSET
    if not isinstance(listing_type, Unset):
        json_listing_type = listing_type.value

    params["listing_type"] = json_listing_type

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/pricing/{card_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PricingResponse]]:
    if response.status_code == 200:
        response_200 = PricingResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PricingResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, PricingResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    card_id: str,
    *,
    client: AuthenticatedClient,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = "all",
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingListingType] = GetCardPricingListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PricingResponse]]:
    r"""Get price history (bid/ask) for a card

     Returns historical pricing for a single card as a bid/ask spread: completed auction sales (the
    \"bid\" side — what cards actually sold for) alongside Buy It Now listings (the \"ask\" side — what
    sellers were asking, which is not necessarily a completed sale). Results are grouped into raw
    (ungraded) and graded sections, with graded results organized by grading company and grade value.
    Supports filtering by parallel variant, grade, time period, and listing type. Each call returns the
    most-recent listings for the card, up to a cap of 500 rows ending at `as_of_date` (default today, US
    Eastern). If that cap is hit a warning is returned in `messages`; to page further back through
    history, set `as_of_date` to the oldest `date` in the response and query again (the boundary day may
    repeat a few rows — duplicates, never gaps).

    Args:
        card_id (str):
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):
        period (Union[Unset, str]):  Default: 'all'.
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingListingType]):  Default:
            GetCardPricingListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PricingResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        parallel_id=parallel_id,
        grade_id=grade_id,
        period=period,
        as_of_date=as_of_date,
        listing_type=listing_type,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    card_id: str,
    *,
    client: AuthenticatedClient,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = "all",
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingListingType] = GetCardPricingListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PricingResponse]]:
    r"""Get price history (bid/ask) for a card

     Returns historical pricing for a single card as a bid/ask spread: completed auction sales (the
    \"bid\" side — what cards actually sold for) alongside Buy It Now listings (the \"ask\" side — what
    sellers were asking, which is not necessarily a completed sale). Results are grouped into raw
    (ungraded) and graded sections, with graded results organized by grading company and grade value.
    Supports filtering by parallel variant, grade, time period, and listing type. Each call returns the
    most-recent listings for the card, up to a cap of 500 rows ending at `as_of_date` (default today, US
    Eastern). If that cap is hit a warning is returned in `messages`; to page further back through
    history, set `as_of_date` to the oldest `date` in the response and query again (the boundary day may
    repeat a few rows — duplicates, never gaps).

    Args:
        card_id (str):
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):
        period (Union[Unset, str]):  Default: 'all'.
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingListingType]):  Default:
            GetCardPricingListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PricingResponse]
    """

    return sync_detailed(
        card_id=card_id,
        client=client,
        parallel_id=parallel_id,
        grade_id=grade_id,
        period=period,
        as_of_date=as_of_date,
        listing_type=listing_type,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    card_id: str,
    *,
    client: AuthenticatedClient,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = "all",
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingListingType] = GetCardPricingListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, PricingResponse]]:
    r"""Get price history (bid/ask) for a card

     Returns historical pricing for a single card as a bid/ask spread: completed auction sales (the
    \"bid\" side — what cards actually sold for) alongside Buy It Now listings (the \"ask\" side — what
    sellers were asking, which is not necessarily a completed sale). Results are grouped into raw
    (ungraded) and graded sections, with graded results organized by grading company and grade value.
    Supports filtering by parallel variant, grade, time period, and listing type. Each call returns the
    most-recent listings for the card, up to a cap of 500 rows ending at `as_of_date` (default today, US
    Eastern). If that cap is hit a warning is returned in `messages`; to page further back through
    history, set `as_of_date` to the oldest `date` in the response and query again (the boundary day may
    repeat a few rows — duplicates, never gaps).

    Args:
        card_id (str):
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):
        period (Union[Unset, str]):  Default: 'all'.
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingListingType]):  Default:
            GetCardPricingListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PricingResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        parallel_id=parallel_id,
        grade_id=grade_id,
        period=period,
        as_of_date=as_of_date,
        listing_type=listing_type,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    card_id: str,
    *,
    client: AuthenticatedClient,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = "all",
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingListingType] = GetCardPricingListingType.BOTH,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, PricingResponse]]:
    r"""Get price history (bid/ask) for a card

     Returns historical pricing for a single card as a bid/ask spread: completed auction sales (the
    \"bid\" side — what cards actually sold for) alongside Buy It Now listings (the \"ask\" side — what
    sellers were asking, which is not necessarily a completed sale). Results are grouped into raw
    (ungraded) and graded sections, with graded results organized by grading company and grade value.
    Supports filtering by parallel variant, grade, time period, and listing type. Each call returns the
    most-recent listings for the card, up to a cap of 500 rows ending at `as_of_date` (default today, US
    Eastern). If that cap is hit a warning is returned in `messages`; to page further back through
    history, set `as_of_date` to the oldest `date` in the response and query again (the boundary day may
    repeat a few rows — duplicates, never gaps).

    Args:
        card_id (str):
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):
        period (Union[Unset, str]):  Default: 'all'.
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingListingType]):  Default:
            GetCardPricingListingType.BOTH.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PricingResponse]
    """

    return (
        await asyncio_detailed(
            card_id=card_id,
            client=client,
            parallel_id=parallel_id,
            grade_id=grade_id,
            period=period,
            as_of_date=as_of_date,
            listing_type=listing_type,
            limit=limit,
        )
    ).parsed
