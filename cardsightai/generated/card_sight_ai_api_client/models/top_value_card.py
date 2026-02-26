from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TopValueCard")


@_attrs_define
class TopValueCard:
    """
    Attributes:
        card_id (str): Card UUID
        card_name (str): Card name
        release_name (str): Release name
        release_year (str): Release year
        current_value (str): Current market value
        quantity (float): Quantity owned
    """

    card_id: str
    card_name: str
    release_name: str
    release_year: str
    current_value: str
    quantity: float

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        card_name = self.card_name

        release_name = self.release_name

        release_year = self.release_year

        current_value = self.current_value

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cardId": card_id,
                "cardName": card_name,
                "releaseName": release_name,
                "releaseYear": release_year,
                "currentValue": current_value,
                "quantity": quantity,
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

        current_value = d.pop("currentValue")

        quantity = d.pop("quantity")

        top_value_card = cls(
            card_id=card_id,
            card_name=card_name,
            release_name=release_name,
            release_year=release_year,
            current_value=current_value,
            quantity=quantity,
        )

        return top_value_card
