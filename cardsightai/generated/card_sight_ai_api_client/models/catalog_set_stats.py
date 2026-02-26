from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogSetStats")


@_attrs_define
class CatalogSetStats:
    """
    Attributes:
        total (float): Total number of card sets
        identifiable (float): Number of sets that can be recognized by AI
    """

    total: float
    identifiable: float

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        identifiable = self.identifiable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "identifiable": identifiable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        identifiable = d.pop("identifiable")

        catalog_set_stats = cls(
            total=total,
            identifiable=identifiable,
        )

        return catalog_set_stats
