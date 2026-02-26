from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogManufacturerBreakdownItem")


@_attrs_define
class CatalogManufacturerBreakdownItem:
    """
    Attributes:
        id (UUID): Manufacturer unique identifier
        name (str): Manufacturer name
        release_count (float): Number of releases by this manufacturer
    """

    id: UUID
    name: str
    release_count: float

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        release_count = self.release_count

        field_dict: dict[str, Any] = {}

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

        catalog_manufacturer_breakdown_item = cls(
            id=id,
            name=name,
            release_count=release_count,
        )

        return catalog_manufacturer_breakdown_item
