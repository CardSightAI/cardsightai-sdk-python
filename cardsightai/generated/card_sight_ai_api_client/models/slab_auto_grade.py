from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlabAutoGrade")


@_attrs_define
class SlabAutoGrade:
    """
    Attributes:
        id (Union[Unset, UUID]): UUID of the autograph grade from the catalog. Absent if not matched.
        value (Union[Unset, str]): Autograph grade value
        condition (Union[Unset, str]): Autograph grade condition
    """

    id: Union[Unset, UUID] = UNSET
    value: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        value = self.value

        condition = self.condition

        field_dict: dict[str, Any] = {}

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

        slab_auto_grade = cls(
            id=id,
            value=value,
            condition=condition,
        )

        return slab_auto_grade
