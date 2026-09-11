from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.candle_period_input_types import CandlePeriodInputTypes


T = TypeVar("T", bound="CandlePeriodInput")


@_attrs_define
class CandlePeriodInput:
    """
    Attributes:
        period_start (str): Bucket start date (YYYY-MM-DD): the UTC calendar day, the Monday of the ISO week, or the 1st
            of the month, depending on interval.
        types (CandlePeriodInputTypes): Stats keyed by listing type; new listing types appear as additive keys.
            Currently "auction" (completed auction sales — the bid side) and "fixed" (Buy It Now asking prices — the ask
            side, not necessarily completed sales). A type with no listings in this bucket is absent from the map.
    """

    period_start: str
    types: "CandlePeriodInputTypes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start

        types = self.types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period_start": period_start,
                "types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candle_period_input_types import CandlePeriodInputTypes

        d = dict(src_dict)
        period_start = d.pop("period_start")

        types = CandlePeriodInputTypes.from_dict(d.pop("types"))

        candle_period_input = cls(
            period_start=period_start,
            types=types,
        )

        candle_period_input.additional_properties = d
        return candle_period_input

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
