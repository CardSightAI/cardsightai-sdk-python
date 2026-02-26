from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.manufacturer import Manufacturer


T = TypeVar("T", bound="PaginatedManufacturersResponse")


@_attrs_define
class PaginatedManufacturersResponse:
    """
    Attributes:
        manufacturers (list['Manufacturer']): Array of card manufacturer entities (e.g., Topps, Panini, Upper Deck)
        total_count (float): Total number of manufacturers matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    manufacturers: list["Manufacturer"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        manufacturers = []
        for manufacturers_item_data in self.manufacturers:
            manufacturers_item = manufacturers_item_data.to_dict()
            manufacturers.append(manufacturers_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "manufacturers": manufacturers,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.manufacturer import Manufacturer

        d = dict(src_dict)
        manufacturers = []
        _manufacturers = d.pop("manufacturers")
        for manufacturers_item_data in _manufacturers:
            manufacturers_item = Manufacturer.from_dict(manufacturers_item_data)

            manufacturers.append(manufacturers_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_manufacturers_response = cls(
            manufacturers=manufacturers,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_manufacturers_response
