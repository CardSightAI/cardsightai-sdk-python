from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ListCard")


@_attrs_define
class ListCard:
    """
    Attributes:
        id (str): Internal ID for the list card
        list_id (str): ID of the list
        card_id (str): ID of the card
    """

    id: str
    list_id: str
    card_id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        list_id = self.list_id

        card_id = self.card_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "listId": list_id,
                "cardId": card_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        list_id = d.pop("listId")

        card_id = d.pop("cardId")

        list_card = cls(
            id=id,
            list_id=list_id,
            card_id=card_id,
        )

        return list_card
