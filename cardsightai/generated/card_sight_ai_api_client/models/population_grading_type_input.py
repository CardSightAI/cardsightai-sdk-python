from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.population_grade_entry_input import PopulationGradeEntryInput


T = TypeVar("T", bound="PopulationGradingTypeInput")


@_attrs_define
class PopulationGradingTypeInput:
    """
    Attributes:
        id (str): Grading type UUID
        name (str): Grading type name (e.g. "Standard")
        total_population (int): Sum of population + qualified_population across all grades for this type
        grades (list['PopulationGradeEntryInput']): Every grade for this type, with zero-fill for grades without data
    """

    id: str
    name: str
    total_population: int
    grades: list["PopulationGradeEntryInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        total_population = self.total_population

        grades = []
        for grades_item_data in self.grades:
            grades_item = grades_item_data.to_dict()
            grades.append(grades_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.population_grade_entry_input import PopulationGradeEntryInput

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        total_population = d.pop("total_population")

        grades = []
        _grades = d.pop("grades")
        for grades_item_data in _grades:
            grades_item = PopulationGradeEntryInput.from_dict(grades_item_data)

            grades.append(grades_item)

        population_grading_type_input = cls(
            id=id,
            name=name,
            total_population=total_population,
            grades=grades,
        )

        population_grading_type_input.additional_properties = d
        return population_grading_type_input

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
