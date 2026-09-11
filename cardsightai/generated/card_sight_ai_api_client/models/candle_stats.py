from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CandleStats")


@_attrs_define
class CandleStats:
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

    def to_dict(self) -> dict[str, Any]:
        mean = self.mean

        median = self.median

        high = self.high

        low = self.low

        count = self.count

        field_dict: dict[str, Any] = {}

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

        candle_stats = cls(
            mean=mean,
            median=median,
            high=high,
            low=low,
            count=count,
        )

        return candle_stats
