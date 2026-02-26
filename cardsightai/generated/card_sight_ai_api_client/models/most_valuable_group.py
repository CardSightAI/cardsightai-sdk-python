from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MostValuableGroup")


@_attrs_define
class MostValuableGroup:
    """
    Attributes:
        name (str): Name of most valuable group
        value (str): Total value of the group
    """

    name: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        most_valuable_group = cls(
            name=name,
            value=value,
        )

        return most_valuable_group
