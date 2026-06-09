from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.release_population_response import ReleasePopulationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    release_id: str,
    *,
    grading_company_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["grading_company_id"] = grading_company_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/population/release/{release_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ReleasePopulationResponse]]:
    if response.status_code == 200:
        response_200 = ReleasePopulationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ReleasePopulationResponse.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ReleasePopulationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    release_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, ReleasePopulationResponse]]:
    r"""Get population report for an entire release

     Retrieve graded population counts across every set in a release, sourced directly from each grading
    company's authoritative per-set figures (e.g. PSA's set-level totals). These match the grading
    company's own website even when CardSight's card-level matching is incomplete.

    Each grading company entry contains:
    - **grading_types[]**: populations rolled up across every set in the release.
    - **sets[]**: per-set rollups so consumers can see which sets within the release contributed. Sets
    with no confirmed link (or no recorded data) for a company are omitted.

    Within each rollup, every grade defined for the company is enumerated; grades with no recorded data
    are reported as `population: 0, qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: only sets with a confirmed grading-company set link contribute to the totals. A
    release with no confirmed links returns an empty `grading_companies` array.

    **Note**: this endpoint echoes the `release_id` and `release_name` only, plus `set_id` and
    `set_name` for each set rollup. For full release/set metadata (year, manufacturer, full card lists,
    etc.), call the catalog endpoint.

    Args:
        release_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ReleasePopulationResponse]]
    """

    kwargs = _get_kwargs(
        release_id=release_id,
        grading_company_id=grading_company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    release_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, ReleasePopulationResponse]]:
    r"""Get population report for an entire release

     Retrieve graded population counts across every set in a release, sourced directly from each grading
    company's authoritative per-set figures (e.g. PSA's set-level totals). These match the grading
    company's own website even when CardSight's card-level matching is incomplete.

    Each grading company entry contains:
    - **grading_types[]**: populations rolled up across every set in the release.
    - **sets[]**: per-set rollups so consumers can see which sets within the release contributed. Sets
    with no confirmed link (or no recorded data) for a company are omitted.

    Within each rollup, every grade defined for the company is enumerated; grades with no recorded data
    are reported as `population: 0, qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: only sets with a confirmed grading-company set link contribute to the totals. A
    release with no confirmed links returns an empty `grading_companies` array.

    **Note**: this endpoint echoes the `release_id` and `release_name` only, plus `set_id` and
    `set_name` for each set rollup. For full release/set metadata (year, manufacturer, full card lists,
    etc.), call the catalog endpoint.

    Args:
        release_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ReleasePopulationResponse]
    """

    return sync_detailed(
        release_id=release_id,
        client=client,
        grading_company_id=grading_company_id,
    ).parsed


async def asyncio_detailed(
    release_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, ReleasePopulationResponse]]:
    r"""Get population report for an entire release

     Retrieve graded population counts across every set in a release, sourced directly from each grading
    company's authoritative per-set figures (e.g. PSA's set-level totals). These match the grading
    company's own website even when CardSight's card-level matching is incomplete.

    Each grading company entry contains:
    - **grading_types[]**: populations rolled up across every set in the release.
    - **sets[]**: per-set rollups so consumers can see which sets within the release contributed. Sets
    with no confirmed link (or no recorded data) for a company are omitted.

    Within each rollup, every grade defined for the company is enumerated; grades with no recorded data
    are reported as `population: 0, qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: only sets with a confirmed grading-company set link contribute to the totals. A
    release with no confirmed links returns an empty `grading_companies` array.

    **Note**: this endpoint echoes the `release_id` and `release_name` only, plus `set_id` and
    `set_name` for each set rollup. For full release/set metadata (year, manufacturer, full card lists,
    etc.), call the catalog endpoint.

    Args:
        release_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ReleasePopulationResponse]]
    """

    kwargs = _get_kwargs(
        release_id=release_id,
        grading_company_id=grading_company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    release_id: str,
    *,
    client: AuthenticatedClient,
    grading_company_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, ReleasePopulationResponse]]:
    r"""Get population report for an entire release

     Retrieve graded population counts across every set in a release, sourced directly from each grading
    company's authoritative per-set figures (e.g. PSA's set-level totals). These match the grading
    company's own website even when CardSight's card-level matching is incomplete.

    Each grading company entry contains:
    - **grading_types[]**: populations rolled up across every set in the release.
    - **sets[]**: per-set rollups so consumers can see which sets within the release contributed. Sets
    with no confirmed link (or no recorded data) for a company are omitted.

    Within each rollup, every grade defined for the company is enumerated; grades with no recorded data
    are reported as `population: 0, qualified_population: 0`.

    **Qualified vs unqualified**: when a grade is assigned with a qualifier (e.g. PSA \"8Q\"), the count
    is reported in `qualified_population` rather than `population`. Both are reported per grade.

    **Filtering**: pass `?grading_company_id={uuid}` to limit the response to a single grading company.

    **Coverage**: only sets with a confirmed grading-company set link contribute to the totals. A
    release with no confirmed links returns an empty `grading_companies` array.

    **Note**: this endpoint echoes the `release_id` and `release_name` only, plus `set_id` and
    `set_name` for each set rollup. For full release/set metadata (year, manufacturer, full card lists,
    etc.), call the catalog endpoint.

    Args:
        release_id (str):
        grading_company_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ReleasePopulationResponse]
    """

    return (
        await asyncio_detailed(
            release_id=release_id,
            client=client,
            grading_company_id=grading_company_id,
        )
    ).parsed
