from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.grade import Grade
    from ..models.grading_company import GradingCompany
    from ..models.grading_type import GradingType


T = TypeVar("T", bound="GradesResponse")


@_attrs_define
class GradesResponse:
    """
    Attributes:
        grades (list['Grade']): List of specific grade values available for this grading type
        total (float): Total number of grades for this grading type
        grading_type (GradingType):
        grading_company (GradingCompany):
    """

    grades: list["Grade"]
    total: float
    grading_type: "GradingType"
    grading_company: "GradingCompany"

    def to_dict(self) -> dict[str, Any]:
        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        total = self.total

        grading_type = self.grading_type.to_dict()

        grading_company = self.grading_company.to_dict()

        field_dict: dict[str, Any] = {}

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
        from ..models.grade import Grade
        from ..models.grading_company import GradingCompany
        from ..models.grading_type import GradingType

        d = dict(src_dict)
        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = Grade.from_dict(grades_item_data)

            grades.append(grades_item)

        total = d.pop("total")

        grading_type = GradingType.from_dict(d.pop("gradingType"))

        grading_company = GradingCompany.from_dict(d.pop("gradingCompany"))

        grades_response = cls(
            grades=grades,
            total=total,
            grading_type=grading_type,
            grading_company=grading_company,
        )

        return grades_response
