from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.marketplace_grade_group import MarketplaceGradeGroup


T = TypeVar("T", bound="MarketplaceCompanyGroup")


@_attrs_define
class MarketplaceCompanyGroup:
    """
    Attributes:
        company_name (str): Grading company name
        company_id (UUID): Grading company UUID
        grades (list['MarketplaceGradeGroup']): Grade groups
    """

    company_name: str
    company_id: UUID
    grades: list["MarketplaceGradeGroup"]

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        company_id = str(self.company_id)

        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company_name": company_name,
                "company_id": company_id,
                "grades": grades,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_grade_group import MarketplaceGradeGroup

        d = dict(src_dict)
        company_name = d.pop("company_name")

        company_id = UUID(d.pop("company_id"))

        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = MarketplaceGradeGroup.from_dict(grades_item_data)

            grades.append(grades_item)

        marketplace_company_group = cls(
            company_name=company_name,
            company_id=company_id,
            grades=grades,
        )

        return marketplace_company_group
