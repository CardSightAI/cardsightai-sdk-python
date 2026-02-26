from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_release_by_segment_input import CatalogReleaseBySegmentInput


T = TypeVar("T", bound="CatalogReleaseStatsInput")


@_attrs_define
class CatalogReleaseStatsInput:
    """
    Attributes:
        total (float): Total number of releases across all years
        by_segment (list['CatalogReleaseBySegmentInput']): Breakdown by segment, then by year
    """

    total: float
    by_segment: list["CatalogReleaseBySegmentInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_segment = []
        for by_segment_item_data in self.by_segment:
            by_segment_item = by_segment_item_data.to_dict()
            by_segment.append(by_segment_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "bySegment": by_segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_release_by_segment_input import CatalogReleaseBySegmentInput

        d = dict(src_dict)
        total = d.pop("total")

        by_segment = []
        _by_segment = d.pop("bySegment")
        for by_segment_item_data in _by_segment:
            by_segment_item = CatalogReleaseBySegmentInput.from_dict(by_segment_item_data)

            by_segment.append(by_segment_item)

        catalog_release_stats_input = cls(
            total=total,
            by_segment=by_segment,
        )

        catalog_release_stats_input.additional_properties = d
        return catalog_release_stats_input

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
