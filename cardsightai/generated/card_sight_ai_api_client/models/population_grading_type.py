from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.population_grade_entry import PopulationGradeEntry


T = TypeVar("T", bound="PopulationGradingType")


@_attrs_define
class PopulationGradingType:
    """
    Attributes:
        id (str): Grading type UUID
        name (str): Grading type name (e.g. "Standard")
        total_population (int): Sum of population + qualified_population across all grades for this type
        grades (list['PopulationGradeEntry']): Every grade for this type, with zero-fill for grades without data
    """

    id: str
    name: str
    total_population: int
    grades: list["PopulationGradeEntry"]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        total_population = self.total_population

        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "total_population": total_population,
                "grades": grades,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.population_grade_entry import PopulationGradeEntry

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        total_population = d.pop("total_population")

        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = PopulationGradeEntry.from_dict(grades_item_data)

            grades.append(grades_item)

        population_grading_type = cls(
            id=id,
            name=name,
            total_population=total_population,
            grades=grades,
        )

        return population_grading_type
