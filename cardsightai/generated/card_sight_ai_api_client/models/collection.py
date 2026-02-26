from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
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

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        collector_id = self.collector_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

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

        collection = cls(
            id=id,
            collector_id=collector_id,
            name=name,
            description=description,
        )

        return collection
