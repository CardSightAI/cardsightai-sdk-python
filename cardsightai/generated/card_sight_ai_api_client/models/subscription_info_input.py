from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_key_usage_input import ApiKeyUsageInput


T = TypeVar("T", bound="SubscriptionInfoInput")


@_attrs_define
class SubscriptionInfoInput:
    """
    Attributes:
        calls (int): Total aggregate number of API calls made across all API keys for the current billing period
        api_keys (list['ApiKeyUsageInput']): Array containing usage information for the current API key only
    """

    calls: int
    api_keys: list["ApiKeyUsageInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        api_keys = []
        for api_keys_item_data in self.api_keys:
            api_keys_item = api_keys_item_data.to_dict()
            api_keys.append(api_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calls": calls,
                "api_keys": api_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_usage_input import ApiKeyUsageInput

        d = dict(src_dict)
        calls = d.pop("calls")

        api_keys = []
        _api_keys = d.pop("api_keys")
        for api_keys_item_data in _api_keys:
            api_keys_item = ApiKeyUsageInput.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        subscription_info_input = cls(
            calls=calls,
            api_keys=api_keys,
        )

        subscription_info_input.additional_properties = d
        return subscription_info_input

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
