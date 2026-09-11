from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.candle_period_types import CandlePeriodTypes


T = TypeVar("T", bound="CandlePeriod")


@_attrs_define
class CandlePeriod:
    """
    Attributes:
        period_start (str): Bucket start date (YYYY-MM-DD): the UTC calendar day, the Monday of the ISO week, or the 1st
            of the month, depending on interval.
        types (CandlePeriodTypes): Stats keyed by listing type; new listing types appear as additive keys. Currently
            "auction" (completed auction sales — the bid side) and "fixed" (Buy It Now asking prices — the ask side, not
            necessarily completed sales). A type with no listings in this bucket is absent from the map.
    """

    period_start: str
    types: "CandlePeriodTypes"

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start

        types = self.types.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "period_start": period_start,
                "types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candle_period_types import CandlePeriodTypes

        d = dict(src_dict)
        period_start = d.pop("period_start")

        types = CandlePeriodTypes.from_dict(d.pop("types"))

        candle_period = cls(
            period_start=period_start,
            types=types,
        )

        return candle_period
