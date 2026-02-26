"""Unit tests for CardSight AI client wrappers"""

import asyncio
import inspect
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from cardsightai import AsyncCardSightAI, CardSightAI
from cardsightai.client import APIModuleProxy, CardIdentificationHelper
from cardsightai.exceptions import AuthenticationError


class TestClientInitialization:
    """Test client initialization"""

    def test_sync_client_requires_api_key(self):
        """Test that sync client requires API key"""
        with pytest.raises(AuthenticationError):
            CardSightAI()

    def test_sync_client_accepts_api_key(self):
        """Test that sync client accepts API key parameter"""
        client = CardSightAI(api_key="test_key")
        assert client is not None

    def test_sync_client_uses_env_var(self, monkeypatch):
        """Test that sync client uses CARDSIGHTAI_API_KEY env var"""
        monkeypatch.setenv("CARDSIGHTAI_API_KEY", "test_key_from_env")
        client = CardSightAI()
        assert client is not None

    def test_async_client_requires_api_key(self):
        """Test that async client requires API key"""
        with pytest.raises(AuthenticationError):
            AsyncCardSightAI()

    def test_async_client_accepts_api_key(self):
        """Test that async client accepts API key parameter"""
        client = AsyncCardSightAI(api_key="test_key")
        assert client is not None

    def test_async_client_uses_env_var(self, monkeypatch):
        """Test that async client uses CARDSIGHTAI_API_KEY env var"""
        monkeypatch.setenv("CARDSIGHTAI_API_KEY", "test_key_from_env")
        client = AsyncCardSightAI()
        assert client is not None

    def test_async_client_custom_base_url(self):
        """Test that custom base_url is accepted without error"""
        client = AsyncCardSightAI(api_key="test_key", base_url="https://custom.api.com")
        assert client is not None

    def test_async_client_env_base_url(self, monkeypatch):
        """Test that CARDSIGHTAI_BASE_URL env var is accepted without error"""
        monkeypatch.setenv("CARDSIGHTAI_BASE_URL", "https://env.api.com")
        client = AsyncCardSightAI(api_key="test_key")
        assert client is not None

    def test_async_client_env_timeout(self, monkeypatch):
        """Test that CARDSIGHTAI_TIMEOUT env var is accepted without error"""
        monkeypatch.setenv("CARDSIGHTAI_TIMEOUT", "60")
        client = AsyncCardSightAI(api_key="test_key")
        assert client is not None


class TestClientProperties:
    """Test that all expected top-level properties exist on both clients"""

    EXPECTED_MODULE_ATTRS = [
        "catalog",
        "health",
        "collections",
        "grades",
        "ai",
        "images",
        "lists",
        "collectors",
        "feedback",
        "autocomplete",
        "subscription",
        "collection_images",
        "card_detection",
        "card_identification",
    ]

    @pytest.fixture
    def async_client(self):
        return AsyncCardSightAI(api_key="test_key")

    @pytest.fixture
    def sync_client(self):
        return CardSightAI(api_key="test_key")

    @pytest.mark.parametrize("attr", EXPECTED_MODULE_ATTRS)
    def test_async_client_has_module_attr(self, async_client, attr):
        """Test that async client exposes API module proxy"""
        proxy = getattr(async_client, attr)
        assert isinstance(proxy, APIModuleProxy)

    @pytest.mark.parametrize("attr", EXPECTED_MODULE_ATTRS)
    def test_sync_client_has_module_attr(self, sync_client, attr):
        """Test that sync client exposes API module proxy (via SyncWrapper)"""
        proxy = getattr(sync_client, attr)
        assert proxy is not None

    def test_async_client_has_identify(self, async_client):
        """Test that async client has identify helper"""
        assert isinstance(async_client.identify, CardIdentificationHelper)

    def test_sync_client_has_identify(self, sync_client):
        """Test that sync client has identify helper"""
        assert sync_client.identify is not None

    def test_async_client_invalid_attr_raises(self, async_client):
        """Test that accessing a nonexistent attribute raises AttributeError"""
        with pytest.raises(AttributeError, match="has no attribute"):
            _ = async_client.nonexistent_module


