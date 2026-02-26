from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_list_cards_response import BatchListCardsResponse
from ...models.error_response import ErrorResponse
from ...models.list_card import ListCard
from ...models.list_card_item_input import ListCardItemInput
from ...types import Response


def _get_kwargs(
    list_id: str,
    *,
    body: Union["ListCardItemInput", list["ListCardItemInput"]],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/lists/{list_id}/cards",
    }

    _kwargs["json"]: Union[dict[str, Any], list[dict[str, Any]]]
    if isinstance(body, ListCardItemInput):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = []
        for componentsschemas_add_card_to_list_input_type_1_item_data in body:
            componentsschemas_add_card_to_list_input_type_1_item = (
                componentsschemas_add_card_to_list_input_type_1_item_data.to_dict()
            )
            _kwargs["json"].append(componentsschemas_add_card_to_list_input_type_1_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> Union["BatchListCardsResponse", "ListCard"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_add_cards_to_list_response_type_0 = ListCard.from_dict(data)

                return componentsschemas_add_cards_to_list_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_add_cards_to_list_response_type_1 = BatchListCardsResponse.from_dict(data)

            return componentsschemas_add_cards_to_list_response_type_1

        response_201 = _parse_response_201(response.json())

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

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient,
    body: Union["ListCardItemInput", list["ListCardItemInput"]],
) -> Response[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    """Add card(s) to a list

     Add one or multiple cards to a specific list. Supports both single card and batch (up to 100 cards)
    operations.

    Args:
        list_id (str):
        body (Union['ListCardItemInput', list['ListCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['BatchListCardsResponse', 'ListCard']]]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient,
    body: Union["ListCardItemInput", list["ListCardItemInput"]],
) -> Optional[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    """Add card(s) to a list

     Add one or multiple cards to a specific list. Supports both single card and batch (up to 100 cards)
    operations.

    Args:
        list_id (str):
        body (Union['ListCardItemInput', list['ListCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['BatchListCardsResponse', 'ListCard']]
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient,
    body: Union["ListCardItemInput", list["ListCardItemInput"]],
) -> Response[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    """Add card(s) to a list

     Add one or multiple cards to a specific list. Supports both single card and batch (up to 100 cards)
    operations.

    Args:
        list_id (str):
        body (Union['ListCardItemInput', list['ListCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['BatchListCardsResponse', 'ListCard']]]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient,
    body: Union["ListCardItemInput", list["ListCardItemInput"]],
) -> Optional[Union[ErrorResponse, Union["BatchListCardsResponse", "ListCard"]]]:
    """Add card(s) to a list

     Add one or multiple cards to a specific list. Supports both single card and batch (up to 100 cards)
    operations.

    Args:
        list_id (str):
        body (Union['ListCardItemInput', list['ListCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['BatchListCardsResponse', 'ListCard']]
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
            body=body,
        )
    ).parsed
