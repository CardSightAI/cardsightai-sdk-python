from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListCardItem")


@_attrs_define
class ListCardItem:
    """
    Attributes:
        card_id (str): UUID of the card to add to the list
    """

    card_id: str

    def to_dict(self) -> dict[str, Any]:
        card_id = self.card_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cardId": card_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = d.pop("cardId")

        list_card_item = cls(
            card_id=card_id,
        )

        return list_card_item
