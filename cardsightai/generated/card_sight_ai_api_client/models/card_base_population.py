from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.variant_grading_company_population import VariantGradingCompanyPopulation


T = TypeVar("T", bound="CardBasePopulation")


@_attrs_define
class CardBasePopulation:
    """
    Attributes:
        total_population (int): Total across all grading companies for the base card
        grading_companies (list['VariantGradingCompanyPopulation']):
    """

    total_population: int
    grading_companies: list["VariantGradingCompanyPopulation"]

    def to_dict(self) -> dict[str, Any]:
        total_population = self.total_population

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total_population": total_population,
                "grading_companies": grading_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_grading_company_population import VariantGradingCompanyPopulation

        d = dict(src_dict)
        total_population = d.pop("total_population")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = VariantGradingCompanyPopulation.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        card_base_population = cls(
            total_population=total_population,
            grading_companies=grading_companies,
        )

        return card_base_population
