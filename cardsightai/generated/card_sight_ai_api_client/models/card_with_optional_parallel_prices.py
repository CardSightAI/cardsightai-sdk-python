from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardWithOptionalParallelPrices")


@_attrs_define
class CardWithOptionalParallelPrices:
    """Average pricing data for the base card. Only included when price data is available.

    Attributes:
        raw (Union[Unset, str]): Average price for ungraded/raw condition cards. Format: USD with 2 decimal places
            (e.g., "10.00", "5.50")
        psa_10 (Union[Unset, str]): Average price for PSA 10 (Gem Mint) graded cards. Format: USD with 2 decimal places
            (e.g., "100.00", "75.25")
        psa_9 (Union[Unset, str]): Average price for PSA 9 (Mint) graded cards. Format: USD with 2 decimal places (e.g.,
            "50.00", "35.75")
    """

    raw: Union[Unset, str] = UNSET
    psa_10: Union[Unset, str] = UNSET
    psa_9: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        psa_10 = self.psa_10

        psa_9 = self.psa_9

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if psa_10 is not UNSET:
            field_dict["psa-10"] = psa_10
        if psa_9 is not UNSET:
            field_dict["psa-9"] = psa_9

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw = d.pop("raw", UNSET)

        psa_10 = d.pop("psa-10", UNSET)

        psa_9 = d.pop("psa-9", UNSET)

        card_with_optional_parallel_prices = cls(
            raw=raw,
            psa_10=psa_10,
            psa_9=psa_9,
        )

        return card_with_optional_parallel_prices
