from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.candle_period_input import CandlePeriodInput
    from ..models.timeseries_grade_group_input_totals import TimeseriesGradeGroupInputTotals


T = TypeVar("T", bound="TimeseriesGradeGroupInput")


@_attrs_define
class TimeseriesGradeGroupInput:
    """
    Attributes:
        grade_value (str): Grade value (e.g., "10", "9.5")
        grade_id (UUID): Grade UUID
        candles (list['CandlePeriodInput']): Chronological buckets computed from this grade's listings only, oldest
            first. A bucket with no listings in any requested type is omitted entirely.
        totals (TimeseriesGradeGroupInputTotals): Whole-window counts for this grade, keyed by listing type. A type with
            no listings across the window is omitted; a type can appear with total_count 0 when all of its listings were
            removed by the outlier filter.
    """

    grade_value: str
    grade_id: UUID
    candles: list["CandlePeriodInput"]
    totals: "TimeseriesGradeGroupInputTotals"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grade_value = self.grade_value

        grade_id = str(self.grade_id)

        candles = []
        for candles_item_data in self.candles:
            candles_item = candles_item_data.to_dict()
            candles.append(candles_item)

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.candle_period_input import CandlePeriodInput
        from ..models.timeseries_grade_group_input_totals import TimeseriesGradeGroupInputTotals

        d = dict(src_dict)
        grade_value = d.pop("grade_value")

        grade_id = UUID(d.pop("grade_id"))

        candles = []
        _candles = d.pop("candles")
        for candles_item_data in _candles:
            candles_item = CandlePeriodInput.from_dict(candles_item_data)

            candles.append(candles_item)

        totals = TimeseriesGradeGroupInputTotals.from_dict(d.pop("totals"))

        timeseries_grade_group_input = cls(
            grade_value=grade_value,
            grade_id=grade_id,
            candles=candles,
            totals=totals,
        )

        timeseries_grade_group_input.additional_properties = d
        return timeseries_grade_group_input

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
