from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_release_year_breakdown_input import CatalogReleaseYearBreakdownInput


T = TypeVar("T", bound="CatalogReleaseBySegmentInput")


@_attrs_define
class CatalogReleaseBySegmentInput:
    """
    Attributes:
        segment_name (str): Segment name
        total (float): Total releases in this segment across all years
        by_year (list['CatalogReleaseYearBreakdownInput']): Year-by-year breakdown for this segment
    """

    segment_name: str
    total: float
    by_year: list["CatalogReleaseYearBreakdownInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_name = self.segment_name

        total = self.total

        by_year = []
        for by_year_item_data in self.by_year:
            by_year_item = by_year_item_data.to_dict()
            by_year.append(by_year_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.catalog_release_year_breakdown_input import CatalogReleaseYearBreakdownInput

        d = dict(src_dict)
        segment_name = d.pop("segmentName")

        total = d.pop("total")

        by_year = []
        _by_year = d.pop("byYear")
        for by_year_item_data in _by_year:
            by_year_item = CatalogReleaseYearBreakdownInput.from_dict(by_year_item_data)

            by_year.append(by_year_item)

        catalog_release_by_segment_input = cls(
            segment_name=segment_name,
            total=total,
            by_year=by_year,
        )

        catalog_release_by_segment_input.additional_properties = d
        return catalog_release_by_segment_input

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
