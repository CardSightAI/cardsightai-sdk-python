from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_card_stats_input import CatalogCardStatsInput
    from ..models.catalog_manufacturer_stats_input import CatalogManufacturerStatsInput
    from ..models.catalog_parallel_stats_input import CatalogParallelStatsInput
    from ..models.catalog_release_stats_input import CatalogReleaseStatsInput
    from ..models.catalog_segment_stats_input import CatalogSegmentStatsInput
    from ..models.catalog_set_stats_input import CatalogSetStatsInput


T = TypeVar("T", bound="CatalogStatisticsResponseInput")


@_attrs_define
class CatalogStatisticsResponseInput:
    """
    Attributes:
        segments (CatalogSegmentStatsInput):
        manufacturers (CatalogManufacturerStatsInput):
        releases (CatalogReleaseStatsInput):
        sets (CatalogSetStatsInput):
        cards (CatalogCardStatsInput):
        parallels (CatalogParallelStatsInput):
    """

    segments: "CatalogSegmentStatsInput"
    manufacturers: "CatalogManufacturerStatsInput"
    releases: "CatalogReleaseStatsInput"
    sets: "CatalogSetStatsInput"
    cards: "CatalogCardStatsInput"
    parallels: "CatalogParallelStatsInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments = self.segments.to_dict()

        manufacturers = self.manufacturers.to_dict()

        releases = self.releases.to_dict()

        sets = self.sets.to_dict()

        cards = self.cards.to_dict()

        parallels = self.parallels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segments": segments,
                "manufacturers": manufacturers,
                "releases": releases,
                "sets": sets,
                "cards": cards,
                "parallels": parallels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_card_stats_input import CatalogCardStatsInput
        from ..models.catalog_manufacturer_stats_input import CatalogManufacturerStatsInput
        from ..models.catalog_parallel_stats_input import CatalogParallelStatsInput
        from ..models.catalog_release_stats_input import CatalogReleaseStatsInput
        from ..models.catalog_segment_stats_input import CatalogSegmentStatsInput
        from ..models.catalog_set_stats_input import CatalogSetStatsInput

        d = dict(src_dict)
        segments = CatalogSegmentStatsInput.from_dict(d.pop("segments"))

        manufacturers = CatalogManufacturerStatsInput.from_dict(d.pop("manufacturers"))

        releases = CatalogReleaseStatsInput.from_dict(d.pop("releases"))

        sets = CatalogSetStatsInput.from_dict(d.pop("sets"))

        cards = CatalogCardStatsInput.from_dict(d.pop("cards"))

        parallels = CatalogParallelStatsInput.from_dict(d.pop("parallels"))

        catalog_statistics_response_input = cls(
            segments=segments,
            manufacturers=manufacturers,
            releases=releases,
            sets=sets,
            cards=cards,
            parallels=parallels,
        )

        catalog_statistics_response_input.additional_properties = d
        return catalog_statistics_response_input

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
