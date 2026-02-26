from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.breakdown_group import BreakdownGroup
    from ..models.breakdown_pagination import BreakdownPagination
    from ..models.collection_breakdown_summary import CollectionBreakdownSummary


T = TypeVar("T", bound="CollectionBreakdownResponse")


@_attrs_define
class CollectionBreakdownResponse:
    """
    Attributes:
        summary (CollectionBreakdownSummary):
        groups (list['BreakdownGroup']): Array of breakdown groups
        pagination (BreakdownPagination):
    """

    summary: "CollectionBreakdownSummary"
    groups: list["BreakdownGroup"]
    pagination: "BreakdownPagination"

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

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
        from ..models.breakdown_group import BreakdownGroup
        from ..models.breakdown_pagination import BreakdownPagination
        from ..models.collection_breakdown_summary import CollectionBreakdownSummary

        d = dict(src_dict)
        summary = CollectionBreakdownSummary.from_dict(d.pop("summary"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = BreakdownGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        pagination = BreakdownPagination.from_dict(d.pop("pagination"))

        collection_breakdown_response = cls(
            summary=summary,
            groups=groups,
            pagination=pagination,
        )

        return collection_breakdown_response
