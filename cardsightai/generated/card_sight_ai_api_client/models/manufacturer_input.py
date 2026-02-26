from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManufacturerInput")


@_attrs_define
class ManufacturerInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        manufacturer_input = cls(
            id=id,
            name=name,
            description=description,
        )

        manufacturer_input.additional_properties = d
        return manufacturer_input

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
