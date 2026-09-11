from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.candle_stats import CandleStats


T = TypeVar("T", bound="CandlePeriodTypes")


@_attrs_define
class CandlePeriodTypes:
    """Stats keyed by listing type; new listing types appear as additive keys. Currently "auction" (completed auction sales
    — the bid side) and "fixed" (Buy It Now asking prices — the ask side, not necessarily completed sales). A type with
    no listings in this bucket is absent from the map.

    """

    additional_properties: dict[str, "CandleStats"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candle_stats import CandleStats

        d = dict(src_dict)
        candle_period_types = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CandleStats.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        candle_period_types.additional_properties = additional_properties
        return candle_period_types

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "CandleStats":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "CandleStats") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
