from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.subscription_info import SubscriptionInfo
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/subscription/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SubscriptionInfo]]:
    if response.status_code == 200:
        response_200 = SubscriptionInfo.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SubscriptionInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SubscriptionInfo]]:
    r"""Get subscription information

     Retrieve subscription usage information for the authenticated client.

    **Returns:**
    - Total aggregate API calls made across all API keys for the current billing period
    - Array containing usage information for the current API key being used to make this request

    **Billing Period:**
    - The billing period is calculated monthly (first day of the current month to present)
    - Usage data is tracked in the api_key_usage_monthly table
    - Calls are aggregated across all API keys belonging to the client

    **Response Fields:**
    - `calls`: Total number of API calls across all your API keys for the current billing period
    - `api_keys`: Array with one element showing the current API key and its usage
      - `key`: The API key used to make this request
      - `calls`: Number of API calls made using this specific key for the current billing period

    **Example Response:**
    ```json
    {
      \"calls\": 1250,
      \"api_keys\": [
        {
          \"key\": \"csa_live_abc123...\",
          \"calls\": 450
        }
      ]
    }
    ```

    **Use Cases:**
    - Monitor your API usage to stay within subscription limits
    - Track usage by individual API key
    - Identify which keys are making the most requests
    - Billing and cost tracking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SubscriptionInfo]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SubscriptionInfo]]:
    r"""Get subscription information

     Retrieve subscription usage information for the authenticated client.

    **Returns:**
    - Total aggregate API calls made across all API keys for the current billing period
    - Array containing usage information for the current API key being used to make this request

    **Billing Period:**
    - The billing period is calculated monthly (first day of the current month to present)
    - Usage data is tracked in the api_key_usage_monthly table
    - Calls are aggregated across all API keys belonging to the client

    **Response Fields:**
    - `calls`: Total number of API calls across all your API keys for the current billing period
    - `api_keys`: Array with one element showing the current API key and its usage
      - `key`: The API key used to make this request
      - `calls`: Number of API calls made using this specific key for the current billing period

    **Example Response:**
    ```json
    {
      \"calls\": 1250,
      \"api_keys\": [
        {
          \"key\": \"csa_live_abc123...\",
          \"calls\": 450
        }
      ]
    }
    ```

    **Use Cases:**
    - Monitor your API usage to stay within subscription limits
    - Track usage by individual API key
    - Identify which keys are making the most requests
    - Billing and cost tracking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SubscriptionInfo]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorResponse, SubscriptionInfo]]:
    r"""Get subscription information

     Retrieve subscription usage information for the authenticated client.

    **Returns:**
    - Total aggregate API calls made across all API keys for the current billing period
    - Array containing usage information for the current API key being used to make this request

    **Billing Period:**
    - The billing period is calculated monthly (first day of the current month to present)
    - Usage data is tracked in the api_key_usage_monthly table
    - Calls are aggregated across all API keys belonging to the client

    **Response Fields:**
    - `calls`: Total number of API calls across all your API keys for the current billing period
    - `api_keys`: Array with one element showing the current API key and its usage
      - `key`: The API key used to make this request
      - `calls`: Number of API calls made using this specific key for the current billing period

    **Example Response:**
    ```json
    {
      \"calls\": 1250,
      \"api_keys\": [
        {
          \"key\": \"csa_live_abc123...\",
          \"calls\": 450
        }
      ]
    }
    ```

    **Use Cases:**
    - Monitor your API usage to stay within subscription limits
    - Track usage by individual API key
    - Identify which keys are making the most requests
    - Billing and cost tracking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SubscriptionInfo]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorResponse, SubscriptionInfo]]:
    r"""Get subscription information

     Retrieve subscription usage information for the authenticated client.

    **Returns:**
    - Total aggregate API calls made across all API keys for the current billing period
    - Array containing usage information for the current API key being used to make this request

    **Billing Period:**
    - The billing period is calculated monthly (first day of the current month to present)
    - Usage data is tracked in the api_key_usage_monthly table
    - Calls are aggregated across all API keys belonging to the client

    **Response Fields:**
    - `calls`: Total number of API calls across all your API keys for the current billing period
    - `api_keys`: Array with one element showing the current API key and its usage
      - `key`: The API key used to make this request
      - `calls`: Number of API calls made using this specific key for the current billing period

    **Example Response:**
    ```json
    {
      \"calls\": 1250,
      \"api_keys\": [
        {
          \"key\": \"csa_live_abc123...\",
          \"calls\": 450
        }
      ]
    }
    ```

    **Use Cases:**
    - Monitor your API usage to stay within subscription limits
    - Track usage by individual API key
    - Identify which keys are making the most requests
    - Billing and cost tracking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SubscriptionInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
