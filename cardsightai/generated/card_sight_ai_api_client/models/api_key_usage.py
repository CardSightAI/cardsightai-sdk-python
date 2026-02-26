from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ApiKeyUsage")


@_attrs_define
class ApiKeyUsage:
    """
    Attributes:
        key (str): The API key (masked or full depending on context)
        calls (int): Total number of API calls made using this key for the current billing period
    """

    key: str
    calls: int

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        calls = self.calls

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "calls": calls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        calls = d.pop("calls")

        api_key_usage = cls(
            key=key,
            calls=calls,
        )

        return api_key_usage
