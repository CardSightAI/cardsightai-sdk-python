from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.variant_grading_company_population_input import VariantGradingCompanyPopulationInput


T = TypeVar("T", bound="CardBasePopulationInput")


@_attrs_define
class CardBasePopulationInput:
    """
    Attributes:
        total_population (int): Total across all grading companies for the base card
        grading_companies (list['VariantGradingCompanyPopulationInput']):
    """

    total_population: int
    grading_companies: list["VariantGradingCompanyPopulationInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_population = self.total_population

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_population": total_population,
                "grading_companies": grading_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_grading_company_population_input import VariantGradingCompanyPopulationInput

        d = dict(src_dict)
        total_population = d.pop("total_population")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = VariantGradingCompanyPopulationInput.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        card_base_population_input = cls(
            total_population=total_population,
            grading_companies=grading_companies,
        )

        card_base_population_input.additional_properties = d
        return card_base_population_input

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
