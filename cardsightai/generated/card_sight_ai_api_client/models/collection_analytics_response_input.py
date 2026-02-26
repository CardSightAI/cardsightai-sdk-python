from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection_composition_input import CollectionCompositionInput
    from ..models.collection_financials_input import CollectionFinancialsInput
    from ..models.collection_overview_input import CollectionOverviewInput
    from ..models.collection_performance_input import CollectionPerformanceInput


T = TypeVar("T", bound="CollectionAnalyticsResponseInput")


@_attrs_define
class CollectionAnalyticsResponseInput:
    """
    Attributes:
        overview (CollectionOverviewInput):
        financials (CollectionFinancialsInput):
        composition (CollectionCompositionInput):
        performance (CollectionPerformanceInput):
    """

    overview: "CollectionOverviewInput"
    financials: "CollectionFinancialsInput"
    composition: "CollectionCompositionInput"
    performance: "CollectionPerformanceInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overview = self.overview.to_dict()

        financials = self.financials.to_dict()

        composition = self.composition.to_dict()

        performance = self.performance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overview": overview,
                "financials": financials,
                "composition": composition,
                "performance": performance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_composition_input import CollectionCompositionInput
        from ..models.collection_financials_input import CollectionFinancialsInput
        from ..models.collection_overview_input import CollectionOverviewInput
        from ..models.collection_performance_input import CollectionPerformanceInput

        d = dict(src_dict)
        overview = CollectionOverviewInput.from_dict(d.pop("overview"))

        financials = CollectionFinancialsInput.from_dict(d.pop("financials"))

        composition = CollectionCompositionInput.from_dict(d.pop("composition"))

        performance = CollectionPerformanceInput.from_dict(d.pop("performance"))

        collection_analytics_response_input = cls(
            overview=overview,
            financials=financials,
            composition=composition,
            performance=performance,
        )

        collection_analytics_response_input.additional_properties = d
        return collection_analytics_response_input

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
