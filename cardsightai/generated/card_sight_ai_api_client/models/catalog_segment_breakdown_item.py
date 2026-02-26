from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogSegmentBreakdownItem")


@_attrs_define
class CatalogSegmentBreakdownItem:
    """
    Attributes:
        id (UUID): Segment unique identifier
        name (str): Segment name
        count (float): Number of releases in this segment
    """

    id: UUID
    name: str
    count: float

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        count = d.pop("count")

        catalog_segment_breakdown_item = cls(
            id=id,
            name=name,
            count=count,
        )

        return catalog_segment_breakdown_item
