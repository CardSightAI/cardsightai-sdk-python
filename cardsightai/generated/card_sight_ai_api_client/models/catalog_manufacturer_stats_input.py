from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_manufacturer_breakdown_item_input import CatalogManufacturerBreakdownItemInput


T = TypeVar("T", bound="CatalogManufacturerStatsInput")


@_attrs_define
class CatalogManufacturerStatsInput:
    """
    Attributes:
        total (float): Total number of manufacturers
        breakdown (list['CatalogManufacturerBreakdownItemInput']): All manufacturers with their release counts
    """

    total: float
    breakdown: list["CatalogManufacturerBreakdownItemInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        breakdown = []
        for breakdown_item_data in self.breakdown:
            breakdown_item = breakdown_item_data.to_dict()
            breakdown.append(breakdown_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "breakdown": breakdown,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_manufacturer_breakdown_item_input import CatalogManufacturerBreakdownItemInput

        d = dict(src_dict)
        total = d.pop("total")

        breakdown = []
        _breakdown = d.pop("breakdown")
        for breakdown_item_data in _breakdown:
            breakdown_item = CatalogManufacturerBreakdownItemInput.from_dict(breakdown_item_data)

            breakdown.append(breakdown_item)

        catalog_manufacturer_stats_input = cls(
            total=total,
            breakdown=breakdown,
        )

        catalog_manufacturer_stats_input.additional_properties = d
        return catalog_manufacturer_stats_input

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
