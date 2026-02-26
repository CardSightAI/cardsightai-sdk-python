from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.grading_companies_response import GradingCompaniesResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/grades/companies",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GradingCompaniesResponse]]:
    if response.status_code == 200:
        response_200 = GradingCompaniesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = GradingCompaniesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GradingCompaniesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradingCompaniesResponse]]:
    """List all grading companies

     Retrieve a complete list of all grading companies available in the system.

    **Grading companies** are organizations that authenticate and grade trading cards, such as PSA, BGS
    (Beckett), SGC, and CGC.

    **Response includes:**
    - List of all grading companies with metadata
    - Company names, descriptions, and notes
    - Total count of companies

    **Use Cases:**
    - Display grading company selection in UI
    - Populate dropdown menus for grading filters
    - Show available grading options to users
    - Reference data for collection management

    **Example Companies:**
    - PSA (Professional Sports Authenticator)
    - BGS (Beckett Grading Services)
    - SGC (Sportscard Guaranty)
    - CGC (Certified Guaranty Company)

    **Important Notes:**
    - This endpoint returns all companies in the system
    - Companies are sorted alphabetically by name
    - No authentication required (public reference data)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradingCompaniesResponse]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradingCompaniesResponse]]:
    """List all grading companies

     Retrieve a complete list of all grading companies available in the system.

    **Grading companies** are organizations that authenticate and grade trading cards, such as PSA, BGS
    (Beckett), SGC, and CGC.

    **Response includes:**
    - List of all grading companies with metadata
    - Company names, descriptions, and notes
    - Total count of companies

    **Use Cases:**
    - Display grading company selection in UI
    - Populate dropdown menus for grading filters
    - Show available grading options to users
    - Reference data for collection management

    **Example Companies:**
    - PSA (Professional Sports Authenticator)
    - BGS (Beckett Grading Services)
    - SGC (Sportscard Guaranty)
    - CGC (Certified Guaranty Company)

    **Important Notes:**
    - This endpoint returns all companies in the system
    - Companies are sorted alphabetically by name
    - No authentication required (public reference data)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradingCompaniesResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradingCompaniesResponse]]:
    """List all grading companies

     Retrieve a complete list of all grading companies available in the system.

    **Grading companies** are organizations that authenticate and grade trading cards, such as PSA, BGS
    (Beckett), SGC, and CGC.

    **Response includes:**
    - List of all grading companies with metadata
    - Company names, descriptions, and notes
    - Total count of companies

    **Use Cases:**
    - Display grading company selection in UI
    - Populate dropdown menus for grading filters
    - Show available grading options to users
    - Reference data for collection management

    **Example Companies:**
    - PSA (Professional Sports Authenticator)
    - BGS (Beckett Grading Services)
    - SGC (Sportscard Guaranty)
    - CGC (Certified Guaranty Company)

    **Important Notes:**
    - This endpoint returns all companies in the system
    - Companies are sorted alphabetically by name
    - No authentication required (public reference data)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradingCompaniesResponse]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradingCompaniesResponse]]:
    """List all grading companies

     Retrieve a complete list of all grading companies available in the system.

    **Grading companies** are organizations that authenticate and grade trading cards, such as PSA, BGS
    (Beckett), SGC, and CGC.

    **Response includes:**
    - List of all grading companies with metadata
    - Company names, descriptions, and notes
    - Total count of companies

    **Use Cases:**
    - Display grading company selection in UI
    - Populate dropdown menus for grading filters
    - Show available grading options to users
    - Reference data for collection management

    **Example Companies:**
    - PSA (Professional Sports Authenticator)
    - BGS (Beckett Grading Services)
    - SGC (Sportscard Guaranty)
    - CGC (Certified Guaranty Company)

    **Important Notes:**
    - This endpoint returns all companies in the system
    - Companies are sorted alphabetically by name
    - No authentication required (public reference data)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradingCompaniesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
