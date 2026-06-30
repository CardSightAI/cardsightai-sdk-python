from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CardSetContextInput")


@_attrs_define
class CardSetContextInput:
    """
    Attributes:
        set_id (UUID): Set UUID
        name (str): Set name
        year (str): Release year
        release (str): Release name
    """

    set_id: UUID
    name: str
    year: str
    release: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_id = str(self.set_id)

        name = self.name

        year = self.year

        release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "set_id": set_id,
                "name": name,
                "year": year,
                "release": release,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_id = UUID(d.pop("set_id"))

        name = d.pop("name")

        year = d.pop("year")

        release = d.pop("release")

        card_set_context_input = cls(
            set_id=set_id,
            name=name,
            year=year,
            release=release,
        )

        card_set_context_input.additional_properties = d
        return card_set_context_input

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
