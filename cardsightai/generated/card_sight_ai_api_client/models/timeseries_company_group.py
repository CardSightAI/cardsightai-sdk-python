from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.timeseries_grade_group import TimeseriesGradeGroup


T = TypeVar("T", bound="TimeseriesCompanyGroup")


@_attrs_define
class TimeseriesCompanyGroup:
    """
    Attributes:
        company_name (str): Grading company name (e.g., "PSA")
        company_id (UUID): Grading company UUID
        grades (list['TimeseriesGradeGroup']): Per-grade candle series for this company
    """

    company_name: str
    company_id: UUID
    grades: list["TimeseriesGradeGroup"]

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
        from ..models.timeseries_grade_group import TimeseriesGradeGroup

        d = dict(src_dict)
        company_name = d.pop("company_name")

        company_id = UUID(d.pop("company_id"))

        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = TimeseriesGradeGroup.from_dict(grades_item_data)

            grades.append(grades_item)

        timeseries_company_group = cls(
            company_name=company_name,
            company_id=company_id,
            grades=grades,
        )

        return timeseries_company_group
