from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.candle_period import CandlePeriod
    from ..models.timeseries_grade_group_totals import TimeseriesGradeGroupTotals


T = TypeVar("T", bound="TimeseriesGradeGroup")


@_attrs_define
class TimeseriesGradeGroup:
    """
    Attributes:
        grade_value (str): Grade value (e.g., "10", "9.5")
        grade_id (UUID): Grade UUID
        candles (list['CandlePeriod']): Chronological buckets computed from this grade's listings only, oldest first. A
            bucket with no listings in any requested type is omitted entirely.
        totals (TimeseriesGradeGroupTotals): Whole-window counts for this grade, keyed by listing type. A type with no
            listings across the window is omitted; a type can appear with total_count 0 when all of its listings were
            removed by the outlier filter.
    """

    grade_value: str
    grade_id: UUID
    candles: list["CandlePeriod"]
    totals: "TimeseriesGradeGroupTotals"

    def to_dict(self) -> dict[str, Any]:
        grade_value = self.grade_value

        grade_id = str(self.grade_id)

        candles = []
        for candles_item_data in self.candles:
            candles_item = candles_item_data.to_dict()
            candles.append(candles_item)

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "grade_value": grade_value,
                "grade_id": grade_id,
                "candles": candles,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candle_period import CandlePeriod
        from ..models.timeseries_grade_group_totals import TimeseriesGradeGroupTotals

        d = dict(src_dict)
        grade_value = d.pop("grade_value")

        grade_id = UUID(d.pop("grade_id"))

        candles = []
        _candles = d.pop("candles")
        for candles_item_data in _candles:
            candles_item = CandlePeriod.from_dict(candles_item_data)

            candles.append(candles_item)

        totals = TimeseriesGradeGroupTotals.from_dict(d.pop("totals"))

        timeseries_grade_group = cls(
            grade_value=grade_value,
            grade_id=grade_id,
            candles=candles,
            totals=totals,
        )

        return timeseries_grade_group
