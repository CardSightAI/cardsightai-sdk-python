from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collection_composition import CollectionComposition
    from ..models.collection_financials import CollectionFinancials
    from ..models.collection_overview import CollectionOverview


T = TypeVar("T", bound="CollectionAnalyticsResponse")


@_attrs_define
class CollectionAnalyticsResponse:
    """
    Attributes:
        overview (CollectionOverview):
        financials (CollectionFinancials):
        composition (CollectionComposition):
    """

    overview: "CollectionOverview"
    financials: "CollectionFinancials"
    composition: "CollectionComposition"

    def to_dict(self) -> dict[str, Any]:
        overview = self.overview.to_dict()

        financials = self.financials.to_dict()

        composition = self.composition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "overview": overview,
                "financials": financials,
                "composition": composition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_composition import CollectionComposition
        from ..models.collection_financials import CollectionFinancials
        from ..models.collection_overview import CollectionOverview

        d = dict(src_dict)
        overview = CollectionOverview.from_dict(d.pop("overview"))

        financials = CollectionFinancials.from_dict(d.pop("financials"))

        composition = CollectionComposition.from_dict(d.pop("composition"))

        collection_analytics_response = cls(
            overview=overview,
            financials=financials,
            composition=composition,
        )

        return collection_analytics_response
