from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.set_population_response import SetPopulationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    set_id: str,
    *,
    grading_company_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["grading_company_id"] = grading_company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/population/set/{set_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SetPopulationResponse]]:
    if response.status_code == 200:
        response_200 = SetPopulationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = SetPopulationResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, SetPopulationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    set_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SetPopulationResponse]]:
    r"""Get population report for an entire set

     Retrieve graded population counts for a given set, sourced directly from each grading company's
    authoritative per-set figures (e.g. PSA's set-level totals). These match the grading company's own
    website even when CardSight's card-level matching for the set is incomplete.

    Populations are reported per **grading company → grading type → grade**. Every grade defined for a
    present company is enumerated; grades with no recorded data are reported as `population: 0,
    qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: a grading company appears in the response only when its source set has a confirmed
    link to this CardSight set. If no grading company has a confirmed link, `grading_companies` is
    empty.

    **Note**: this endpoint echoes the `set_id` and `set_name` only. For per-card population detail,
    call `/v1/population/card/{card_id}`. For full set metadata (cards, release, etc.), call the catalog
    endpoint.

    Args:
        set_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetPopulationResponse]]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
        grading_company_id=grading_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    set_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SetPopulationResponse]]:
    r"""Get population report for an entire set

     Retrieve graded population counts for a given set, sourced directly from each grading company's
    authoritative per-set figures (e.g. PSA's set-level totals). These match the grading company's own
    website even when CardSight's card-level matching for the set is incomplete.

    Populations are reported per **grading company → grading type → grade**. Every grade defined for a
    present company is enumerated; grades with no recorded data are reported as `population: 0,
    qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: a grading company appears in the response only when its source set has a confirmed
    link to this CardSight set. If no grading company has a confirmed link, `grading_companies` is
    empty.

    **Note**: this endpoint echoes the `set_id` and `set_name` only. For per-card population detail,
    call `/v1/population/card/{card_id}`. For full set metadata (cards, release, etc.), call the catalog
    endpoint.

    Args:
        set_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetPopulationResponse]
    """

    return sync_detailed(
        set_id=set_id,
        client=client,
        grading_company_id=grading_company_id,
    ).parsed


async def asyncio_detailed(
    set_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, SetPopulationResponse]]:
    r"""Get population report for an entire set

     Retrieve graded population counts for a given set, sourced directly from each grading company's
    authoritative per-set figures (e.g. PSA's set-level totals). These match the grading company's own
    website even when CardSight's card-level matching for the set is incomplete.

    Populations are reported per **grading company → grading type → grade**. Every grade defined for a
    present company is enumerated; grades with no recorded data are reported as `population: 0,
    qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: a grading company appears in the response only when its source set has a confirmed
    link to this CardSight set. If no grading company has a confirmed link, `grading_companies` is
    empty.

    **Note**: this endpoint echoes the `set_id` and `set_name` only. For per-card population detail,
    call `/v1/population/card/{card_id}`. For full set metadata (cards, release, etc.), call the catalog
    endpoint.

    Args:
        set_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SetPopulationResponse]]
    """

    kwargs = _get_kwargs(
        set_id=set_id,
        grading_company_id=grading_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    set_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, SetPopulationResponse]]:
    r"""Get population report for an entire set

     Retrieve graded population counts for a given set, sourced directly from each grading company's
    authoritative per-set figures (e.g. PSA's set-level totals). These match the grading company's own
    website even when CardSight's card-level matching for the set is incomplete.

    Populations are reported per **grading company → grading type → grade**. Every grade defined for a
    present company is enumerated; grades with no recorded data are reported as `population: 0,
    qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: a grading company appears in the response only when its source set has a confirmed
    link to this CardSight set. If no grading company has a confirmed link, `grading_companies` is
    empty.

    **Note**: this endpoint echoes the `set_id` and `set_name` only. For per-card population detail,
    call `/v1/population/card/{card_id}`. For full set metadata (cards, release, etc.), call the catalog
    endpoint.

    Args:
        set_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SetPopulationResponse]
    """

    return (
        await asyncio_detailed(
            set_id=set_id,
            client=client,
            grading_company_id=grading_company_id,
        )
    ).parsed
