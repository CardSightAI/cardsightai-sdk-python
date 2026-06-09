from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.card_population_response import CardPopulationResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    card_id: str,
    *,
    grading_company_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["grading_company_id"] = grading_company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/population/card/{card_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CardPopulationResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CardPopulationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CardPopulationResponse.from_dict(response.json())

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
) -> Response[Union[CardPopulationResponse, ErrorResponse]]:
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
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[CardPopulationResponse, ErrorResponse]]:
    r"""Get population report for a single card

     Retrieve the graded population report for a specific card across every grading company that has
    reported data for it.

    The response is structured around the card's variants:
    - **base**: populations recorded against the base card (no parallel applied). Absent if no data
    exists for the base.
    - **parallels[]**: one entry per parallel that has any population data, identified by parallel UUID
    and name.

    Within each variant, populations are nested by **grading company → grading type → grade**. Every
    grade defined for a present company is enumerated; grades with no recorded data are reported as
    `population: 0, qualified_population: 0`. Grading companies that have no data for a given variant
    are omitted from that variant.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Note**: this endpoint echoes the `card_id` and `card_name` only — for full card metadata (set,
    release, parallels, attributes), call the catalog endpoint.

    Args:
        card_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CardPopulationResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        grading_company_id=grading_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    card_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[CardPopulationResponse, ErrorResponse]]:
    r"""Get population report for a single card

     Retrieve the graded population report for a specific card across every grading company that has
    reported data for it.

    The response is structured around the card's variants:
    - **base**: populations recorded against the base card (no parallel applied). Absent if no data
    exists for the base.
    - **parallels[]**: one entry per parallel that has any population data, identified by parallel UUID
    and name.

    Within each variant, populations are nested by **grading company → grading type → grade**. Every
    grade defined for a present company is enumerated; grades with no recorded data are reported as
    `population: 0, qualified_population: 0`. Grading companies that have no data for a given variant
    are omitted from that variant.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Note**: this endpoint echoes the `card_id` and `card_name` only — for full card metadata (set,
    release, parallels, attributes), call the catalog endpoint.

    Args:
        card_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CardPopulationResponse, ErrorResponse]
    """

    return sync_detailed(
        card_id=card_id,
        client=client,
        grading_company_id=grading_company_id,
    ).parsed


async def asyncio_detailed(
    card_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[CardPopulationResponse, ErrorResponse]]:
    r"""Get population report for a single card

     Retrieve the graded population report for a specific card across every grading company that has
    reported data for it.

    The response is structured around the card's variants:
    - **base**: populations recorded against the base card (no parallel applied). Absent if no data
    exists for the base.
    - **parallels[]**: one entry per parallel that has any population data, identified by parallel UUID
    and name.

    Within each variant, populations are nested by **grading company → grading type → grade**. Every
    grade defined for a present company is enumerated; grades with no recorded data are reported as
    `population: 0, qualified_population: 0`. Grading companies that have no data for a given variant
    are omitted from that variant.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Note**: this endpoint echoes the `card_id` and `card_name` only — for full card metadata (set,
    release, parallels, attributes), call the catalog endpoint.

    Args:
        card_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CardPopulationResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        card_id=card_id,
        grading_company_id=grading_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    card_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[CardPopulationResponse, ErrorResponse]]:
    r"""Get population report for a single card

     Retrieve the graded population report for a specific card across every grading company that has
    reported data for it.

    The response is structured around the card's variants:
    - **base**: populations recorded against the base card (no parallel applied). Absent if no data
    exists for the base.
    - **parallels[]**: one entry per parallel that has any population data, identified by parallel UUID
    and name.

    Within each variant, populations are nested by **grading company → grading type → grade**. Every
    grade defined for a present company is enumerated; grades with no recorded data are reported as
    `population: 0, qualified_population: 0`. Grading companies that have no data for a given variant
    are omitted from that variant.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Note**: this endpoint echoes the `card_id` and `card_name` only — for full card metadata (set,
    release, parallels, attributes), call the catalog endpoint.

    Args:
        card_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CardPopulationResponse, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            card_id=card_id,
            client=client,
            grading_company_id=grading_company_id,
        )
    ).parsed
