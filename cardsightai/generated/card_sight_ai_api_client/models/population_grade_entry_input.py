from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PopulationGradeEntryInput")


@_attrs_define
class PopulationGradeEntryInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

        population_grade_entry_input = cls(
            id=id,
            grade=grade,
            population=population,
            qualified_population=qualified_population,
            condition=condition,
        )

        population_grade_entry_input.additional_properties = d
        return population_grade_entry_input

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
