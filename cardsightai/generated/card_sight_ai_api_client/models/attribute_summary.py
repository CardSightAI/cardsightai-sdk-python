from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeSummary")


@_attrs_define
class AttributeSummary:
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

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        short_name = self.short_name

        card_count = self.card_count

        description = self.description

        field_dict: dict[str, Any] = {}

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

        attribute_summary = cls(
            id=id,
            name=name,
            short_name=short_name,
            card_count=card_count,
            description=description,
        )

        return attribute_summary
