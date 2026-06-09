from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.identifiable_set_input import IdentifiableSetInput


T = TypeVar("T", bound="IdentifiableSetsResponseInput")


@_attrs_define
class IdentifiableSetsResponseInput:
    """
    Attributes:
        sets (list['IdentifiableSetInput']): Identifiable sets for this page
        total_count (float): Total number of identifiable sets matching the query
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    sets: list["IdentifiableSetInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sets": sets,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identifiable_set_input import IdentifiableSetInput

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = IdentifiableSetInput.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        identifiable_sets_response_input = cls(
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        identifiable_sets_response_input.additional_properties = d
        return identifiable_sets_response_input

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
