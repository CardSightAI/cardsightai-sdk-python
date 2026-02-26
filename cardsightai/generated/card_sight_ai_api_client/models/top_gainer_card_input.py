from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TopGainerCardInput")


@_attrs_define
class TopGainerCardInput:
    """
    Attributes:
        card_id (str): Card UUID
        card_name (str): Card name
        release_name (str): Release name
        release_year (str): Release year
        buy_price (str): Purchase price
        current_value (str): Current market value
        gain (str): Dollar gain amount
        gain_percentage (float): Percentage gain
    """

    card_id: str
    card_name: str
    release_name: str
    release_year: str
    buy_price: str
    current_value: str
    gain: str
    gain_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        card_name = self.card_name

        release_name = self.release_name

        release_year = self.release_year

        buy_price = self.buy_price

        current_value = self.current_value

        gain = self.gain

        gain_percentage = self.gain_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardId": card_id,
                "cardName": card_name,
                "releaseName": release_name,
                "releaseYear": release_year,
                "buyPrice": buy_price,
                "currentValue": current_value,
                "gain": gain,
                "gainPercentage": gain_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId")

        card_name = d.pop("cardName")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        buy_price = d.pop("buyPrice")

        current_value = d.pop("currentValue")

        gain = d.pop("gain")

        gain_percentage = d.pop("gainPercentage")

        top_gainer_card_input = cls(
            card_id=card_id,
            card_name=card_name,
            release_name=release_name,
            release_year=release_year,
            buy_price=buy_price,
            current_value=current_value,
            gain=gain,
            gain_percentage=gain_percentage,
        )

        top_gainer_card_input.additional_properties = d
        return top_gainer_card_input

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
