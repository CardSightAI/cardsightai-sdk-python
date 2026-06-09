from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlabQualifier")


@_attrs_define
class SlabQualifier:
    """
    Attributes:
        code (str): Qualifier code (e.g., OC, MC, PD, ST)
        id (Union[Unset, UUID]): UUID of the qualifier from the catalog. Absent if qualifier could not be matched.
    """

    code: str
    id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        slab_qualifier = cls(
            code=code,
            id=id,
        )

        return slab_qualifier
