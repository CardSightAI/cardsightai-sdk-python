"""Custom exceptions for the CardSight AI SDK"""

from typing import Any


class CardSightAIError(Exception):
    """Base exception for all CardSight AI SDK errors"""

    def __init__(self, message: str, request_id: str | None = None):
        super().__init__(message)
        self.message = message
        self.request_id = request_id


class AuthenticationError(CardSightAIError):
    """Raised when API authentication fails"""

    def __init__(self, message: str = "Invalid API key", request_id: str | None = None):
        super().__init__(message, request_id)


class RateLimitError(CardSightAIError):
    """Raised when API rate limit is exceeded"""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        request_id: str | None = None,
        retry_after: int | None = None,
    ):
        super().__init__(message, request_id)
        self.retry_after = retry_after


class APIError(CardSightAIError):
    """Raised for general API errors"""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        request_id: str | None = None,
        response_data: Any | None = None,
    ):
        super().__init__(message, request_id)
        self.status_code = status_code
        self.response_data = response_data
