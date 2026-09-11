from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CandleStatsInput")


@_attrs_define
class CandleStatsInput:
    """
    Attributes:
        mean (float): Arithmetic mean listing price in USD for this bucket. For auction candles this aggregates final
            sale prices; for fixed candles it aggregates Buy It Now asking prices (not necessarily completed sales).
        median (float): Median listing price in USD for this bucket
        high (float): Highest listing price in USD in this bucket
        low (float): Lowest listing price in USD in this bucket
        count (int): Number of listings in this bucket for this listing type (after outlier filtering)
    """

    mean: float
    median: float
    high: float
    low: float
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mean = self.mean

        median = self.median

        high = self.high

        low = self.low

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mean": mean,
                "median": median,
                "high": high,
                "low": low,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mean = d.pop("mean")

        median = d.pop("median")

        high = d.pop("high")

        low = d.pop("low")

        count = d.pop("count")

        candle_stats_input = cls(
            mean=mean,
            median=median,
            high=high,
            low=low,
            count=count,
        )

        candle_stats_input.additional_properties = d
        return candle_stats_input

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
