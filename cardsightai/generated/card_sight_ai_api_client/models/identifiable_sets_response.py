from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.identifiable_set import IdentifiableSet


T = TypeVar("T", bound="IdentifiableSetsResponse")


@_attrs_define
class IdentifiableSetsResponse:
    """
    Attributes:
        sets (list['IdentifiableSet']): Identifiable sets for this page
        total_count (float): Total number of identifiable sets matching the query
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    sets: list["IdentifiableSet"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.identifiable_set import IdentifiableSet

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = IdentifiableSet.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        identifiable_sets_response = cls(
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return identifiable_sets_response
