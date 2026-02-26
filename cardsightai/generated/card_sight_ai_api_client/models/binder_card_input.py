from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BinderCardInput")


@_attrs_define
class BinderCardInput:
    """
    Attributes:
        id (UUID): Unique identifier for the binder card link
        binder_id (UUID): ID of the binder
        collection_card_id (UUID): ID of the collection card
    """

    id: UUID
    binder_id: UUID
    collection_card_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        binder_id = str(self.binder_id)

        collection_card_id = str(self.collection_card_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "binderId": binder_id,
                "collectionCardId": collection_card_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        binder_id = UUID(d.pop("binderId"))

        collection_card_id = UUID(d.pop("collectionCardId"))

        binder_card_input = cls(
            id=id,
            binder_id=binder_id,
            collection_card_id=collection_card_id,
        )

        binder_card_input.additional_properties = d
        return binder_card_input

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
