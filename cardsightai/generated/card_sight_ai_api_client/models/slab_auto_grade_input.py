from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlabAutoGradeInput")


@_attrs_define
class SlabAutoGradeInput:
    """
    Attributes:
        id (Union[Unset, UUID]): UUID of the autograph grade from the catalog. Absent if not matched.
        value (Union[Unset, str]): Autograph grade value
        condition (Union[Unset, str]): Autograph grade condition
    """

    id: Union[Unset, UUID] = UNSET
    value: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        value = self.value

        condition = self.condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        value = d.pop("value", UNSET)

        condition = d.pop("condition", UNSET)

        slab_auto_grade_input = cls(
            id=id,
            value=value,
            condition=condition,
        )

        slab_auto_grade_input.additional_properties = d
        return slab_auto_grade_input

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
