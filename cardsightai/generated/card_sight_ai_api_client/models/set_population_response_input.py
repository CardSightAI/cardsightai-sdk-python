from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.aggregated_grading_company_population_input import AggregatedGradingCompanyPopulationInput


T = TypeVar("T", bound="SetPopulationResponseInput")


@_attrs_define
class SetPopulationResponseInput:
    """
    Attributes:
        set_id (str): Set UUID (echoed back from the request)
        set_name (str): Set name (echoed for visual confirmation only)
        grading_companies (list['AggregatedGradingCompanyPopulationInput']): One entry per grading company that has any
            population data for cards in this set
    """

    set_id: str
    set_name: str
    grading_companies: list["AggregatedGradingCompanyPopulationInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "set_id": set_id,
                "set_name": set_name,
                "grading_companies": grading_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregated_grading_company_population_input import AggregatedGradingCompanyPopulationInput

        d = dict(src_dict)
        set_id = d.pop("set_id")

        set_name = d.pop("set_name")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = AggregatedGradingCompanyPopulationInput.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        set_population_response_input = cls(
            set_id=set_id,
            set_name=set_name,
            grading_companies=grading_companies,
        )

        set_population_response_input.additional_properties = d
        return set_population_response_input

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
