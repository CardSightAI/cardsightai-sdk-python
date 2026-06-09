from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.aggregated_grading_company_population import AggregatedGradingCompanyPopulation


T = TypeVar("T", bound="SetPopulationResponse")


@_attrs_define
class SetPopulationResponse:
    """
    Attributes:
        set_id (str): Set UUID (echoed back from the request)
        set_name (str): Set name (echoed for visual confirmation only)
        grading_companies (list['AggregatedGradingCompanyPopulation']): One entry per grading company that has any
            population data for cards in this set
    """

    set_id: str
    set_name: str
    grading_companies: list["AggregatedGradingCompanyPopulation"]

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}

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
        from ..models.aggregated_grading_company_population import AggregatedGradingCompanyPopulation

        d = dict(src_dict)
        set_id = d.pop("set_id")

        set_name = d.pop("set_name")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = AggregatedGradingCompanyPopulation.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        set_population_response = cls(
            set_id=set_id,
            set_name=set_name,
            grading_companies=grading_companies,
        )

        return set_population_response
