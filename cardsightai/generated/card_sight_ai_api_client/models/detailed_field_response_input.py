from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedFieldResponseInput")


@_attrs_define
class DetailedFieldResponseInput:
    """
    Attributes:
        id (str): Unique identifier for the field. Format: UUID v4. This ID is permanent and used for all API operations
            involving this field.
        key (str): Field key/code used when referencing this field in values and filters. Examples: "HP", "RARITY",
            "ARTIST". Typically uppercase.
        name (str): Display name of the field. Examples: "Hit Points", "Rarity", "Artist". Used for display purposes.
        usage_count (float): Total number of catalog entities (cards, sets, releases, and segments) that have a value
            for this field.
        description (Union[Unset, str]): Detailed explanation of what this field represents. Omitted when not provided.
    """

    id: str
    key: str
    name: str
    usage_count: float
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        usage_count = self.usage_count

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "name": name,
                "usageCount": usage_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        name = d.pop("name")

        usage_count = d.pop("usageCount")

        description = d.pop("description", UNSET)

        detailed_field_response_input = cls(
            id=id,
            key=key,
            name=name,
            usage_count=usage_count,
            description=description,
        )

        detailed_field_response_input.additional_properties = d
        return detailed_field_response_input

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
