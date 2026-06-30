from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        shortname: Union[None, str]
        shortname = self.shortname

        is_identifiable = self.is_identifiable

        field_dict: dict[str, Any] = {}

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

        segment = cls(
            id=id,
            name=name,
            shortname=shortname,
            is_identifiable=is_identifiable,
        )

        return segment
