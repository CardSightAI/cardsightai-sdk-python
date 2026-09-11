from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.candle_period import CandlePeriod
    from ..models.raw_timeseries_section_totals import RawTimeseriesSectionTotals


T = TypeVar("T", bound="RawTimeseriesSection")


@_attrs_define
class RawTimeseriesSection:
    """
    Attributes:
        candles (list['CandlePeriod']): Chronological buckets computed from ungraded listings only, oldest first. A
            bucket with no listings in any requested type is omitted entirely; empty when the card has no ungraded listings
            in the window, or when the grade_id filter pins a specific grade (which excludes ungraded listings).
        totals (RawTimeseriesSectionTotals): Whole-window counts for ungraded listings, keyed by listing type. A type
            with no listings across the window is omitted; a type can appear with total_count 0 when all of its listings
            were removed by the outlier filter.
    """

    candles: list["CandlePeriod"]
    totals: "RawTimeseriesSectionTotals"

    def to_dict(self) -> dict[str, Any]:
        candles = []
        for candles_item_data in self.candles:
            candles_item = candles_item_data.to_dict()
            candles.append(candles_item)

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "candles": candles,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candle_period import CandlePeriod
        from ..models.raw_timeseries_section_totals import RawTimeseriesSectionTotals

        d = dict(src_dict)
        candles = []
        _candles = d.pop("candles")
        for candles_item_data in _candles:
            candles_item = CandlePeriod.from_dict(candles_item_data)

            candles.append(candles_item)

        totals = RawTimeseriesSectionTotals.from_dict(d.pop("totals"))

        raw_timeseries_section = cls(
            candles=candles,
            totals=totals,
        )

        return raw_timeseries_section
