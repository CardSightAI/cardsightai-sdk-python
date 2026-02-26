from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BinderInput")


@_attrs_define
class BinderInput:
    """
    Attributes:
        id (UUID): Unique identifier for the binder
        collection_id (UUID): ID of the collection this binder belongs to
        name (Union[Unset, str]): Name of the binder
        description (Union[Unset, str]): Description of the binder
    """

    id: UUID
    collection_id: UUID
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        collection_id = str(self.collection_id)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "collectionId": collection_id,
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
        id = UUID(d.pop("id"))

        collection_id = UUID(d.pop("collectionId"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        binder_input = cls(
            id=id,
            collection_id=collection_id,
            name=name,
            description=description,
        )

        binder_input.additional_properties = d
        return binder_input

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
