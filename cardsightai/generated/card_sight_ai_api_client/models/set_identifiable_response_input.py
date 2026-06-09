from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SetIdentifiableResponseInput")


@_attrs_define
class SetIdentifiableResponseInput:
    """
    Attributes:
        set_id (str): Set unique ID that was checked
        is_identifiable (bool): Whether this set is identifiable by the system
    """

    set_id: str
    is_identifiable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "set_id": set_id,
                "is_identifiable": is_identifiable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_id = d.pop("set_id")

        is_identifiable = d.pop("is_identifiable")

        set_identifiable_response_input = cls(
            set_id=set_id,
            is_identifiable=is_identifiable,
        )

        set_identifiable_response_input.additional_properties = d
        return set_identifiable_response_input

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
