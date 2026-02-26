from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.grading_types_response import GradingTypesResponse
from ...types import Response


def _get_kwargs(
    company_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/grades/companies/{company_id}/types",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GradingTypesResponse]]:
    if response.status_code == 200:
        response_200 = GradingTypesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = GradingTypesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GradingTypesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradingTypesResponse]]:
    """Get grading types for a company

     Retrieve all grading types offered by a specific grading company.

    **Grading types** represent different grading services offered by a company, such as:
    - PSA: Regular, Crossover, Dual Grade
    - BGS: Standard, Black Label, Pristine
    - SGC: Regular, Tuxedo, Premium

    **Path Parameters:**
    - **companyId**: UUID of the grading company

    **Response includes:**
    - List of all grading types for the company
    - Type names, descriptions, and notes
    - Parent grading company information for context
    - Total count of types

    **Use Cases:**
    - Display available grading services for a company
    - Filter grades by grading type
    - Show grading options when adding cards to collection
    - Populate grading type selection in UI

    **Example Types:**
    - PSA Regular (standard PSA grading)
    - BGS Black Label (perfect 10 across all subgrades)
    - SGC Tuxedo (premium black label holder)

    **Important Notes:**
    - Types are specific to each grading company
    - Returns 404 if company ID doesn't exist
    - Types are sorted alphabetically by name

    Args:
        company_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradingTypesResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradingTypesResponse]]:
    """Get grading types for a company

     Retrieve all grading types offered by a specific grading company.

    **Grading types** represent different grading services offered by a company, such as:
    - PSA: Regular, Crossover, Dual Grade
    - BGS: Standard, Black Label, Pristine
    - SGC: Regular, Tuxedo, Premium

    **Path Parameters:**
    - **companyId**: UUID of the grading company

    **Response includes:**
    - List of all grading types for the company
    - Type names, descriptions, and notes
    - Parent grading company information for context
    - Total count of types

    **Use Cases:**
    - Display available grading services for a company
    - Filter grades by grading type
    - Show grading options when adding cards to collection
    - Populate grading type selection in UI

    **Example Types:**
    - PSA Regular (standard PSA grading)
    - BGS Black Label (perfect 10 across all subgrades)
    - SGC Tuxedo (premium black label holder)

    **Important Notes:**
    - Types are specific to each grading company
    - Returns 404 if company ID doesn't exist
    - Types are sorted alphabetically by name

    Args:
        company_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradingTypesResponse]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradingTypesResponse]]:
    """Get grading types for a company

     Retrieve all grading types offered by a specific grading company.

    **Grading types** represent different grading services offered by a company, such as:
    - PSA: Regular, Crossover, Dual Grade
    - BGS: Standard, Black Label, Pristine
    - SGC: Regular, Tuxedo, Premium

    **Path Parameters:**
    - **companyId**: UUID of the grading company

    **Response includes:**
    - List of all grading types for the company
    - Type names, descriptions, and notes
    - Parent grading company information for context
    - Total count of types

    **Use Cases:**
    - Display available grading services for a company
    - Filter grades by grading type
    - Show grading options when adding cards to collection
    - Populate grading type selection in UI

    **Example Types:**
    - PSA Regular (standard PSA grading)
    - BGS Black Label (perfect 10 across all subgrades)
    - SGC Tuxedo (premium black label holder)

    **Important Notes:**
    - Types are specific to each grading company
    - Returns 404 if company ID doesn't exist
    - Types are sorted alphabetically by name

    Args:
        company_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradingTypesResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradingTypesResponse]]:
    """Get grading types for a company

     Retrieve all grading types offered by a specific grading company.

    **Grading types** represent different grading services offered by a company, such as:
    - PSA: Regular, Crossover, Dual Grade
    - BGS: Standard, Black Label, Pristine
    - SGC: Regular, Tuxedo, Premium

    **Path Parameters:**
    - **companyId**: UUID of the grading company

    **Response includes:**
    - List of all grading types for the company
    - Type names, descriptions, and notes
    - Parent grading company information for context
    - Total count of types

    **Use Cases:**
    - Display available grading services for a company
    - Filter grades by grading type
    - Show grading options when adding cards to collection
    - Populate grading type selection in UI

    **Example Types:**
    - PSA Regular (standard PSA grading)
    - BGS Black Label (perfect 10 across all subgrades)
    - SGC Tuxedo (premium black label holder)

    **Important Notes:**
    - Types are specific to each grading company
    - Returns 404 if company ID doesn't exist
    - Types are sorted alphabetically by name

    Args:
        company_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradingTypesResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
        )
    ).parsed
