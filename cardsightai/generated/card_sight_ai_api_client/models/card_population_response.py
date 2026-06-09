from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_base_population import CardBasePopulation
    from ..models.card_parallel_population import CardParallelPopulation


T = TypeVar("T", bound="CardPopulationResponse")


@_attrs_define
class CardPopulationResponse:
    """
    Attributes:
        card_id (str): Card UUID (echoed back from the request)
        card_name (str): Card name (echoed for visual confirmation only)
        total_population (int): Top-level total: base + every parallel, every company, every grade
        parallels (list['CardParallelPopulation']): One entry per parallel that has any population data. Parallels with
            no data are omitted.
        base (Union[Unset, CardBasePopulation]):
    """

    card_id: str
    card_name: str
    total_population: int
    parallels: list["CardParallelPopulation"]
    base: Union[Unset, "CardBasePopulation"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        card_name = self.card_name

        total_population = self.total_population

        parallels = []
        for parallels_item_data in self.parallels:
            parallels_item = parallels_item_data.to_dict()
            parallels.append(parallels_item)

        base: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "card_id": card_id,
                "card_name": card_name,
                "total_population": total_population,
                "parallels": parallels,
            }
        )
        if base is not UNSET:
            field_dict["base"] = base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_base_population import CardBasePopulation
        from ..models.card_parallel_population import CardParallelPopulation

        d = dict(src_dict)
        card_id = d.pop("card_id")

        card_name = d.pop("card_name")

        total_population = d.pop("total_population")

        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = CardParallelPopulation.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        _base = d.pop("base", UNSET)
        base: Union[Unset, CardBasePopulation]
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = CardBasePopulation.from_dict(_base)

        card_population_response = cls(
            card_id=card_id,
            card_name=card_name,
            total_population=total_population,
            parallels=parallels,
            base=base,
        )

        return card_population_response
