from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.api_key_usage import ApiKeyUsage


T = TypeVar("T", bound="SubscriptionInfo")


@_attrs_define
class SubscriptionInfo:
    """
    Attributes:
        calls (int): Total aggregate number of API calls made across all API keys for the current billing period
        api_keys (list['ApiKeyUsage']): Array containing usage information for the current API key only
    """

    calls: int
    api_keys: list["ApiKeyUsage"]

    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calls": calls,
                "api_keys": api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_usage import ApiKeyUsage

        d = dict(src_dict)
        calls = d.pop("calls")

        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = ApiKeyUsage.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        subscription_info = cls(
            calls=calls,
            api_keys=api_keys,
        )

        return subscription_info
