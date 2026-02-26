from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateList")


@_attrs_define
class CreateList:
    """
    Attributes:
        collector_id (str): UUID of the collector who will own this list
        name (Union[Unset, str]): Name of the list
        description (Union[Unset, str]): Description of the list
    """

    collector_id: str
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        collector_id = self.collector_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

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
        collector_id = d.pop("collectorId")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        create_list = cls(
            collector_id=collector_id,
            name=name,
            description=description,
        )

        return create_list
