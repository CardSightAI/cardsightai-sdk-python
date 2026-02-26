from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogParallelStats")


@_attrs_define
class CatalogParallelStats:
    """
    Attributes:
        total (float): Total number of parallel types
        full_set (float): Count of full set parallels (apply to entire set)
        partial (float): Count of partial parallels (apply to specific cards only)
    """

    total: float
    full_set: float
    partial: float

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        full_set = self.full_set

        partial = self.partial

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "fullSet": full_set,
                "partial": partial,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        full_set = d.pop("fullSet")

        partial = d.pop("partial")

        catalog_parallel_stats = cls(
            total=total,
            full_set=full_set,
            partial=partial,
        )

        return catalog_parallel_stats
