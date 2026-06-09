from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.population_grading_type import PopulationGradingType
    from ..models.release_set_rollup import ReleaseSetRollup


T = TypeVar("T", bound="ReleaseGradingCompanyPopulation")


@_attrs_define
class ReleaseGradingCompanyPopulation:
    """
    Attributes:
        id (str): Grading company UUID
        name (str): Grading company name
        last_synced_at (str): Most recent population sync timestamp for this company within this release (ISO 8601)
        total_population (int): Total across all sets and grading types in this release for this company
        grading_types (list['PopulationGradingType']): Aggregated populations across the entire release for this company
        sets (list['ReleaseSetRollup']): Per-set rollup. Sets with no data for this company are omitted.
    """

    id: str
    name: str
    last_synced_at: str
    total_population: int
    grading_types: list["PopulationGradingType"]
    sets: list["ReleaseSetRollup"]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        last_synced_at = self.last_synced_at

        total_population = self.total_population

        grading_types = []
        for grading_types_item_data in self.grading_types:
            grading_types_item = grading_types_item_data.to_dict()
            grading_types.append(grading_types_item)

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "last_synced_at": last_synced_at,
                "total_population": total_population,
                "grading_types": grading_types,
                "sets": sets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.population_grading_type import PopulationGradingType
        from ..models.release_set_rollup import ReleaseSetRollup

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

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = ReleaseSetRollup.from_dict(sets_item_data)

            sets.append(sets_item)

        release_grading_company_population = cls(
            id=id,
            name=name,
            last_synced_at=last_synced_at,
            total_population=total_population,
            grading_types=grading_types,
            sets=sets,
        )

        return release_grading_company_population
