from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetIdentifiableResponse")


@_attrs_define
class SetIdentifiableResponse:
    """
    Attributes:
        set_id (str): Set unique ID that was checked
        is_identifiable (bool): Whether this set is identifiable by the system
    """

    set_id: str
    is_identifiable: bool

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}

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

        set_identifiable_response = cls(
            set_id=set_id,
            is_identifiable=is_identifiable,
        )

        return set_identifiable_response
