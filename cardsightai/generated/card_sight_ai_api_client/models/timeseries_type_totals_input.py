from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TimeseriesTypeTotalsInput")


@_attrs_define
class TimeseriesTypeTotalsInput:
    """
    Attributes:
        total_count (int): Listings included across all candles for this listing type (after outlier filtering); equals
            the sum of the per-candle counts.
        filtered_count (int): Listings removed by the outlier filter for this listing type. Pre-filter total =
            total_count + filtered_count.
    """

    total_count: int
    filtered_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        filtered_count = self.filtered_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "filtered_count": filtered_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("total_count")

        filtered_count = d.pop("filtered_count")

        timeseries_type_totals_input = cls(
            total_count=total_count,
            filtered_count=filtered_count,
        )

        timeseries_type_totals_input.additional_properties = d
        return timeseries_type_totals_input

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
