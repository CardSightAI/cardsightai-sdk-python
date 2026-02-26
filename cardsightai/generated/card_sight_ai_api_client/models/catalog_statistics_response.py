from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_card_stats import CatalogCardStats
    from ..models.catalog_manufacturer_stats import CatalogManufacturerStats
    from ..models.catalog_parallel_stats import CatalogParallelStats
    from ..models.catalog_release_stats import CatalogReleaseStats
    from ..models.catalog_segment_stats import CatalogSegmentStats
    from ..models.catalog_set_stats import CatalogSetStats


T = TypeVar("T", bound="CatalogStatisticsResponse")


@_attrs_define
class CatalogStatisticsResponse:
    """
    Attributes:
        segments (CatalogSegmentStats):
        manufacturers (CatalogManufacturerStats):
        releases (CatalogReleaseStats):
        sets (CatalogSetStats):
        cards (CatalogCardStats):
        parallels (CatalogParallelStats):
    """

    segments: "CatalogSegmentStats"
    manufacturers: "CatalogManufacturerStats"
    releases: "CatalogReleaseStats"
    sets: "CatalogSetStats"
    cards: "CatalogCardStats"
    parallels: "CatalogParallelStats"

    def to_dict(self) -> dict[str, Any]:
        segments = self.segments.to_dict()

        manufacturers = self.manufacturers.to_dict()

        releases = self.releases.to_dict()

        sets = self.sets.to_dict()

        cards = self.cards.to_dict()

        parallels = self.parallels.to_dict()

        field_dict: dict[str, Any] = {}

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
        from ..models.catalog_card_stats import CatalogCardStats
        from ..models.catalog_manufacturer_stats import CatalogManufacturerStats
        from ..models.catalog_parallel_stats import CatalogParallelStats
        from ..models.catalog_release_stats import CatalogReleaseStats
        from ..models.catalog_segment_stats import CatalogSegmentStats
        from ..models.catalog_set_stats import CatalogSetStats

        d = dict(src_dict)
        segments = CatalogSegmentStats.from_dict(d.pop("segments"))

        manufacturers = CatalogManufacturerStats.from_dict(d.pop("manufacturers"))

        releases = CatalogReleaseStats.from_dict(d.pop("releases"))

        sets = CatalogSetStats.from_dict(d.pop("sets"))

        cards = CatalogCardStats.from_dict(d.pop("cards"))

        parallels = CatalogParallelStats.from_dict(d.pop("parallels"))

        catalog_statistics_response = cls(
            segments=segments,
            manufacturers=manufacturers,
            releases=releases,
            sets=sets,
            cards=cards,
            parallels=parallels,
        )

        return catalog_statistics_response
