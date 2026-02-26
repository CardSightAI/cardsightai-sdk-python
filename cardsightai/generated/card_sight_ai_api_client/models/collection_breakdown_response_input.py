from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.breakdown_group_input import BreakdownGroupInput
    from ..models.breakdown_pagination_input import BreakdownPaginationInput
    from ..models.collection_breakdown_summary_input import CollectionBreakdownSummaryInput


T = TypeVar("T", bound="CollectionBreakdownResponseInput")


@_attrs_define
class CollectionBreakdownResponseInput:
    """
    Attributes:
        summary (CollectionBreakdownSummaryInput):
        groups (list['BreakdownGroupInput']): Array of breakdown groups
        pagination (BreakdownPaginationInput):
    """

    summary: "CollectionBreakdownSummaryInput"
    groups: list["BreakdownGroupInput"]
    pagination: "BreakdownPaginationInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "groups": groups,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breakdown_group_input import BreakdownGroupInput
        from ..models.breakdown_pagination_input import BreakdownPaginationInput
        from ..models.collection_breakdown_summary_input import CollectionBreakdownSummaryInput

        d = dict(src_dict)
        summary = CollectionBreakdownSummaryInput.from_dict(d.pop("summary"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = BreakdownGroupInput.from_dict(groups_item_data)

            groups.append(groups_item)

        pagination = BreakdownPaginationInput.from_dict(d.pop("pagination"))

        collection_breakdown_response_input = cls(
            summary=summary,
            groups=groups,
            pagination=pagination,
        )

        collection_breakdown_response_input.additional_properties = d
        return collection_breakdown_response_input

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
