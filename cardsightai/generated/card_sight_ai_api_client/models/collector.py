from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Collector")


@_attrs_define
class Collector:
    """
    Attributes:
        id (str): Unique identifier for the collector
        name (Union[Unset, str]): Name of the collector (e.g., "Mike", "Eric")
    """

    id: str
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        collector = cls(
            id=id,
            name=name,
        )

        return collector
