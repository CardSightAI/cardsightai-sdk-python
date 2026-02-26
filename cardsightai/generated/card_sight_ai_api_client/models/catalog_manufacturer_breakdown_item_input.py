from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogManufacturerBreakdownItemInput")


@_attrs_define
class CatalogManufacturerBreakdownItemInput:
    """
    Attributes:
        id (UUID): Manufacturer unique identifier
        name (str): Manufacturer name
        release_count (float): Number of releases by this manufacturer
    """

    id: UUID
    name: str
    release_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        release_count = self.release_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "releaseCount": release_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        release_count = d.pop("releaseCount")

        catalog_manufacturer_breakdown_item_input = cls(
            id=id,
            name=name,
            release_count=release_count,
        )

        catalog_manufacturer_breakdown_item_input.additional_properties = d
        return catalog_manufacturer_breakdown_item_input

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
