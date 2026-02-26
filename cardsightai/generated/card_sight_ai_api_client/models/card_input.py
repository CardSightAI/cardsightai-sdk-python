from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardInput")


@_attrs_define
class CardInput:
    """
    Attributes:
        release_id (str): UUID of the release this card belongs to. Provided for convenience to avoid additional
            lookups.
        set_id (str): UUID of the set this card belongs to. Links to the set entity. Determines which collection within
            the release contains this card.
        id (str): Unique identifier for the card. Format: UUID v4. This ID is permanent and used for all API operations
            involving this card.
        name (str): Primary subject of the card. Usually a player name for sports cards (e.g., "Michael Jordan") or
            character/subject for non-sports.
        number (Union[Unset, str]): Card number within the set. Examples: "23", "RC-15", "L-5". May include letters for
            special subsets. Null for unnumbered cards.
        description (Union[Unset, str]): Additional card details such as team, position, special notations, or card back
            information. May be null.
        is_parallel_only (Union[Unset, bool]): Indicates this card exists only as a parallel, not as a base card. For
            example, if a set has 15 base cards but a parallel variant has 20 cards, the 5 extra cards would have
            isParallelOnly: true.
    """

    release_id: str
    set_id: str
    id: str
    name: str
    number: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_parallel_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        set_id = self.set_id

        id = self.id

        name = self.name

        number = self.number

        description = self.description

        is_parallel_only = self.is_parallel_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "releaseId": release_id,
                "setId": set_id,
                "id": id,
                "name": name,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
        if is_parallel_only is not UNSET:
            field_dict["isParallelOnly"] = is_parallel_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        release_id = d.pop("releaseId")

        set_id = d.pop("setId")

        id = d.pop("id")

        name = d.pop("name")

        number = d.pop("number", UNSET)

        description = d.pop("description", UNSET)

        is_parallel_only = d.pop("isParallelOnly", UNSET)

        card_input = cls(
            release_id=release_id,
            set_id=set_id,
            id=id,
            name=name,
            number=number,
            description=description,
            is_parallel_only=is_parallel_only,
        )

        card_input.additional_properties = d
        return card_input

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
