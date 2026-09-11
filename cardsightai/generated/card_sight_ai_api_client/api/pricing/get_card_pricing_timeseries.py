from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_card_pricing_timeseries_interval import GetCardPricingTimeseriesInterval
from ...models.get_card_pricing_timeseries_listing_type import GetCardPricingTimeseriesListingType
from ...models.timeseries_response import TimeseriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    card_id: str,
    *,
    interval: GetCardPricingTimeseriesInterval,
    periods: Union[Unset, int] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingTimeseriesListingType] = GetCardPricingTimeseriesListingType.BOTH,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_interval = interval.value
    params["interval"] = json_interval

    params["periods"] = periods

    params["as_of_date"] = as_of_date

    json_listing_type: Union[Unset, str] = UNSET
    if not isinstance(listing_type, Unset):
        json_listing_type = listing_type.value

    params["listing_type"] = json_listing_type

    params["parallel_id"] = parallel_id

    params["grade_id"] = grade_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/pricing/{card_id}/timeseries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TimeseriesResponse]]:
    if response.status_code == 200:
        response_200 = TimeseriesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = TimeseriesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, TimeseriesResponse]]:
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
    interval: GetCardPricingTimeseriesInterval,
    periods: Union[Unset, int] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingTimeseriesListingType] = GetCardPricingTimeseriesListingType.BOTH,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, TimeseriesResponse]]:
    r"""Get listing price time series (candlestick rollups) for a card

     Returns per-period descriptive statistics — mean, median, high, low, and count — aggregated over a
    card's marketplace listings, grouped into daily, weekly, or monthly buckets. Statistics are split by
    grade: `raw` holds candles for ungraded listings, and `graded` holds one candle series per grade,
    grouped by grading company — so graded and ungraded prices never blend into one candle range. Within
    each series, candles are further split by listing type, following the same bid/ask semantics as GET
    /pricing/{card_id}: auction candles summarize completed auction sales (the \"bid\" side), while
    fixed candles summarize Buy It Now asking prices (the \"ask\" side — listed prices, not necessarily
    completed sales). The parallel dimension is request-controlled: omit parallel_id and each grade's
    series blends all parallels of that grade; pass \"null\" for base-card-only candles or a UUID for
    one parallel. Use this to chart price trends over time. The viewpoint is `as_of_date` looking
    backward: the newest bucket is the one containing that date (default today, UTC) and the window
    extends back `periods` buckets (defaults: daily 90, weekly 52, monthly 24; `periods` above 365 is
    rejected, while weekly values above 156 and monthly values above 120 are clamped to those per-
    interval caps — the response echoes the effective values). Buckets, listing types, and grades with
    no listings are omitted rather than returned as zeros, and a card with no listings in the window
    returns an empty raw section and empty graded array as a success. A grouped outlier filter is
    applied over the whole window per grade/parallel variant — a listing is only ever judged against
    other listings of its own variant; per-type filtered counts are reported in each series' totals.
    Statistics are descriptive summaries of raw listings — not valuations.

    Args:
        card_id (str):
        interval (GetCardPricingTimeseriesInterval):
        periods (Union[Unset, int]):
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingTimeseriesListingType]):  Default:
            GetCardPricingTimeseriesListingType.BOTH.
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TimeseriesResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        interval=interval,
        periods=periods,
        as_of_date=as_of_date,
        listing_type=listing_type,
        parallel_id=parallel_id,
        grade_id=grade_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    card_id: str,
    *,
    client: AuthenticatedClient,
    interval: GetCardPricingTimeseriesInterval,
    periods: Union[Unset, int] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingTimeseriesListingType] = GetCardPricingTimeseriesListingType.BOTH,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, TimeseriesResponse]]:
    r"""Get listing price time series (candlestick rollups) for a card

     Returns per-period descriptive statistics — mean, median, high, low, and count — aggregated over a
    card's marketplace listings, grouped into daily, weekly, or monthly buckets. Statistics are split by
    grade: `raw` holds candles for ungraded listings, and `graded` holds one candle series per grade,
    grouped by grading company — so graded and ungraded prices never blend into one candle range. Within
    each series, candles are further split by listing type, following the same bid/ask semantics as GET
    /pricing/{card_id}: auction candles summarize completed auction sales (the \"bid\" side), while
    fixed candles summarize Buy It Now asking prices (the \"ask\" side — listed prices, not necessarily
    completed sales). The parallel dimension is request-controlled: omit parallel_id and each grade's
    series blends all parallels of that grade; pass \"null\" for base-card-only candles or a UUID for
    one parallel. Use this to chart price trends over time. The viewpoint is `as_of_date` looking
    backward: the newest bucket is the one containing that date (default today, UTC) and the window
    extends back `periods` buckets (defaults: daily 90, weekly 52, monthly 24; `periods` above 365 is
    rejected, while weekly values above 156 and monthly values above 120 are clamped to those per-
    interval caps — the response echoes the effective values). Buckets, listing types, and grades with
    no listings are omitted rather than returned as zeros, and a card with no listings in the window
    returns an empty raw section and empty graded array as a success. A grouped outlier filter is
    applied over the whole window per grade/parallel variant — a listing is only ever judged against
    other listings of its own variant; per-type filtered counts are reported in each series' totals.
    Statistics are descriptive summaries of raw listings — not valuations.

    Args:
        card_id (str):
        interval (GetCardPricingTimeseriesInterval):
        periods (Union[Unset, int]):
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingTimeseriesListingType]):  Default:
            GetCardPricingTimeseriesListingType.BOTH.
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TimeseriesResponse]
    """

    return sync_detailed(
        card_id=card_id,
        client=client,
        interval=interval,
        periods=periods,
        as_of_date=as_of_date,
        listing_type=listing_type,
        parallel_id=parallel_id,
        grade_id=grade_id,
    ).parsed


async def asyncio_detailed(
    card_id: str,
    *,
    client: AuthenticatedClient,
    interval: GetCardPricingTimeseriesInterval,
    periods: Union[Unset, int] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingTimeseriesListingType] = GetCardPricingTimeseriesListingType.BOTH,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, TimeseriesResponse]]:
    r"""Get listing price time series (candlestick rollups) for a card

     Returns per-period descriptive statistics — mean, median, high, low, and count — aggregated over a
    card's marketplace listings, grouped into daily, weekly, or monthly buckets. Statistics are split by
    grade: `raw` holds candles for ungraded listings, and `graded` holds one candle series per grade,
    grouped by grading company — so graded and ungraded prices never blend into one candle range. Within
    each series, candles are further split by listing type, following the same bid/ask semantics as GET
    /pricing/{card_id}: auction candles summarize completed auction sales (the \"bid\" side), while
    fixed candles summarize Buy It Now asking prices (the \"ask\" side — listed prices, not necessarily
    completed sales). The parallel dimension is request-controlled: omit parallel_id and each grade's
    series blends all parallels of that grade; pass \"null\" for base-card-only candles or a UUID for
    one parallel. Use this to chart price trends over time. The viewpoint is `as_of_date` looking
    backward: the newest bucket is the one containing that date (default today, UTC) and the window
    extends back `periods` buckets (defaults: daily 90, weekly 52, monthly 24; `periods` above 365 is
    rejected, while weekly values above 156 and monthly values above 120 are clamped to those per-
    interval caps — the response echoes the effective values). Buckets, listing types, and grades with
    no listings are omitted rather than returned as zeros, and a card with no listings in the window
    returns an empty raw section and empty graded array as a success. A grouped outlier filter is
    applied over the whole window per grade/parallel variant — a listing is only ever judged against
    other listings of its own variant; per-type filtered counts are reported in each series' totals.
    Statistics are descriptive summaries of raw listings — not valuations.

    Args:
        card_id (str):
        interval (GetCardPricingTimeseriesInterval):
        periods (Union[Unset, int]):
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingTimeseriesListingType]):  Default:
            GetCardPricingTimeseriesListingType.BOTH.
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TimeseriesResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        interval=interval,
        periods=periods,
        as_of_date=as_of_date,
        listing_type=listing_type,
        parallel_id=parallel_id,
        grade_id=grade_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    card_id: str,
    *,
    client: AuthenticatedClient,
    interval: GetCardPricingTimeseriesInterval,
    periods: Union[Unset, int] = UNSET,
    as_of_date: Union[Unset, str] = UNSET,
    listing_type: Union[Unset, GetCardPricingTimeseriesListingType] = GetCardPricingTimeseriesListingType.BOTH,
    parallel_id: Union[Unset, str] = UNSET,
    grade_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, TimeseriesResponse]]:
    r"""Get listing price time series (candlestick rollups) for a card

     Returns per-period descriptive statistics — mean, median, high, low, and count — aggregated over a
    card's marketplace listings, grouped into daily, weekly, or monthly buckets. Statistics are split by
    grade: `raw` holds candles for ungraded listings, and `graded` holds one candle series per grade,
    grouped by grading company — so graded and ungraded prices never blend into one candle range. Within
    each series, candles are further split by listing type, following the same bid/ask semantics as GET
    /pricing/{card_id}: auction candles summarize completed auction sales (the \"bid\" side), while
    fixed candles summarize Buy It Now asking prices (the \"ask\" side — listed prices, not necessarily
    completed sales). The parallel dimension is request-controlled: omit parallel_id and each grade's
    series blends all parallels of that grade; pass \"null\" for base-card-only candles or a UUID for
    one parallel. Use this to chart price trends over time. The viewpoint is `as_of_date` looking
    backward: the newest bucket is the one containing that date (default today, UTC) and the window
    extends back `periods` buckets (defaults: daily 90, weekly 52, monthly 24; `periods` above 365 is
    rejected, while weekly values above 156 and monthly values above 120 are clamped to those per-
    interval caps — the response echoes the effective values). Buckets, listing types, and grades with
    no listings are omitted rather than returned as zeros, and a card with no listings in the window
    returns an empty raw section and empty graded array as a success. A grouped outlier filter is
    applied over the whole window per grade/parallel variant — a listing is only ever judged against
    other listings of its own variant; per-type filtered counts are reported in each series' totals.
    Statistics are descriptive summaries of raw listings — not valuations.

    Args:
        card_id (str):
        interval (GetCardPricingTimeseriesInterval):
        periods (Union[Unset, int]):
        as_of_date (Union[Unset, str]):
        listing_type (Union[Unset, GetCardPricingTimeseriesListingType]):  Default:
            GetCardPricingTimeseriesListingType.BOTH.
        parallel_id (Union[Unset, str]):
        grade_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TimeseriesResponse]
    """

    return (
        await asyncio_detailed(
            card_id=card_id,
            client=client,
            interval=interval,
            periods=periods,
            as_of_date=as_of_date,
            listing_type=listing_type,
            parallel_id=parallel_id,
            grade_id=grade_id,
        )
    ).parsed
