"""Pytest configuration and shared fixtures"""

import pytest


@pytest.fixture(autouse=True)
def reset_environment(monkeypatch):
    """Reset environment variables for each test"""
    # Remove API key from environment to ensure tests are explicit
    monkeypatch.delenv("CARDSIGHTAI_API_KEY", raising=False)
    monkeypatch.delenv("CARDSIGHTAI_BASE_URL", raising=False)
    monkeypatch.delenv("CARDSIGHTAI_TIMEOUT", raising=False)


@pytest.fixture
def mock_api_key():
    """Provide a test API key"""
    return "test_api_key_12345"


@pytest.fixture
def mock_base_url():
    """Provide a test base URL"""
    return "https://api.test.cardsight.ai"
