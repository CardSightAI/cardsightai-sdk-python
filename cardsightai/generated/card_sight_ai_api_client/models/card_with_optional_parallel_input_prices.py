from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardWithOptionalParallelInputPrices")


@_attrs_define
class CardWithOptionalParallelInputPrices:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        psa_10 = self.psa_10

        psa_9 = self.psa_9

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        card_with_optional_parallel_input_prices = cls(
            raw=raw,
            psa_10=psa_10,
            psa_9=psa_9,
        )

        card_with_optional_parallel_input_prices.additional_properties = d
        return card_with_optional_parallel_input_prices

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
