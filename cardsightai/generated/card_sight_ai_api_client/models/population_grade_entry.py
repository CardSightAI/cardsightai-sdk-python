from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PopulationGradeEntry")


@_attrs_define
class PopulationGradeEntry:
    """
    Attributes:
        id (str): Grade UUID
        grade (str): Grade value (e.g. "10", "9.5")
        population (int): Count of unqualified graded examples
        qualified_population (int): Count of qualified graded examples (e.g. PSA "8Q")
        condition (Union[None, Unset, str]): Condition descriptor (e.g. "Gem Mint")
    """

    id: str
    grade: str
    population: int
    qualified_population: int
    condition: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        grade = self.grade

        population = self.population

        qualified_population = self.qualified_population

        condition: Union[None, Unset, str]
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "grade": grade,
                "population": population,
                "qualified_population": qualified_population,
            }
        )
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        grade = d.pop("grade")

        population = d.pop("population")

        qualified_population = d.pop("qualified_population")

        def _parse_condition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        condition = _parse_condition(d.pop("condition", UNSET))

        population_grade_entry = cls(
            id=id,
            grade=grade,
            population=population,
            qualified_population=qualified_population,
            condition=condition,
        )

        return population_grade_entry
