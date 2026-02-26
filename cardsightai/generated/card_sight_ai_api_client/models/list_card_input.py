from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListCardInput")


@_attrs_define
class ListCardInput:
    """
    Attributes:
        id (str): Internal ID for the list card
        list_id (str): ID of the list
        card_id (str): ID of the card
    """

    id: str
    list_id: str
    card_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        list_id = self.list_id

        card_id = self.card_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        list_card_input = cls(
            id=id,
            list_id=list_id,
            card_id=card_id,
        )

        list_card_input.additional_properties = d
        return list_card_input

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
