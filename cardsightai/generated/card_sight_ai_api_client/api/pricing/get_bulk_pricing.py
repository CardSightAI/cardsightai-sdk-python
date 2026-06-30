from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_pricing_request_input import BulkPricingRequestInput
from ...models.bulk_pricing_response import BulkPricingResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    body: BulkPricingRequestInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/pricing/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkPricingResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = BulkPricingResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = BulkPricingResponse.from_dict(response.json())

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
) -> Response[Union[BulkPricingResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPricingRequestInput,
) -> Response[Union[BulkPricingResponse, ErrorResponse]]:
    """Get price history (bid/ask) for multiple cards

     Returns price history as a bid/ask spread for up to 100 cards in a single request — completed
    auction sales (bid) and Buy It Now asking prices (ask, not necessarily a completed sale). Each card
    is processed independently — individual cards may succeed or fail without affecting others. Results
    include the same raw/graded grouping as the single-card endpoint.

    Args:
        body (BulkPricingRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPricingResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BulkPricingRequestInput,
) -> Optional[Union[BulkPricingResponse, ErrorResponse]]:
    """Get price history (bid/ask) for multiple cards

     Returns price history as a bid/ask spread for up to 100 cards in a single request — completed
    auction sales (bid) and Buy It Now asking prices (ask, not necessarily a completed sale). Each card
    is processed independently — individual cards may succeed or fail without affecting others. Results
    include the same raw/graded grouping as the single-card endpoint.

    Args:
        body (BulkPricingRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPricingResponse, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkPricingRequestInput,
) -> Response[Union[BulkPricingResponse, ErrorResponse]]:
    """Get price history (bid/ask) for multiple cards

     Returns price history as a bid/ask spread for up to 100 cards in a single request — completed
    auction sales (bid) and Buy It Now asking prices (ask, not necessarily a completed sale). Each card
    is processed independently — individual cards may succeed or fail without affecting others. Results
    include the same raw/graded grouping as the single-card endpoint.

    Args:
        body (BulkPricingRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPricingResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkPricingRequestInput,
) -> Optional[Union[BulkPricingResponse, ErrorResponse]]:
    """Get price history (bid/ask) for multiple cards

     Returns price history as a bid/ask spread for up to 100 cards in a single request — completed
    auction sales (bid) and Buy It Now asking prices (ask, not necessarily a completed sale). Each card
    is processed independently — individual cards may succeed or fail without affecting others. Results
    include the same raw/graded grouping as the single-card endpoint.

    Args:
        body (BulkPricingRequestInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPricingResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
