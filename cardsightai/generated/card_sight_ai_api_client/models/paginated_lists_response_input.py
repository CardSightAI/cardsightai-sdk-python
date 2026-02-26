from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_input import ListInput


T = TypeVar("T", bound="PaginatedListsResponseInput")


@_attrs_define
class PaginatedListsResponseInput:
    """
    Attributes:
        lists (list['ListInput']): Array of list entities (want lists, collection goals, etc.)
        total_count (float): Total number of lists matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    lists: list["ListInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lists = []
        for lists_item_data in self.lists:
            lists_item = lists_item_data.to_dict()
            lists.append(lists_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.list_input import ListInput

        d = dict(src_dict)
        lists = []
        _lists = d.pop("lists")
        for lists_item_data in _lists:
            lists_item = ListInput.from_dict(lists_item_data)

            lists.append(lists_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_lists_response_input = cls(
            lists=lists,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_lists_response_input.additional_properties = d
        return paginated_lists_response_input

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
