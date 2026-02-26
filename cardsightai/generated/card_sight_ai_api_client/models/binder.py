from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Binder")


@_attrs_define
class Binder:
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

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        collection_id = str(self.collection_id)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

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

        binder = cls(
            id=id,
            collection_id=collection_id,
            name=name,
            description=description,
        )

        return binder