class TestAPIModuleProxy:
    """Test that APIModuleProxy exposes generated function names as callables"""

    @pytest.fixture
    def async_client(self):
        return AsyncCardSightAI(api_key="test_key")

    def test_catalog_get_statistics(self, async_client):
        func = async_client.catalog.get_statistics
        assert callable(func)

    def test_catalog_get_segments(self, async_client):
        func = async_client.catalog.get_segments
        assert callable(func)

    def test_catalog_get_card(self, async_client):
        func = async_client.catalog.get_card
        assert callable(func)

    def test_catalog_get_cards(self, async_client):
        func = async_client.catalog.get_cards
        assert callable(func)

    def test_catalog_get_manufacturers(self, async_client):
        func = async_client.catalog.get_manufacturers
        assert callable(func)

    def test_catalog_get_releases(self, async_client):
        func = async_client.catalog.get_releases
        assert callable(func)

    def test_catalog_get_sets(self, async_client):
        func = async_client.catalog.get_sets
        assert callable(func)

    def test_catalog_get_attributes(self, async_client):
        func = async_client.catalog.get_attributes
        assert callable(func)

    def test_catalog_get_parallels(self, async_client):
        func = async_client.catalog.get_parallels
        assert callable(func)

    def test_health_get_health(self, async_client):
        func = async_client.health.get_health
        assert callable(func)

    def test_health_get_health_authenticated(self, async_client):
        func = async_client.health.get_health_authenticated
        assert callable(func)

    def test_collections_create_collection(self, async_client):
        func = async_client.collections.create_collection
        assert callable(func)

    def test_collections_get_collections(self, async_client):
        func = async_client.collections.get_collections
        assert callable(func)

    def test_collections_get_collection_analytics(self, async_client):
        func = async_client.collections.get_collection_analytics
        assert callable(func)

    def test_grades_get_grading_companies(self, async_client):
        func = async_client.grades.get_grading_companies
        assert callable(func)

    def test_grades_get_grading_types(self, async_client):
        func = async_client.grades.get_grading_types
        assert callable(func)

    def test_ai_process_ai_query(self, async_client):
        func = async_client.ai.process_ai_query
        assert callable(func)

    def test_images_get_card_image(self, async_client):
        func = async_client.images.get_card_image
        assert callable(func)

    def test_lists_create_list(self, async_client):
        func = async_client.lists.create_list
        assert callable(func)

    def test_lists_get_lists(self, async_client):
        func = async_client.lists.get_lists
        assert callable(func)

    def test_collectors_get_collectors(self, async_client):
        func = async_client.collectors.get_collectors
        assert callable(func)

    def test_feedback_get_feedback(self, async_client):
        func = async_client.feedback.get_feedback
        assert callable(func)

    def test_feedback_submit_general_feedback(self, async_client):
        func = async_client.feedback.submit_general_feedback
        assert callable(func)

    def test_autocomplete_autocomplete_cards(self, async_client):
        func = async_client.autocomplete.autocomplete_cards
        assert callable(func)

    def test_autocomplete_autocomplete_segments(self, async_client):
        func = async_client.autocomplete.autocomplete_segments
        assert callable(func)

    def test_subscription_get_subscription(self, async_client):
        func = async_client.subscription.get_subscription
        assert callable(func)

    def test_collection_images_get_collection_card_image(self, async_client):
        func = async_client.collection_images.get_collection_card_image
        assert callable(func)

    def test_card_detection_detect_card(self, async_client):
        func = async_client.card_detection.detect_card
        assert callable(func)

    def test_card_identification_identify_card(self, async_client):
        func = async_client.card_identification.identify_card
        assert callable(func)

    def test_card_identification_identify_card_by_segment(self, async_client):
        func = async_client.card_identification.identify_card_by_segment
        assert callable(func)


