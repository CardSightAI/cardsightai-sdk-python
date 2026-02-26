from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogCardStatsInput")


@_attrs_define
class CatalogCardStatsInput:
    """
    Attributes:
        total (float): Total cards including all parallel versions
        base (float): Base cards (non-parallel, non-variation)
        variations (float): Variation cards (non-parallel)
        parallels (float): Total parallel card instances
    """

    total: float
    base: float
    variations: float
    parallels: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        base = self.base

        variations = self.variations

        parallels = self.parallels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "base": base,
                "variations": variations,
                "parallels": parallels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        base = d.pop("base")

        variations = d.pop("variations")

        parallels = d.pop("parallels")

        catalog_card_stats_input = cls(
            total=total,
            base=base,
            variations=variations,
            parallels=parallels,
        )

        catalog_card_stats_input.additional_properties = d
        return catalog_card_stats_input

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
