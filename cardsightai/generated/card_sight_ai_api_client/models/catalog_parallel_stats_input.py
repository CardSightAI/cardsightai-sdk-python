from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogParallelStatsInput")


@_attrs_define
class CatalogParallelStatsInput:
    """
    Attributes:
        total (float): Total number of parallel types
        full_set (float): Count of full set parallels (apply to entire set)
        partial (float): Count of partial parallels (apply to specific cards only)
    """

    total: float
    full_set: float
    partial: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        full_set = self.full_set

        partial = self.partial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        catalog_parallel_stats_input = cls(
            total=total,
            full_set=full_set,
            partial=partial,
        )

        catalog_parallel_stats_input.additional_properties = d
        return catalog_parallel_stats_input

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
