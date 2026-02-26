from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.paginated_sets_response_sets_item import PaginatedSetsResponseSetsItem


T = TypeVar("T", bound="PaginatedSetsResponse")


@_attrs_define
class PaginatedSetsResponse:
    """
    Attributes:
        sets (list['PaginatedSetsResponseSetsItem']): Array of set entities with card counts and release information
        total_count (float): Total number of sets matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    sets: list["PaginatedSetsResponseSetsItem"]
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
        from ..models.paginated_sets_response_sets_item import PaginatedSetsResponseSetsItem

        d = dict(src_dict)
        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = PaginatedSetsResponseSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_sets_response = cls(
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_sets_response
