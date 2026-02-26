from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Manufacturer")


@_attrs_define
class Manufacturer:
    """
    Attributes:
        id (str): Unique identifier for the manufacturer. Format: UUID v4. This ID is permanent and used for all API
            operations involving this manufacturer.
        name (str): Official name of the manufacturer. Examples: "Topps", "Panini America", "Upper Deck". This is the
            primary display name.
        description (Union[Unset, str]): Additional information about the manufacturer, such as founding year,
            headquarters, or notable product lines. May be null if not provided.
    """

    id: str
    name: str
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
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

        description = d.pop("description", UNSET)

        manufacturer = cls(
            id=id,
            name=name,
            description=description,
        )

        return manufacturer
