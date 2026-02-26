from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionFinancialsInput")


@_attrs_define
class CollectionFinancialsInput:
    """
    Attributes:
        total_invested (Union[Unset, str]): Total amount invested (sum of buy prices)
        current_market_value (Union[Unset, str]): Current total market value
        total_realized_gains (Union[Unset, str]): Total gains from sold cards
        total_unrealized_gains (Union[Unset, str]): Unrealized gains on unsold cards
        overall_roi (Union[Unset, float]): Overall return on investment percentage
        realized_roi (Union[Unset, float]): ROI on sold cards only
    """

    total_invested: Union[Unset, str] = UNSET
    current_market_value: Union[Unset, str] = UNSET
    total_realized_gains: Union[Unset, str] = UNSET
    total_unrealized_gains: Union[Unset, str] = UNSET
    overall_roi: Union[Unset, float] = UNSET
    realized_roi: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_invested = self.total_invested

        current_market_value = self.current_market_value

        total_realized_gains = self.total_realized_gains

        total_unrealized_gains = self.total_unrealized_gains

        overall_roi = self.overall_roi

        realized_roi = self.realized_roi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_invested is not UNSET:
            field_dict["totalInvested"] = total_invested
        if current_market_value is not UNSET:
            field_dict["currentMarketValue"] = current_market_value
        if total_realized_gains is not UNSET:
            field_dict["totalRealizedGains"] = total_realized_gains
        if total_unrealized_gains is not UNSET:
            field_dict["totalUnrealizedGains"] = total_unrealized_gains
        if overall_roi is not UNSET:
            field_dict["overallROI"] = overall_roi
        if realized_roi is not UNSET:
            field_dict["realizedROI"] = realized_roi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_invested = d.pop("totalInvested", UNSET)

        current_market_value = d.pop("currentMarketValue", UNSET)

        total_realized_gains = d.pop("totalRealizedGains", UNSET)

        total_unrealized_gains = d.pop("totalUnrealizedGains", UNSET)

        overall_roi = d.pop("overallROI", UNSET)

        realized_roi = d.pop("realizedROI", UNSET)

        collection_financials_input = cls(
            total_invested=total_invested,
            current_market_value=current_market_value,
            total_realized_gains=total_realized_gains,
            total_unrealized_gains=total_unrealized_gains,
            overall_roi=overall_roi,
            realized_roi=realized_roi,
        )

        collection_financials_input.additional_properties = d
        return collection_financials_input

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
