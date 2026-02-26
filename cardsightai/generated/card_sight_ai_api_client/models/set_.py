from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Set")


@_attrs_define
class Set:
    """
    Attributes:
        id (str): Unique identifier for the set. Format: UUID v4. This ID is permanent and used for all API operations
            involving this set.
        release_id (str): UUID of the release this set belongs to. Links to the release entity. A release typically
            contains multiple sets.
        name (str): Name of the set within the release. Examples: "Base Set", "Rookie Autographs", "Legends". Describes
            the theme or type of cards in this set.
        is_identifiable (bool): Whether cards in this set can be identified by the CardSightAI identification service.
        description (Union[Unset, str]): Additional details about the set, such as card count, special features, or
            checklist highlights. May be null.
    """

    id: str
    release_id: str
    name: str
    is_identifiable: bool
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        release_id = self.release_id

        name = self.name

        is_identifiable = self.is_identifiable

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "releaseId": release_id,
                "name": name,
                "is_identifiable": is_identifiable,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        release_id = d.pop("releaseId")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        description = d.pop("description", UNSET)

        set_ = cls(
            id=id,
            release_id=release_id,
            name=name,
            is_identifiable=is_identifiable,
            description=description,
        )

        return set_
