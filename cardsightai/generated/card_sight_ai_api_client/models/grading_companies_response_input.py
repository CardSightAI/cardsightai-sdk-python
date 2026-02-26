from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grading_company_input import GradingCompanyInput


T = TypeVar("T", bound="GradingCompaniesResponseInput")


@_attrs_define
class GradingCompaniesResponseInput:
    """
    Attributes:
        companies (list['GradingCompanyInput']): List of grading companies
        total (float): Total number of grading companies available
    """

    companies: list["GradingCompanyInput"]
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companies": companies,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grading_company_input import GradingCompanyInput

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = GradingCompanyInput.from_dict(companies_item_data)

            companies.append(companies_item)

        total = d.pop("total")

        grading_companies_response_input = cls(
            companies=companies,
            total=total,
        )

        grading_companies_response_input.additional_properties = d
        return grading_companies_response_input

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
