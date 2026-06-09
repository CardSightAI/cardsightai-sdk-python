from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.source_breakdown_item import SourceBreakdownItem


T = TypeVar("T", bound="MarketplaceMeta")


@_attrs_define
class MarketplaceMeta:
    """
    Attributes:
        sources (list['SourceBreakdownItem']): Breakdown by data source
        total_records (int): Total records returned
    """

    sources: list["SourceBreakdownItem"]
    total_records: int

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        total_records = self.total_records

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sources": sources,
                "total_records": total_records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_breakdown_item import SourceBreakdownItem

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceBreakdownItem.from_dict(sources_item_data)

            sources.append(sources_item)

        total_records = d.pop("total_records")

        marketplace_meta = cls(
            sources=sources,
            total_records=total_records,
        )

        return marketplace_meta
