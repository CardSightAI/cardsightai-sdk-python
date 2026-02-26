from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.feedback_submit_response import FeedbackSubmitResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/feedback/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    if response.status_code == 200:
        response_200 = FeedbackSubmitResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

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
) -> Response[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Retrieve feedback by ID

     Retrieve a previously submitted feedback entry by its unique ID.

    **Important Security Notes:**
    - You can only retrieve feedback submitted by your own API key
    - Attempting to access feedback from another client will result in a 403 Forbidden error
    - The unique ID is a UUID that was returned when the feedback was originally submitted

    Use this endpoint to:
    - Check the status of your submitted feedback
    - Retrieve details of feedback for your own records
    - Verify that feedback was successfully submitted

    **Response Codes:**
    - 200: Feedback found and belongs to your client
    - 401: Authentication required
    - 403: Feedback exists but belongs to another client
    - 404: Feedback ID not found

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FeedbackSubmitResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Retrieve feedback by ID

     Retrieve a previously submitted feedback entry by its unique ID.

    **Important Security Notes:**
    - You can only retrieve feedback submitted by your own API key
    - Attempting to access feedback from another client will result in a 403 Forbidden error
    - The unique ID is a UUID that was returned when the feedback was originally submitted

    Use this endpoint to:
    - Check the status of your submitted feedback
    - Retrieve details of feedback for your own records
    - Verify that feedback was successfully submitted

    **Response Codes:**
    - 200: Feedback found and belongs to your client
    - 401: Authentication required
    - 403: Feedback exists but belongs to another client
    - 404: Feedback ID not found

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, FeedbackSubmitResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Retrieve feedback by ID

     Retrieve a previously submitted feedback entry by its unique ID.

    **Important Security Notes:**
    - You can only retrieve feedback submitted by your own API key
    - Attempting to access feedback from another client will result in a 403 Forbidden error
    - The unique ID is a UUID that was returned when the feedback was originally submitted

    Use this endpoint to:
    - Check the status of your submitted feedback
    - Retrieve details of feedback for your own records
    - Verify that feedback was successfully submitted

    **Response Codes:**
    - 200: Feedback found and belongs to your client
    - 401: Authentication required
    - 403: Feedback exists but belongs to another client
    - 404: Feedback ID not found

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FeedbackSubmitResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, FeedbackSubmitResponse]]:
    """Retrieve feedback by ID

     Retrieve a previously submitted feedback entry by its unique ID.

    **Important Security Notes:**
    - You can only retrieve feedback submitted by your own API key
    - Attempting to access feedback from another client will result in a 403 Forbidden error
    - The unique ID is a UUID that was returned when the feedback was originally submitted

    Use this endpoint to:
    - Check the status of your submitted feedback
    - Retrieve details of feedback for your own records
    - Verify that feedback was successfully submitted

    **Response Codes:**
    - 200: Feedback found and belongs to your client
    - 401: Authentication required
    - 403: Feedback exists but belongs to another client
    - 404: Feedback ID not found

    Args:
        id (UUID):

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
        )
    ).parsed
