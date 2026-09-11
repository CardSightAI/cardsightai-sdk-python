from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.timeseries_type_totals_input import TimeseriesTypeTotalsInput


T = TypeVar("T", bound="TimeseriesGradeGroupInputTotals")


@_attrs_define
class TimeseriesGradeGroupInputTotals:
    """Whole-window counts for this grade, keyed by listing type. A type with no listings across the window is omitted; a
    type can appear with total_count 0 when all of its listings were removed by the outlier filter.

    """

    additional_properties: dict[str, "TimeseriesTypeTotalsInput"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timeseries_type_totals_input import TimeseriesTypeTotalsInput

        d = dict(src_dict)
        timeseries_grade_group_input_totals = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TimeseriesTypeTotalsInput.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        timeseries_grade_group_input_totals.additional_properties = additional_properties
        return timeseries_grade_group_input_totals

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TimeseriesTypeTotalsInput":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TimeseriesTypeTotalsInput") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
