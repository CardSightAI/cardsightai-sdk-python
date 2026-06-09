from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FieldValue")


@_attrs_define
class FieldValue:
    """
    Attributes:
        key (str): Field key (e.g., "HP", "Rarity", "Artist")
        value (str): Field value for the given key
    """

    key: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        field_value = cls(
            key=key,
            value=value,
        )

        return field_value
