from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldSummary")


@_attrs_define
class FieldSummary:
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

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        usage_count = self.usage_count

        description = self.description

        field_dict: dict[str, Any] = {}

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

        field_summary = cls(
            id=id,
            key=key,
            name=name,
            usage_count=usage_count,
            description=description,
        )

        return field_summary
