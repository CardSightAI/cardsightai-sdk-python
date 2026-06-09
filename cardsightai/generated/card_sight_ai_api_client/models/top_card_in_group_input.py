from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopCardInGroupInput")


@_attrs_define
class TopCardInGroupInput:
    """
    Attributes:
        card_id (str): Card UUID
        card_name (str): Card name
        set_name (str): Set name
        release_name (str): Release name
        release_year (str): Release year
        quantity (float): Quantity in collection
        buy_price (Union[Unset, str]): Purchase price per card
    """

    card_id: str
    card_name: str
    set_name: str
    release_name: str
    release_year: str
    quantity: float
    buy_price: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        card_name = self.card_name

        set_name = self.set_name

        release_name = self.release_name

        release_year = self.release_year

        quantity = self.quantity

        buy_price = self.buy_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardId": card_id,
                "cardName": card_name,
                "setName": set_name,
                "releaseName": release_name,
                "releaseYear": release_year,
                "quantity": quantity,
            }
        )
        if buy_price is not UNSET:
            field_dict["buyPrice"] = buy_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId")

        card_name = d.pop("cardName")

        set_name = d.pop("setName")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        quantity = d.pop("quantity")

        buy_price = d.pop("buyPrice", UNSET)

        top_card_in_group_input = cls(
            card_id=card_id,
            card_name=card_name,
            set_name=set_name,
            release_name=release_name,
            release_year=release_year,
            quantity=quantity,
            buy_price=buy_price,
        )

        top_card_in_group_input.additional_properties = d
        return top_card_in_group_input

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
