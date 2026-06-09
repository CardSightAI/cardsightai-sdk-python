from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.release_grading_company_population_input import ReleaseGradingCompanyPopulationInput


T = TypeVar("T", bound="ReleasePopulationResponseInput")


@_attrs_define
class ReleasePopulationResponseInput:
    """
    Attributes:
        release_id (str): Release UUID (echoed back from the request)
        release_name (str): Release name (echoed for visual confirmation only)
        grading_companies (list['ReleaseGradingCompanyPopulationInput']): One entry per grading company that has any
            population data for cards in this release
    """

    release_id: str
    release_name: str
    grading_companies: list["ReleaseGradingCompanyPopulationInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        release_name = self.release_name

        grading_companies = []
        for grading_companies_item_data in self.grading_companies:
            grading_companies_item = grading_companies_item_data.to_dict()
            grading_companies.append(grading_companies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.release_grading_company_population_input import ReleaseGradingCompanyPopulationInput

        d = dict(src_dict)
        release_id = d.pop("release_id")

        release_name = d.pop("release_name")

        grading_companies = []
        _grading_companies = d.pop("grading_companies")
        for grading_companies_item_data in _grading_companies:
            grading_companies_item = ReleaseGradingCompanyPopulationInput.from_dict(grading_companies_item_data)

            grading_companies.append(grading_companies_item)

        release_population_response_input = cls(
            release_id=release_id,
            release_name=release_name,
            grading_companies=grading_companies,
        )

        release_population_response_input.additional_properties = d
        return release_population_response_input

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
