from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCollectionInput")


@_attrs_define
class CreateCollectionInput:
    """
    Attributes:
        collector_id (UUID): UUID of the collector who will own this collection
        name (Union[Unset, str]): Name of the collection
        description (Union[Unset, str]): Description of the collection
    """

    collector_id: UUID
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collector_id = str(self.collector_id)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectorId": collector_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collector_id = UUID(d.pop("collectorId"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        create_collection_input = cls(
            collector_id=collector_id,
            name=name,
            description=description,
        )

        create_collection_input.additional_properties = d
        return create_collection_input

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
