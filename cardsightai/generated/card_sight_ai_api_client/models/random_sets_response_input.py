from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.random_sets_response_input_sets_item import RandomSetsResponseInputSetsItem


T = TypeVar("T", bound="RandomSetsResponseInput")


@_attrs_define
class RandomSetsResponseInput:
    """
    Attributes:
        sets (list['RandomSetsResponseInputSetsItem']): Array of random sets matching the specified filters
        count (float): Actual number of sets returned. May be less than requested count if insufficient matches.
    """

    sets: list["RandomSetsResponseInputSetsItem"]
    count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sets": sets,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.random_sets_response_input_sets_item import RandomSetsResponseInputSetsItem

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = RandomSetsResponseInputSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        count = d.pop("count")

        random_sets_response_input = cls(
            sets=sets,
            count=count,
        )

        random_sets_response_input.additional_properties = d
        return random_sets_response_input

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
