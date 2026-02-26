from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_release_year_breakdown import CatalogReleaseYearBreakdown


T = TypeVar("T", bound="CatalogReleaseBySegment")


@_attrs_define
class CatalogReleaseBySegment:
    """
    Attributes:
        segment_name (str): Segment name
        total (float): Total releases in this segment across all years
        by_year (list['CatalogReleaseYearBreakdown']): Year-by-year breakdown for this segment
    """

    segment_name: str
    total: float
    by_year: list["CatalogReleaseYearBreakdown"]

    def to_dict(self) -> dict[str, Any]:
        segment_name = self.segment_name

        total = self.total

        by_year = []
        for by_year_item_data in self.by_year:
            by_year_item = by_year_item_data.to_dict()
            by_year.append(by_year_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segmentName": segment_name,
                "total": total,
                "byYear": by_year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_release_year_breakdown import CatalogReleaseYearBreakdown

        d = dict(src_dict)
        segment_name = d.pop("segmentName")

        total = d.pop("total")

        by_year = []
        _by_year = d.pop("byYear")
        for by_year_item_data in _by_year:
            by_year_item = CatalogReleaseYearBreakdown.from_dict(by_year_item_data)

            by_year.append(by_year_item)

        catalog_release_by_segment = cls(
            segment_name=segment_name,
            total=total,
            by_year=by_year,
        )

        return catalog_release_by_segment
