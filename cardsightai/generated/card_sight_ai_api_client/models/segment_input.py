from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        shortname (Union[None, str]): Short, URL-friendly key for the segment, usable in place of the name or UUID on
            segment-specific routes such as /v1/identify/card/{segment} (e.g. "magic" for "Magic: The Gathering"). Null when
            no shortname is set.
        is_identifiable (bool): Whether cards in this segment can be identified by the CardSightAI identification
            service.
    """

    id: str
    name: str
    shortname: Union[None, str]
    is_identifiable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        shortname: Union[None, str]
        shortname = self.shortname

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "shortname": shortname,
                "is_identifiable": is_identifiable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_shortname(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        shortname = _parse_shortname(d.pop("shortname"))

        is_identifiable = d.pop("is_identifiable")

        segment_input = cls(
            id=id,
            name=name,
            shortname=shortname,
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
