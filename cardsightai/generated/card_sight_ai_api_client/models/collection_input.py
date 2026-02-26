from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionInput")


@_attrs_define
class CollectionInput:
    """
    Attributes:
        id (str): Unique identifier for the collection
        collector_id (str): ID of the collector who owns this collection
        name (Union[Unset, str]): Name of the collection
        description (Union[Unset, str]): Description of the collection
    """

    id: str
    collector_id: str
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        collector_id = self.collector_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        id = d.pop("id")

        collector_id = d.pop("collectorId")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        collection_input = cls(
            id=id,
            collector_id=collector_id,
            name=name,
            description=description,
        )

        collection_input.additional_properties = d
        return collection_input

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
