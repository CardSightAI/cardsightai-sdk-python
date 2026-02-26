"""
CardSight AI Client Wrapper

This module provides a lightweight wrapper around the generated API client
that provides a cleaner interface while delegating to generated code.
"""

import asyncio
import inspect
import os
from importlib import import_module
from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO

import httpx

from .exceptions import AuthenticationError
from .generated.card_sight_ai_api_client import AuthenticatedClient


class APIModuleProxy:
    """
    Proxy that automatically wraps generated API module functions to inject the client.

    This allows calling:
        await client.catalog.get_statistics()

    Instead of:
        from cardsightai.generated...api.catalog import get_statistics
        await get_statistics.asyncio(client=client._client)
    """

    def __init__(self, module, client: AuthenticatedClient):
        self._module = module
        self._client = client

    def __getattr__(self, name: str):
        """Dynamically proxy attribute access to the underlying module"""
        # Import the submodule (e.g., catalog.get_statistics)
        try:
            from importlib import import_module

            # Get the full module path (e.g., 'cardsightai.generated...api.catalog')
            module_path = self._module.__name__
            # Import the endpoint module (e.g., 'cardsightai.generated...api.catalog.get_statistics')
            endpoint_module = import_module(f".{name}", module_path)

            # If it has an asyncio function, wrap it
            if hasattr(endpoint_module, "asyncio"):

                async def wrapped(**kwargs):
                    return await endpoint_module.asyncio(client=self._client, **kwargs)

                return wrapped

            return endpoint_module

        except (ImportError, AttributeError):
            # Fallback to direct attribute access
            return getattr(self._module, name)


class CardIdentificationHelper:
    """Helper for card identification with file upload support"""

    def __init__(self, client: AuthenticatedClient):
        self._client = client

    @staticmethod
    def _convert_image(image: str | Path | bytes | BinaryIO) -> bytes:
        """Convert various image input types to bytes."""
        if isinstance(image, (str, Path)):
            with open(image, "rb") as f:
                return f.read()
        elif isinstance(image, bytes):
            return image
        elif hasattr(image, "read"):
            return image.read()
        else:
            raise ValueError(f"Unsupported image type: {type(image)}")

    async def identify(
        self,
        image: str | Path | bytes | BinaryIO,
        **kwargs: Any,
    ):
        """
        Identify a trading card from an image.

        Args:
            image: Card image as file path, bytes, or file-like object
            **kwargs: Additional parameters to pass to the API

        Returns:
            Card identification result

        Example:
            >>> result = await client.identify.identify("card.jpg")
            >>> result = await client.identify.identify(image_bytes)
        """
        image_data = self._convert_image(image)

        from .generated.card_sight_ai_api_client.api.card_identification import identify_card
        from .generated.card_sight_ai_api_client.models.file_upload_input import FileUploadInput
        from .generated.card_sight_ai_api_client.types import File

        upload_input = FileUploadInput(image=File(payload=BytesIO(image_data)))
        return await identify_card.asyncio(client=self._client, body=upload_input, **kwargs)

    async def identify_by_segment(
        self,
        segment: str,
        image: str | Path | bytes | BinaryIO,
        **kwargs: Any,
    ):
        """
        Identify a trading card from an image for a specific segment (sport).

        Args:
            segment: Segment UUID or name (e.g., "football", "basketball")
            image: Card image as file path, bytes, or file-like object
            **kwargs: Additional parameters to pass to the API

        Returns:
            Card identification result

        Example:
            >>> result = await client.identify.identify_by_segment("football", "card.jpg")
        """
        image_data = self._convert_image(image)

        from .generated.card_sight_ai_api_client.api.card_identification import identify_card_by_segment
        from .generated.card_sight_ai_api_client.models.file_upload_input import FileUploadInput
        from .generated.card_sight_ai_api_client.types import File

        upload_input = FileUploadInput(image=File(payload=BytesIO(image_data)))
        return await identify_card_by_segment.asyncio(segment, client=self._client, body=upload_input, **kwargs)


