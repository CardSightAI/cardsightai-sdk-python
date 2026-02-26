from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TopGainerCard")


@_attrs_define
class TopGainerCard:
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

        top_gainer_card = cls(
            card_id=card_id,
            card_name=card_name,
            release_name=release_name,
            release_year=release_year,
            buy_price=buy_price,
            current_value=current_value,
            gain=gain,
            gain_percentage=gain_percentage,
        )

        return top_gainer_card
