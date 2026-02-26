from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.random_sets_response_sets_item import RandomSetsResponseSetsItem


T = TypeVar("T", bound="RandomSetsResponse")


@_attrs_define
class RandomSetsResponse:
    """
    Attributes:
        sets (list['RandomSetsResponseSetsItem']): Array of random sets matching the specified filters
        count (float): Actual number of sets returned. May be less than requested count if insufficient matches.
    """

    sets: list["RandomSetsResponseSetsItem"]
    count: float

    def to_dict(self) -> dict[str, Any]:
        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sets": sets,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.random_sets_response_sets_item import RandomSetsResponseSetsItem

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = RandomSetsResponseSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        count = d.pop("count")

        random_sets_response = cls(
            sets=sets,
            count=count,
        )

        return random_sets_response