class AsyncCardSightAI:
    """
    Async client for the CardSight AI API.

    This is a lightweight wrapper that exposes the generated API modules
    with automatic client injection, providing a clean interface without
    extensive proxy code.

    Args:
        api_key: Your CardSight AI API key. If not provided, will look for
                CARDSIGHTAI_API_KEY environment variable.
        base_url: Base URL for the API. Defaults to https://api.cardsight.ai
        timeout: Request timeout in seconds. Defaults to 30.
        **kwargs: Additional arguments to pass to the httpx client.

    Example:
        >>> async with AsyncCardSightAI() as client:
        ...     # Health check
        ...     health = await client.health.get_health()
        ...
        ...     # Catalog statistics
        ...     stats = await client.catalog.get_statistics()
        ...
        ...     # Identify a card (with file upload helper)
        ...     result = await client.identify.identify("card.jpg")
    """

    _MODULE_MAP = {
        "catalog": "catalog",
        "health": "health",
        "collections": "collection_management",
        "grades": "grades",
        "ai": "ai",
        "images": "images",
        "lists": "lists",
        "collectors": "collectors",
        "feedback": "feedback",
        "autocomplete": "autocomplete",
        "subscription": "subscription",
        "collection_images": "collection_card_images",
        "card_detection": "card_detection",
        "card_identification": "card_identification",
    }

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.cardsight.ai",
        timeout: float = 30.0,
        **kwargs: Any,
    ):
        # Get API key from parameter or environment
        api_key = api_key or os.getenv("CARDSIGHTAI_API_KEY")
        if not api_key:
            raise AuthenticationError(
                "API key is required. Provide it as a parameter or set CARDSIGHTAI_API_KEY environment variable."
            )

        # Allow override from environment
        base_url = os.getenv("CARDSIGHTAI_BASE_URL", base_url)
        timeout_env = os.getenv("CARDSIGHTAI_TIMEOUT")
        if timeout_env:
            timeout = float(timeout_env)

        # Create the authenticated client with X-API-Key header
        self._client = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=httpx.Timeout(timeout),
            headers={"X-API-Key": api_key},
            **kwargs,
        )

        # Lazily-loaded API module proxies
        self._api_modules: dict[str, APIModuleProxy] = {}

        # Special helper for card identification (file upload support)
        self.identify = CardIdentificationHelper(self._client)

    def __getattr__(self, name: str):
        if name in self._MODULE_MAP:
            if name not in self._api_modules:
                mod = import_module(
                    f".generated.card_sight_ai_api_client.api.{self._MODULE_MAP[name]}",
                    "cardsightai",
                )
                self._api_modules[name] = APIModuleProxy(mod, self._client)
            return self._api_modules[name]
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    async def __aenter__(self):
        """Async context manager entry"""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit - close httpx client"""
        await self._client.get_async_httpx_client().aclose()


class SyncWrapper:
    """
    Wrapper that converts async methods to sync by running them in an event loop.

    This enables synchronous usage of the async client without duplicating code.
    """

    def __init__(self, async_obj, loop):
        self._async_obj = async_obj
        self._loop = loop

    def __getattr__(self, name: str):
        """Dynamically wrap attributes"""
        attr = getattr(self._async_obj, name)

        # If it's an async function, wrap it to run synchronously
        if inspect.iscoroutinefunction(attr):

            def sync_wrapper(*args, **kwargs):
                return self._loop.run_until_complete(attr(*args, **kwargs))

            return sync_wrapper

        # If it's an object with async methods, recursively wrap it
        if hasattr(attr, "__dict__") or hasattr(attr, "__getattr__"):
            return SyncWrapper(attr, self._loop)

        return attr


class CardSightAI:
    """
    Synchronous client for the CardSight AI API.

    This wraps AsyncCardSightAI and runs async methods synchronously using
    a persistent event loop. Provides the same interface as the async client.

    Args:
        api_key: Your CardSight AI API key. If not provided, will look for
                CARDSIGHTAI_API_KEY environment variable.
        base_url: Base URL for the API. Defaults to https://api.cardsight.ai
        timeout: Request timeout in seconds. Defaults to 30.
        **kwargs: Additional arguments to pass to the httpx client.

    Example:
        >>> client = CardSightAI()
        >>>
        >>> # Health check
        >>> health = client.health.get_health()
        >>>
        >>> # Catalog statistics
        >>> stats = client.catalog.get_statistics()
        >>>
        >>> # Identify a card
        >>> result = client.identify.identify("card.jpg")
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.cardsight.ai",
        timeout: float = 30.0,
        **kwargs: Any,
    ):
        # Create async client
        self._async_client = AsyncCardSightAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            **kwargs,
        )

        # Create persistent event loop
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

    def __getattr__(self, name: str):
        """Proxy all attributes through SyncWrapper"""
        return SyncWrapper(getattr(self._async_client, name), self._loop)

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close client and loop"""
        # Close the httpx client synchronously
        self._async_client._client.get_httpx_client().close()

        # Close the event loop
        if self._loop and not self._loop.is_closed():
            self._loop.close()

    def close(self):
        """Explicitly close the client and event loop"""
        self.__exit__(None, None, None)


__all__ = ["AsyncCardSightAI", "CardSightAI"]
