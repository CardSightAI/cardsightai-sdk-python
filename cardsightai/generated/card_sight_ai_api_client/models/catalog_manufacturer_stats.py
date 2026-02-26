from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.catalog_manufacturer_breakdown_item import CatalogManufacturerBreakdownItem


T = TypeVar("T", bound="CatalogManufacturerStats")


@_attrs_define
class CatalogManufacturerStats:
    """
    Attributes:
        total (float): Total number of manufacturers
        breakdown (list['CatalogManufacturerBreakdownItem']): All manufacturers with their release counts
    """

    total: float
    breakdown: list["CatalogManufacturerBreakdownItem"]

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        breakdown = []
        for breakdown_item_data in self.breakdown:
            breakdown_item = breakdown_item_data.to_dict()
            breakdown.append(breakdown_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "breakdown": breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_manufacturer_breakdown_item import CatalogManufacturerBreakdownItem

        d = dict(src_dict)
        total = d.pop("total")

        breakdown = []
        _breakdown = d.pop("breakdown")
        for breakdown_item_data in _breakdown:
            breakdown_item = CatalogManufacturerBreakdownItem.from_dict(breakdown_item_data)

            breakdown.append(breakdown_item)

        catalog_manufacturer_stats = cls(
            total=total,
            breakdown=breakdown,
        )

        return catalog_manufacturer_stats