class TestLazyLoading:
    """Test that API modules are lazily loaded"""

    def test_api_modules_starts_empty(self):
        client = AsyncCardSightAI(api_key="test_key")
        assert len(client._api_modules) == 0

    def test_accessing_module_populates_cache(self):
        client = AsyncCardSightAI(api_key="test_key")
        _ = client.catalog
        assert "catalog" in client._api_modules

    def test_same_proxy_returned_on_repeated_access(self):
        client = AsyncCardSightAI(api_key="test_key")
        proxy1 = client.catalog
        proxy2 = client.catalog
        assert proxy1 is proxy2

    def test_different_modules_cached_independently(self):
        client = AsyncCardSightAI(api_key="test_key")
        _ = client.catalog
        _ = client.health
        assert len(client._api_modules) == 2
        assert "catalog" in client._api_modules
        assert "health" in client._api_modules

    def test_identify_not_in_api_modules(self):
        """identify is a helper, not a lazy-loaded module proxy"""
        client = AsyncCardSightAI(api_key="test_key")
        _ = client.identify
        assert "identify" not in client._api_modules


class TestCardIdentificationHelper:
    """Test CardIdentificationHelper methods"""

    @pytest.fixture
    def async_client(self):
        return AsyncCardSightAI(api_key="test_key")

    def test_identify_method_exists(self, async_client):
        assert hasattr(async_client.identify, "identify")
        assert callable(async_client.identify.identify)
        assert inspect.iscoroutinefunction(async_client.identify.identify)

    def test_identify_by_segment_method_exists(self, async_client):
        assert hasattr(async_client.identify, "identify_by_segment")
        assert callable(async_client.identify.identify_by_segment)
        assert inspect.iscoroutinefunction(async_client.identify.identify_by_segment)

    def test_convert_image_from_bytes(self):
        data = b"fake image bytes"
        result = CardIdentificationHelper._convert_image(data)
        assert result == data

    def test_convert_image_from_file_like(self):
        from io import BytesIO
        data = b"fake image bytes"
        buf = BytesIO(data)
        result = CardIdentificationHelper._convert_image(buf)
        assert result == data

    def test_convert_image_from_path(self, tmp_path):
        img_file = tmp_path / "test.jpg"
        img_file.write_bytes(b"fake image bytes")
        result = CardIdentificationHelper._convert_image(str(img_file))
        assert result == b"fake image bytes"

    def test_convert_image_from_pathlib(self, tmp_path):
        img_file = tmp_path / "test.jpg"
        img_file.write_bytes(b"fake image bytes")
        result = CardIdentificationHelper._convert_image(img_file)
        assert result == b"fake image bytes"

    def test_convert_image_unsupported_type(self):
        with pytest.raises(ValueError, match="Unsupported image type"):
            CardIdentificationHelper._convert_image(12345)


class TestContextManagers:
    """Test context manager support"""

    def test_sync_client_context_manager(self):
        with CardSightAI(api_key="test_key") as client:
            assert client is not None

    @pytest.mark.asyncio
    async def test_async_client_context_manager(self):
        async with AsyncCardSightAI(api_key="test_key") as client:
            assert client is not None


class TestSyncWrapper:
    """Test that SyncWrapper properly converts async to sync"""

    @pytest.fixture
    def client(self):
        return CardSightAI(api_key="test_key")

    def test_sync_wrapper_returns_callable(self, client):
        """Sync-wrapped module proxy methods should be callable (not coroutines)"""
        func = client.catalog.get_statistics
        assert callable(func)
        assert not inspect.iscoroutinefunction(func)

    def test_sync_client_uses_async_client_internally(self):
        client = CardSightAI(api_key="test_key")
        assert hasattr(client, "_async_client")
        assert isinstance(client._async_client, AsyncCardSightAI)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
