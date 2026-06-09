from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.population_grading_type_input import PopulationGradingTypeInput


T = TypeVar("T", bound="ReleaseSetRollupInput")


@_attrs_define
class ReleaseSetRollupInput:
    """
    Attributes:
        set_id (str): Set UUID
        set_name (str): Set name (echoed for visual confirmation only)
        total_population (int): Total across all grading types for this set within the company
        grading_types (list['PopulationGradingTypeInput']):
    """

    set_id: str
    set_name: str
    total_population: int
    grading_types: list["PopulationGradingTypeInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        total_population = self.total_population

        grading_types = []
        for grading_types_item_data in self.grading_types:
            grading_types_item = grading_types_item_data.to_dict()
            grading_types.append(grading_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "set_id": set_id,
                "set_name": set_name,
                "total_population": total_population,
                "grading_types": grading_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.population_grading_type_input import PopulationGradingTypeInput

        d = dict(src_dict)
        set_id = d.pop("set_id")

        set_name = d.pop("set_name")

        total_population = d.pop("total_population")

        grading_types = []
        _grading_types = d.pop("grading_types")
        for grading_types_item_data in _grading_types:
            grading_types_item = PopulationGradingTypeInput.from_dict(grading_types_item_data)

            grading_types.append(grading_types_item)

        release_set_rollup_input = cls(
            set_id=set_id,
            set_name=set_name,
            total_population=total_population,
            grading_types=grading_types,
        )

        release_set_rollup_input.additional_properties = d
        return release_set_rollup_input

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
