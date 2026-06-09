from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_base_population_input import CardBasePopulationInput
    from ..models.card_parallel_population_input import CardParallelPopulationInput


T = TypeVar("T", bound="CardPopulationResponseInput")


@_attrs_define
class CardPopulationResponseInput:
    """
    Attributes:
        card_id (str): Card UUID (echoed back from the request)
        card_name (str): Card name (echoed for visual confirmation only)
        total_population (int): Top-level total: base + every parallel, every company, every grade
        parallels (list['CardParallelPopulationInput']): One entry per parallel that has any population data. Parallels
            with no data are omitted.
        base (Union[Unset, CardBasePopulationInput]):
    """

    card_id: str
    card_name: str
    total_population: int
    parallels: list["CardParallelPopulationInput"]
    base: Union[Unset, "CardBasePopulationInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.card_base_population_input import CardBasePopulationInput
        from ..models.card_parallel_population_input import CardParallelPopulationInput

        d = dict(src_dict)
        card_id = d.pop("card_id")

        card_name = d.pop("card_name")

        total_population = d.pop("total_population")

        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = CardParallelPopulationInput.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        _base = d.pop("base", UNSET)
        base: Union[Unset, CardBasePopulationInput]
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = CardBasePopulationInput.from_dict(_base)

        card_population_response_input = cls(
            card_id=card_id,
            card_name=card_name,
            total_population=total_population,
            parallels=parallels,
            base=base,
        )

        card_population_response_input.additional_properties = d
        return card_population_response_input

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
