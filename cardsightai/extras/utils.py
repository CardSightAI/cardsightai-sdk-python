"""Utility functions for the CardSight AI SDK"""

from pathlib import Path
from typing import Any


def get_highest_confidence_detection(detections: list[dict[str, Any]] | dict[str, Any]) -> dict[str, Any] | None:
    """
    Extract the detection with the highest confidence level from identification results.

    Args:
        detections: Either a list of detections or a response dict containing detections

    Returns:
        The detection with the highest confidence, or None if no detections found

    Example:
        >>> result = client.identify.card("card.jpg")
        >>> best_match = get_highest_confidence_detection(result)
        >>> if best_match:
        ...     print(f"Card: {best_match['card']['name']}")
        ...     print(f"Confidence: {best_match['confidence']}")
    """
    # Handle response wrapper format
    items: list[dict[str, Any]] | dict[str, Any] = detections
    if isinstance(items, dict):
        if "data" in items:
            items = items["data"]
        if isinstance(items, dict) and "detections" in items:
            items = items["detections"]

    if not isinstance(items, list) or not items:
        return None
    detections = items

    # Define confidence level ordering
    confidence_levels = {"High": 3, "Medium": 2, "Low": 1}

    # Sort detections by confidence level
    sorted_detections = sorted(
        detections, key=lambda d: confidence_levels.get(d.get("confidence", "Low"), 0), reverse=True
    )

    return sorted_detections[0] if sorted_detections else None


def validate_image_file(
    file_path: str | Path, max_size_mb: float = 10.0, allowed_formats: list[str] | None = None
) -> Path:
    """
    Validate an image file for upload.

    Args:
        file_path: Path to the image file
        max_size_mb: Maximum allowed file size in megabytes (default: 10MB)
        allowed_formats: List of allowed file extensions (default: jpeg, jpg, png, webp)

    Returns:
        Validated Path object

    Raises:
        ValueError: If the file is invalid (doesn't exist, too large, wrong format)

    Example:
        >>> image_path = validate_image_file("card.jpg")
        >>> result = client.identify.card(image_path)
    """
    if allowed_formats is None:
        allowed_formats = [".jpeg", ".jpg", ".png", ".webp"]

    file_path = Path(file_path)

    # Check if file exists
    if not file_path.exists():
        raise ValueError(f"File not found: {file_path}")

    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    # Check file format
    file_ext = file_path.suffix.lower()
    if file_ext not in allowed_formats:
        raise ValueError(f"Invalid file format '{file_ext}'. Allowed formats: {', '.join(allowed_formats)}")

    # Check file size
    file_size_mb = file_path.stat().st_size / (1024 * 1024)
    if file_size_mb > max_size_mb:
        raise ValueError(f"File size ({file_size_mb:.2f} MB) exceeds maximum allowed size ({max_size_mb} MB)")

    return file_path


class PaginationIterator:
    """
    Iterator for paginated API results.

    This class provides automatic pagination handling for list endpoints.

    Example:
        >>> async for card in PaginationIterator(client.catalog.cards.list, take=100):
        ...     print(card['name'])
    """

    def __init__(self, fetch_func, take: int = 20, **kwargs):
        """
        Initialize the pagination iterator.

        Args:
            fetch_func: The async function to call for fetching results
            take: Number of results to fetch per page
            **kwargs: Additional keyword arguments to pass to the fetch function
        """
        self.fetch_func = fetch_func
        self.take = take
        self.kwargs = kwargs
        self.skip = 0
        self.total_count = None
        self.current_items: list[Any] = []
        self.current_index = 0

    def __aiter__(self):
        """Return the async iterator"""
        return self

    async def __anext__(self):
        """Get the next item from pagination"""
        # If we've exhausted current items, fetch more
        if self.current_index >= len(self.current_items):
            await self._fetch_next_page()

            # If no more items after fetching, stop iteration
            if not self.current_items:
                raise StopAsyncIteration

            self.current_index = 0

        # Return the next item
        item = self.current_items[self.current_index]
        self.current_index += 1
        return item

    async def _fetch_next_page(self):
        """Fetch the next page of results"""
        # If we know the total and have fetched all, stop
        if self.total_count is not None and self.skip >= self.total_count:
            self.current_items = []
            return

        # Fetch the next page
        result = await self.fetch_func(skip=self.skip, take=self.take, **self.kwargs)

        # Extract items and total count from result
        if isinstance(result, dict):
            # Handle response wrapper
            data = result.get("data", result)

            # Extract items based on the endpoint type
            # The key might be "cards", "releases", "sets", etc.
            items_key = None
            for key in data.keys():
                if isinstance(data[key], list):
                    items_key = key
                    break

            if items_key:
                self.current_items = data[items_key]
                self.total_count = data.get("total_count", self.total_count)
            else:
                self.current_items = []
        else:
            self.current_items = []

        self.skip += self.take


def create_pagination_iterator(fetch_func, **kwargs):
    """
    Create a pagination iterator for a list endpoint.

    Args:
        fetch_func: The async function to call for fetching results
        **kwargs: Arguments to pass to PaginationIterator

    Returns:
        PaginationIterator instance

    Example:
        >>> iterator = create_pagination_iterator(client.catalog.cards.list, take=100)
        >>> async for card in iterator:
        ...     print(card['name'])
    """
    return PaginationIterator(fetch_func, **kwargs)
