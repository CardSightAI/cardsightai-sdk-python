from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedAttributeResponseInput")


@_attrs_define
class DetailedAttributeResponseInput:
    """
    Attributes:
        id (str): Unique identifier for the attribute. Format: UUID v4. This ID is permanent and used for all API
            operations involving this attribute.
        name (str): Full descriptive name of the attribute. Examples: "Rookie Card", "Autograph", "Game-Used
            Memorabilia". Used for display purposes.
        short_name (str): Abbreviated code for the attribute. Examples: "RC" (Rookie Card), "AU" (Autograph), "GU"
            (Game-Used). Used for compact display and filtering.
        card_count (float): Number of cards with this attribute
        description (Union[Unset, str]): Detailed explanation of what this attribute represents, when it applies, or any
            special notes. May be null.
    """

    id: str
    name: str
    short_name: str
    card_count: float
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        short_name = self.short_name

        card_count = self.card_count

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "shortName": short_name,
                "cardCount": card_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        short_name = d.pop("shortName")

        card_count = d.pop("cardCount")

        description = d.pop("description", UNSET)

        detailed_attribute_response_input = cls(
            id=id,
            name=name,
            short_name=short_name,
            card_count=card_count,
            description=description,
        )

        detailed_attribute_response_input.additional_properties = d
        return detailed_attribute_response_input

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
