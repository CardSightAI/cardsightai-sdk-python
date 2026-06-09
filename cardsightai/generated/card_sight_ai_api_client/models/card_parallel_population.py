from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.variant_grading_company_population import VariantGradingCompanyPopulation


T = TypeVar("T", bound="CardParallelPopulation")


@_attrs_define
class CardParallelPopulation:
    """
    Attributes:
        parallel_id (str): Parallel UUID
        parallel_name (str): Parallel name (echoed for visual confirmation only)
        total_population (int): Total across all grading companies for this parallel
        grading_companies (list['VariantGradingCompanyPopulation']):
    """

    parallel_id: str
    parallel_name: str
    total_population: int
    grading_companies: list["VariantGradingCompanyPopulation"]

    def to_dict(self) -> dict[str, Any]:
        parallel_id = self.parallel_id

        parallel_name = self.parallel_name

        total_population = self.total_population

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "parallel_id": parallel_id,
                "parallel_name": parallel_name,
                "total_population": total_population,
                "grading_companies": grading_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_grading_company_population import VariantGradingCompanyPopulation

        d = dict(src_dict)
        parallel_id = d.pop("parallel_id")

        parallel_name = d.pop("parallel_name")

        total_population = d.pop("total_population")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = VariantGradingCompanyPopulation.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        card_parallel_population = cls(
            parallel_id=parallel_id,
            parallel_name=parallel_name,
            total_population=total_population,
            grading_companies=grading_companies,
        )

        return card_parallel_population
