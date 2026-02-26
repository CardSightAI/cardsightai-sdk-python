from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.grading_company import GradingCompany


T = TypeVar("T", bound="GradingCompaniesResponse")


@_attrs_define
class GradingCompaniesResponse:
    """
    Attributes:
        companies (list['GradingCompany']): List of grading companies
        total (float): Total number of grading companies available
    """

    companies: list["GradingCompany"]
    total: float

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "companies": companies,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grading_company import GradingCompany

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = GradingCompany.from_dict(companies_item_data)

            companies.append(companies_item)

        total = d.pop("total")

        grading_companies_response = cls(
            companies=companies,
            total=total,
        )

        return grading_companies_response
