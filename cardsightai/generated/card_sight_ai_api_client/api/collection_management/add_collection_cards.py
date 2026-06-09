from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_collection_cards_response import BatchCollectionCardsResponse
from ...models.collection_card import CollectionCard
from ...models.collection_card_item_input import CollectionCardItemInput
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    collection_id: UUID,
    *,
    body: Union["CollectionCardItemInput", list["CollectionCardItemInput"]],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/collection/{collection_id}/cards",
    }

    _kwargs["json"]: Union[dict[str, Any], list[dict[str, Any]]]
    if isinstance(body, CollectionCardItemInput):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = []
        for componentsschemas_create_collection_card_input_type_1_item_data in body:
            componentsschemas_create_collection_card_input_type_1_item = (
                componentsschemas_create_collection_card_input_type_1_item_data.to_dict()
            )
            _kwargs["json"].append(componentsschemas_create_collection_card_input_type_1_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> Union["BatchCollectionCardsResponse", "CollectionCard"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_add_collection_cards_response_type_0 = CollectionCard.from_dict(data)

                return componentsschemas_add_collection_cards_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_add_collection_cards_response_type_1 = BatchCollectionCardsResponse.from_dict(data)

            return componentsschemas_add_collection_cards_response_type_1

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union["CollectionCardItemInput", list["CollectionCardItemInput"]],
) -> Response[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    r"""Add cards to collection

     Add one or multiple cards to a collection with detailed tracking information.

    **Supports two modes:**
    1. **Single Card**: Add one card with all metadata
    2. **Batch Mode**: Add up to 100 cards in a single request

    **Card Metadata (all optional):**
    - **quantity**: Number of copies (default: 1)
    - **grade**: Professional grading (e.g., \"PSA 10\", \"BGS 9.5\")
    - **gradeCompany**: Grading service (PSA, BGS, SGC, etc.)
    - **purchasePrice**: What you paid for the card
    - **purchaseDate**: When you acquired it
    - **purchaseFrom**: Where/who you bought it from
    - **condition**: Raw condition if ungraded (Mint, Near Mint, etc.)
    - **notes**: Personal notes about the card
    - **isForSale**: Mark card as available for sale
    - **salePrice**: Asking price if for sale

    **Batch Operation:**
    - Use 'cards' array instead of single card fields
    - Mixed success/failure responses possible
    - Returns detailed results for each card

    **Use Cases:**
    - Track new acquisitions
    - Import bulk collections
    - Record graded cards
    - Build want lists

    Args:
        collection_id (UUID):
        body (Union['CollectionCardItemInput', list['CollectionCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['BatchCollectionCardsResponse', 'CollectionCard']]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union["CollectionCardItemInput", list["CollectionCardItemInput"]],
) -> Optional[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    r"""Add cards to collection

     Add one or multiple cards to a collection with detailed tracking information.

    **Supports two modes:**
    1. **Single Card**: Add one card with all metadata
    2. **Batch Mode**: Add up to 100 cards in a single request

    **Card Metadata (all optional):**
    - **quantity**: Number of copies (default: 1)
    - **grade**: Professional grading (e.g., \"PSA 10\", \"BGS 9.5\")
    - **gradeCompany**: Grading service (PSA, BGS, SGC, etc.)
    - **purchasePrice**: What you paid for the card
    - **purchaseDate**: When you acquired it
    - **purchaseFrom**: Where/who you bought it from
    - **condition**: Raw condition if ungraded (Mint, Near Mint, etc.)
    - **notes**: Personal notes about the card
    - **isForSale**: Mark card as available for sale
    - **salePrice**: Asking price if for sale

    **Batch Operation:**
    - Use 'cards' array instead of single card fields
    - Mixed success/failure responses possible
    - Returns detailed results for each card

    **Use Cases:**
    - Track new acquisitions
    - Import bulk collections
    - Record graded cards
    - Build want lists

    Args:
        collection_id (UUID):
        body (Union['CollectionCardItemInput', list['CollectionCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['BatchCollectionCardsResponse', 'CollectionCard']]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union["CollectionCardItemInput", list["CollectionCardItemInput"]],
) -> Response[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    r"""Add cards to collection

     Add one or multiple cards to a collection with detailed tracking information.

    **Supports two modes:**
    1. **Single Card**: Add one card with all metadata
    2. **Batch Mode**: Add up to 100 cards in a single request

    **Card Metadata (all optional):**
    - **quantity**: Number of copies (default: 1)
    - **grade**: Professional grading (e.g., \"PSA 10\", \"BGS 9.5\")
    - **gradeCompany**: Grading service (PSA, BGS, SGC, etc.)
    - **purchasePrice**: What you paid for the card
    - **purchaseDate**: When you acquired it
    - **purchaseFrom**: Where/who you bought it from
    - **condition**: Raw condition if ungraded (Mint, Near Mint, etc.)
    - **notes**: Personal notes about the card
    - **isForSale**: Mark card as available for sale
    - **salePrice**: Asking price if for sale

    **Batch Operation:**
    - Use 'cards' array instead of single card fields
    - Mixed success/failure responses possible
    - Returns detailed results for each card

    **Use Cases:**
    - Track new acquisitions
    - Import bulk collections
    - Record graded cards
    - Build want lists

    Args:
        collection_id (UUID):
        body (Union['CollectionCardItemInput', list['CollectionCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['BatchCollectionCardsResponse', 'CollectionCard']]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union["CollectionCardItemInput", list["CollectionCardItemInput"]],
) -> Optional[Union[ErrorResponse, Union["BatchCollectionCardsResponse", "CollectionCard"]]]:
    r"""Add cards to collection

     Add one or multiple cards to a collection with detailed tracking information.

    **Supports two modes:**
    1. **Single Card**: Add one card with all metadata
    2. **Batch Mode**: Add up to 100 cards in a single request

    **Card Metadata (all optional):**
    - **quantity**: Number of copies (default: 1)
    - **grade**: Professional grading (e.g., \"PSA 10\", \"BGS 9.5\")
    - **gradeCompany**: Grading service (PSA, BGS, SGC, etc.)
    - **purchasePrice**: What you paid for the card
    - **purchaseDate**: When you acquired it
    - **purchaseFrom**: Where/who you bought it from
    - **condition**: Raw condition if ungraded (Mint, Near Mint, etc.)
    - **notes**: Personal notes about the card
    - **isForSale**: Mark card as available for sale
    - **salePrice**: Asking price if for sale

    **Batch Operation:**
    - Use 'cards' array instead of single card fields
    - Mixed success/failure responses possible
    - Returns detailed results for each card

    **Use Cases:**
    - Track new acquisitions
    - Import bulk collections
    - Record graded cards
    - Build want lists

    Args:
        collection_id (UUID):
        body (Union['CollectionCardItemInput', list['CollectionCardItemInput']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['BatchCollectionCardsResponse', 'CollectionCard']]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
