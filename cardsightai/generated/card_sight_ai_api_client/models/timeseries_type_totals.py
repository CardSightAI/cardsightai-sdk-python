from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TimeseriesTypeTotals")


@_attrs_define
class TimeseriesTypeTotals:
    """
    Attributes:
        total_count (int): Listings included across all candles for this listing type (after outlier filtering); equals
            the sum of the per-candle counts.
        filtered_count (int): Listings removed by the outlier filter for this listing type. Pre-filter total =
            total_count + filtered_count.
    """

    total_count: int
    filtered_count: int

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        filtered_count = self.filtered_count

        field_dict: dict[str, Any] = {}

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

        timeseries_type_totals = cls(
            total_count=total_count,
            filtered_count=filtered_count,
        )

        return timeseries_type_totals
