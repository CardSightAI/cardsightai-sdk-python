from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.population_grading_type_input import PopulationGradingTypeInput


T = TypeVar("T", bound="VariantGradingCompanyPopulationInput")


@_attrs_define
class VariantGradingCompanyPopulationInput:
    """
    Attributes:
        id (str): Grading company UUID
        name (str): Grading company name (e.g. "PSA")
        last_synced_at (str): Most recent population sync timestamp for this company within this variant (ISO 8601)
        total_population (int): Sum across all grading types for this company within this variant
        grading_types (list['PopulationGradingTypeInput']):
    """

    id: str
    name: str
    last_synced_at: str
    total_population: int
    grading_types: list["PopulationGradingTypeInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        last_synced_at = self.last_synced_at

        total_population = self.total_population

        grading_types = []
        for grading_types_item_data in self.grading_types:
            grading_types_item = grading_types_item_data.to_dict()
            grading_types.append(grading_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "last_synced_at": last_synced_at,
                "total_population": total_population,
                "grading_types": grading_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.population_grading_type_input import PopulationGradingTypeInput

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        last_synced_at = d.pop("last_synced_at")

        total_population = d.pop("total_population")

        grading_types = []
        _grading_types = d.pop("grading_types")
        for grading_types_item_data in _grading_types:
            grading_types_item = PopulationGradingTypeInput.from_dict(grading_types_item_data)

            grading_types.append(grading_types_item)

        variant_grading_company_population_input = cls(
            id=id,
            name=name,
            last_synced_at=last_synced_at,
            total_population=total_population,
            grading_types=grading_types,
        )

        variant_grading_company_population_input.additional_properties = d
        return variant_grading_company_population_input

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
