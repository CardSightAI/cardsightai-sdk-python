from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_release_by_segment import CatalogReleaseBySegment


T = TypeVar("T", bound="CatalogReleaseStats")


@_attrs_define
class CatalogReleaseStats:
    """
    Attributes:
        total (float): Total number of releases across all years
        by_segment (list['CatalogReleaseBySegment']): Breakdown by segment, then by year
    """

    total: float
    by_segment: list["CatalogReleaseBySegment"]

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_segment = []
        for by_segment_item_data in self.by_segment:
            by_segment_item = by_segment_item_data.to_dict()
            by_segment.append(by_segment_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "bySegment": by_segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_release_by_segment import CatalogReleaseBySegment

        d = dict(src_dict)
        total = d.pop("total")

        by_segment = []
        _by_segment = d.pop("bySegment")
        for by_segment_item_data in _by_segment:
            by_segment_item = CatalogReleaseBySegment.from_dict(by_segment_item_data)

            by_segment.append(by_segment_item)

        catalog_release_stats = cls(
            total=total,
            by_segment=by_segment,
        )

        return catalog_release_stats
