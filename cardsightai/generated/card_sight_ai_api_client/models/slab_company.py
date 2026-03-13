from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlabCompany")


@_attrs_define
class SlabCompany:
    """
    Attributes:
        name (str): Grading company name detected on the slab (e.g., "PSA", "BGS", "CGC", "SGC")
        id (Union[Unset, UUID]): UUID of the grading company from the catalog. Absent if company could not be matched.
    """

    name: str
    id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        slab_company = cls(
            name=name,
            id=id,
        )

        return slab_company
