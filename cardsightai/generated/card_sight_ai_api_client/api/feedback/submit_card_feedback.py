from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.feedback_input_input import FeedbackInputInput
from ...models.feedback_submit_response import FeedbackSubmitResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: FeedbackInputInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/feedback/card/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    if response.status_code == 201:
        response_201 = FeedbackSubmitResponse.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, FeedbackSubmitResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FeedbackInputInput,
) -> Response[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Submit feedback for a card

     Submit feedback for a specific card in the catalog.

    Use this endpoint to report:
    - Incorrect player name or card details
    - Wrong card number or designation
    - Missing or incorrect parallel/variant information
    - Incorrect card attributes (rookie card, autograph, memorabilia)
    - Image quality issues or wrong image
    - Pricing discrepancies

    **Rate Limiting**: Maximum 50 feedback submissions per day per API key
    **Duplicate Detection**: Same feedback message for the same entity within 1 hour will be rejected

    Args:
        id (UUID):
        body (FeedbackInputInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FeedbackSubmitResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FeedbackInputInput,
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Submit feedback for a card

     Submit feedback for a specific card in the catalog.

    Use this endpoint to report:
    - Incorrect player name or card details
    - Wrong card number or designation
    - Missing or incorrect parallel/variant information
    - Incorrect card attributes (rookie card, autograph, memorabilia)
    - Image quality issues or wrong image
    - Pricing discrepancies

    **Rate Limiting**: Maximum 50 feedback submissions per day per API key
    **Duplicate Detection**: Same feedback message for the same entity within 1 hour will be rejected

    Args:
        id (UUID):
        body (FeedbackInputInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FeedbackSubmitResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FeedbackInputInput,
) -> Response[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Submit feedback for a card

     Submit feedback for a specific card in the catalog.

    Use this endpoint to report:
    - Incorrect player name or card details
    - Wrong card number or designation
    - Missing or incorrect parallel/variant information
    - Incorrect card attributes (rookie card, autograph, memorabilia)
    - Image quality issues or wrong image
    - Pricing discrepancies

    **Rate Limiting**: Maximum 50 feedback submissions per day per API key
    **Duplicate Detection**: Same feedback message for the same entity within 1 hour will be rejected

    Args:
        id (UUID):
        body (FeedbackInputInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FeedbackSubmitResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: FeedbackInputInput,
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Submit feedback for a card

     Submit feedback for a specific card in the catalog.

    Use this endpoint to report:
    - Incorrect player name or card details
    - Wrong card number or designation
    - Missing or incorrect parallel/variant information
    - Incorrect card attributes (rookie card, autograph, memorabilia)
    - Image quality issues or wrong image
    - Pricing discrepancies

    **Rate Limiting**: Maximum 50 feedback submissions per day per API key
    **Duplicate Detection**: Same feedback message for the same entity within 1 hour will be rejected

    Args:
        id (UUID):
        body (FeedbackInputInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FeedbackSubmitResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
