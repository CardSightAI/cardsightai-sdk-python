from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.grades_response import GradesResponse
from ...types import Response


def _get_kwargs(
    company_id: UUID,
    type_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/grades/companies/{company_id}/types/{type_id}/grades",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GradesResponse]]:
    if response.status_code == 200:
        response_200 = GradesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = GradesResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GradesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: UUID,
    type_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradesResponse]]:
    r"""Get grades for a grading type

     Retrieve all specific grades available for a grading type.

    **Grades** are the actual numeric/letter grades assigned to cards, such as:
    - PSA: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    - BGS: 1, 1.5, 2, 2.5, ... 9, 9.5, 10
    - SGC: 1, 1.5, 2, 2.5, ... 9, 9.5, 10

    **Path Parameters:**
    - **companyId**: UUID of the grading company
    - **typeId**: UUID of the grading type

    **Response includes:**
    - List of all grades for the grading type
    - Grade values (as strings to support decimals like \"9.5\")
    - Parent grading type and company information for context
    - Total count of grades

    **Use Cases:**
    - Display available grades when adding graded cards to collection
    - Filter collection cards by specific grade
    - Show grade options in grading selection UI
    - Validate grade values for card submissions

    **Example Grades:**
    - PSA 10 (Gem Mint)
    - PSA 9 (Mint)
    - BGS 9.5 (Gem Mint)
    - SGC 10 (Pristine)

    **Important Notes:**
    - Grades are specific to each grading type
    - Grade values are stored as strings to support decimal grades
    - Returns 404 if company or type ID doesn't exist
    - Validates that the type belongs to the specified company
    - Grades are sorted by their grade value

    Args:
        company_id (UUID):
        type_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradesResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        type_id=type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: UUID,
    type_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradesResponse]]:
    r"""Get grades for a grading type

     Retrieve all specific grades available for a grading type.

    **Grades** are the actual numeric/letter grades assigned to cards, such as:
    - PSA: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    - BGS: 1, 1.5, 2, 2.5, ... 9, 9.5, 10
    - SGC: 1, 1.5, 2, 2.5, ... 9, 9.5, 10

    **Path Parameters:**
    - **companyId**: UUID of the grading company
    - **typeId**: UUID of the grading type

    **Response includes:**
    - List of all grades for the grading type
    - Grade values (as strings to support decimals like \"9.5\")
    - Parent grading type and company information for context
    - Total count of grades

    **Use Cases:**
    - Display available grades when adding graded cards to collection
    - Filter collection cards by specific grade
    - Show grade options in grading selection UI
    - Validate grade values for card submissions

    **Example Grades:**
    - PSA 10 (Gem Mint)
    - PSA 9 (Mint)
    - BGS 9.5 (Gem Mint)
    - SGC 10 (Pristine)

    **Important Notes:**
    - Grades are specific to each grading type
    - Grade values are stored as strings to support decimal grades
    - Returns 404 if company or type ID doesn't exist
    - Validates that the type belongs to the specified company
    - Grades are sorted by their grade value

    Args:
        company_id (UUID):
        type_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradesResponse]
    """

    return sync_detailed(
        company_id=company_id,
        type_id=type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: UUID,
    type_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GradesResponse]]:
    r"""Get grades for a grading type

     Retrieve all specific grades available for a grading type.

    **Grades** are the actual numeric/letter grades assigned to cards, such as:
    - PSA: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    - BGS: 1, 1.5, 2, 2.5, ... 9, 9.5, 10
    - SGC: 1, 1.5, 2, 2.5, ... 9, 9.5, 10

    **Path Parameters:**
    - **companyId**: UUID of the grading company
    - **typeId**: UUID of the grading type

    **Response includes:**
    - List of all grades for the grading type
    - Grade values (as strings to support decimals like \"9.5\")
    - Parent grading type and company information for context
    - Total count of grades

    **Use Cases:**
    - Display available grades when adding graded cards to collection
    - Filter collection cards by specific grade
    - Show grade options in grading selection UI
    - Validate grade values for card submissions

    **Example Grades:**
    - PSA 10 (Gem Mint)
    - PSA 9 (Mint)
    - BGS 9.5 (Gem Mint)
    - SGC 10 (Pristine)

    **Important Notes:**
    - Grades are specific to each grading type
    - Grade values are stored as strings to support decimal grades
    - Returns 404 if company or type ID doesn't exist
    - Validates that the type belongs to the specified company
    - Grades are sorted by their grade value

    Args:
        company_id (UUID):
        type_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GradesResponse]]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        type_id=type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: UUID,
    type_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GradesResponse]]:
    r"""Get grades for a grading type

     Retrieve all specific grades available for a grading type.

    **Grades** are the actual numeric/letter grades assigned to cards, such as:
    - PSA: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    - BGS: 1, 1.5, 2, 2.5, ... 9, 9.5, 10
    - SGC: 1, 1.5, 2, 2.5, ... 9, 9.5, 10

    **Path Parameters:**
    - **companyId**: UUID of the grading company
    - **typeId**: UUID of the grading type

    **Response includes:**
    - List of all grades for the grading type
    - Grade values (as strings to support decimals like \"9.5\")
    - Parent grading type and company information for context
    - Total count of grades

    **Use Cases:**
    - Display available grades when adding graded cards to collection
    - Filter collection cards by specific grade
    - Show grade options in grading selection UI
    - Validate grade values for card submissions

    **Example Grades:**
    - PSA 10 (Gem Mint)
    - PSA 9 (Mint)
    - BGS 9.5 (Gem Mint)
    - SGC 10 (Pristine)

    **Important Notes:**
    - Grades are specific to each grading type
    - Grade values are stored as strings to support decimal grades
    - Returns 404 if company or type ID doesn't exist
    - Validates that the type belongs to the specified company
    - Grades are sorted by their grade value

    Args:
        company_id (UUID):
        type_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GradesResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            type_id=type_id,
            client=client,
        )
    ).parsed
