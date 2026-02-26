from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_sets_response_input_sets_item import PaginatedSetsResponseInputSetsItem


T = TypeVar("T", bound="PaginatedSetsResponseInput")


@_attrs_define
class PaginatedSetsResponseInput:
    """
    Attributes:
        sets (list['PaginatedSetsResponseInputSetsItem']): Array of set entities with card counts and release
            information
        total_count (float): Total number of sets matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    sets: list["PaginatedSetsResponseInputSetsItem"]
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
        from ..models.paginated_sets_response_input_sets_item import PaginatedSetsResponseInputSetsItem

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = PaginatedSetsResponseInputSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_sets_response_input = cls(
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_sets_response_input.additional_properties = d
        return paginated_sets_response_input

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
