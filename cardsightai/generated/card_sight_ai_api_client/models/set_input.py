from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetInput")


@_attrs_define
class SetInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        release_id = self.release_id

        name = self.name

        is_identifiable = self.is_identifiable

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        set_input = cls(
            id=id,
            release_id=release_id,
            name=name,
            is_identifiable=is_identifiable,
            description=description,
        )

        set_input.additional_properties = d
        return set_input

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
