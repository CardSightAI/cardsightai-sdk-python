from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogCardStats")


@_attrs_define
class CatalogCardStats:
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

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        base = self.base

        variations = self.variations

        parallels = self.parallels

        field_dict: dict[str, Any] = {}

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

        catalog_card_stats = cls(
            total=total,
            base=base,
            variations=variations,
            parallels=parallels,
        )

        return catalog_card_stats
