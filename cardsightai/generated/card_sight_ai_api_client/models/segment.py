from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """
    Attributes:
        id (str): Unique identifier for the segment. Format: UUID v4. This ID is permanent and used for all API
            operations involving this segment.
        name (str): Display name of the segment. Examples: "Sports", "Entertainment", "Gaming". Used for categorizing
            releases and filtering.
        is_identifiable (bool): Whether cards in this segment can be identified by the CardSightAI identification
            service.
    """

    id: str
    name: str
    is_identifiable: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_identifiable": is_identifiable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        segment = cls(
            id=id,
            name=name,
            is_identifiable=is_identifiable,
        )

        return segment
