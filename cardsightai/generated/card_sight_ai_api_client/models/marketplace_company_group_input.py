from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketplace_grade_group_input import MarketplaceGradeGroupInput


T = TypeVar("T", bound="MarketplaceCompanyGroupInput")


@_attrs_define
class MarketplaceCompanyGroupInput:
    """
    Attributes:
        company_name (str): Grading company name
        company_id (UUID): Grading company UUID
        grades (list['MarketplaceGradeGroupInput']): Grade groups
    """

    company_name: str
    company_id: UUID
    grades: list["MarketplaceGradeGroupInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        company_id = str(self.company_id)

        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.marketplace_grade_group_input import MarketplaceGradeGroupInput

        d = dict(src_dict)
        company_name = d.pop("company_name")

        company_id = UUID(d.pop("company_id"))

        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = MarketplaceGradeGroupInput.from_dict(grades_item_data)

            grades.append(grades_item)

        marketplace_company_group_input = cls(
            company_name=company_name,
            company_id=company_id,
            grades=grades,
        )

        marketplace_company_group_input.additional_properties = d
        return marketplace_company_group_input

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
