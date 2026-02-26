from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIContextInput")


@_attrs_define
class AIContextInput:
    """
    Attributes:
        collection_id (Union[Unset, UUID]):
        user_id (Union[Unset, str]):
    """

    collection_id: Union[Unset, UUID] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id: Union[Unset, str] = UNSET
        if not isinstance(self.collection_id, Unset):
            collection_id = str(self.collection_id)

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _collection_id = d.pop("collectionId", UNSET)
        collection_id: Union[Unset, UUID]
        if isinstance(_collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = UUID(_collection_id)

        user_id = d.pop("userId", UNSET)

        ai_context_input = cls(
            collection_id=collection_id,
            user_id=user_id,
        )

        ai_context_input.additional_properties = d
        return ai_context_input

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
