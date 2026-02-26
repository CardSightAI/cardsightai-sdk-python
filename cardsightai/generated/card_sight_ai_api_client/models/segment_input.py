from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentInput")


@_attrs_define
class SegmentInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        segment_input = cls(
            id=id,
            name=name,
            is_identifiable=is_identifiable,
        )

        segment_input.additional_properties = d
        return segment_input

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
