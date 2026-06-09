from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.population_grading_type import PopulationGradingType


T = TypeVar("T", bound="AggregatedGradingCompanyPopulation")


@_attrs_define
class AggregatedGradingCompanyPopulation:
    """
    Attributes:
        id (str): Grading company UUID
        name (str): Grading company name
        last_synced_at (str): Most recent population sync timestamp for this company within this aggregation (ISO 8601)
        total_population (int): Total across all grading types for this company in the requested set/release
        grading_types (list['PopulationGradingType']):
    """

    id: str
    name: str
    last_synced_at: str
    total_population: int
    grading_types: list["PopulationGradingType"]

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
        from ..models.population_grading_type import PopulationGradingType

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        last_synced_at = d.pop("last_synced_at")

        total_population = d.pop("total_population")

        grading_types = []
        _grading_types = d.pop("grading_types")
        for grading_types_item_data in _grading_types:
            grading_types_item = PopulationGradingType.from_dict(grading_types_item_data)

            grading_types.append(grading_types_item)

        aggregated_grading_company_population = cls(
            id=id,
            name=name,
            last_synced_at=last_synced_at,
            total_population=total_population,
            grading_types=grading_types,
        )

        return aggregated_grading_company_population
