from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_segment_breakdown_item import CatalogSegmentBreakdownItem


T = TypeVar("T", bound="CatalogSegmentStats")


@_attrs_define
class CatalogSegmentStats:
    """
    Attributes:
        total (float): Total number of segments
        breakdown (list['CatalogSegmentBreakdownItem']): Breakdown of segments with release counts
    """

    total: float
    breakdown: list["CatalogSegmentBreakdownItem"]

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        breakdown = []
        for breakdown_item_data in self.breakdown:
            breakdown_item = breakdown_item_data.to_dict()
            breakdown.append(breakdown_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "breakdown": breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_segment_breakdown_item import CatalogSegmentBreakdownItem

        d = dict(src_dict)
        total = d.pop("total")

        breakdown = []
        _breakdown = d.pop("breakdown")
        for breakdown_item_data in _breakdown:
            breakdown_item = CatalogSegmentBreakdownItem.from_dict(breakdown_item_data)

            breakdown.append(breakdown_item)

        catalog_segment_stats = cls(
            total=total,
            breakdown=breakdown,
        )

        return catalog_segment_stats
