from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionFinancials")


@_attrs_define
class CollectionFinancials:
    """
    Attributes:
        total_invested (Union[Unset, str]): Total amount invested (sum of buy prices)
        total_realized_gains (Union[Unset, str]): Total gains from sold cards (soldPrice - buyPrice)
    """

    total_invested: Union[Unset, str] = UNSET
    total_realized_gains: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_invested = self.total_invested

        total_realized_gains = self.total_realized_gains

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_invested is not UNSET:
            field_dict["totalInvested"] = total_invested
        if total_realized_gains is not UNSET:
            field_dict["totalRealizedGains"] = total_realized_gains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_invested = d.pop("totalInvested", UNSET)

        total_realized_gains = d.pop("totalRealizedGains", UNSET)

        collection_financials = cls(
            total_invested=total_invested,
            total_realized_gains=total_realized_gains,
        )

        return collection_financials
