from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grade_input import GradeInput
    from ..models.grading_company_input import GradingCompanyInput
    from ..models.grading_type_input import GradingTypeInput


T = TypeVar("T", bound="GradesResponseInput")


@_attrs_define
class GradesResponseInput:
    """
    Attributes:
        grades (list['GradeInput']): List of specific grade values available for this grading type
        total (float): Total number of grades for this grading type
        grading_type (GradingTypeInput):
        grading_company (GradingCompanyInput):
    """

    grades: list["GradeInput"]
    total: float
    grading_type: "GradingTypeInput"
    grading_company: "GradingCompanyInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        total = self.total

        grading_type = self.grading_type.to_dict()

        grading_company = self.grading_company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grades": grades,
                "total": total,
                "gradingType": grading_type,
                "gradingCompany": grading_company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grade_input import GradeInput
        from ..models.grading_company_input import GradingCompanyInput
        from ..models.grading_type_input import GradingTypeInput

        d = dict(src_dict)
        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = GradeInput.from_dict(grades_item_data)

            grades.append(grades_item)

        total = d.pop("total")

        grading_type = GradingTypeInput.from_dict(d.pop("gradingType"))

        grading_company = GradingCompanyInput.from_dict(d.pop("gradingCompany"))

        grades_response_input = cls(
            grades=grades,
            total=total,
            grading_type=grading_type,
            grading_company=grading_company,
        )

        grades_response_input.additional_properties = d
        return grades_response_input

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
