from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.list_ import List


T = TypeVar("T", bound="PaginatedListsResponse")


@_attrs_define
class PaginatedListsResponse:
    """
    Attributes:
        lists (list['List']): Array of list entities (want lists, collection goals, etc.)
        total_count (float): Total number of lists matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    lists: list["List"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        lists = []
        for lists_item_data in self.lists:
            lists_item = lists_item_data.to_dict()
            lists.append(lists_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lists": lists,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_ import List

        d = dict(src_dict)
        lists = []
        _lists = d.pop("lists")
        for lists_item_data in _lists:
            lists_item = List.from_dict(lists_item_data)

            lists.append(lists_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_lists_response = cls(
            lists=lists,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_lists_response
