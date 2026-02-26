from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCollection")


@_attrs_define
class UpdateCollection:
    """
    Attributes:
        name (Union[Unset, str]): Name of the collection
        description (Union[Unset, str]): Description of the collection
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        update_collection = cls(
            name=name,
            description=description,
        )

        return update_collection
