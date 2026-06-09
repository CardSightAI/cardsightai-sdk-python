from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.release_grading_company_population import ReleaseGradingCompanyPopulation


T = TypeVar("T", bound="ReleasePopulationResponse")


@_attrs_define
class ReleasePopulationResponse:
    """
    Attributes:
        release_id (str): Release UUID (echoed back from the request)
        release_name (str): Release name (echoed for visual confirmation only)
        grading_companies (list['ReleaseGradingCompanyPopulation']): One entry per grading company that has any
            population data for cards in this release
    """

    release_id: str
    release_name: str
    grading_companies: list["ReleaseGradingCompanyPopulation"]

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        release_name = self.release_name

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "release_id": release_id,
                "release_name": release_name,
                "grading_companies": grading_companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_grading_company_population import ReleaseGradingCompanyPopulation

        d = dict(src_dict)
        release_id = d.pop("release_id")

        release_name = d.pop("release_name")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = ReleaseGradingCompanyPopulation.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        release_population_response = cls(
            release_id=release_id,
            release_name=release_name,
            grading_companies=grading_companies,
        )

        return release_population_response
