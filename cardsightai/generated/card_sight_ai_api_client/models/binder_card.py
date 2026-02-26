from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="BinderCard")


@_attrs_define
class BinderCard:
    """
    Attributes:
        id (UUID): Unique identifier for the binder card link
        binder_id (UUID): ID of the binder
        collection_card_id (UUID): ID of the collection card
    """

    id: UUID
    binder_id: UUID
    collection_card_id: UUID

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        binder_id = str(self.binder_id)

        collection_card_id = str(self.collection_card_id)

        field_dict: dict[str, Any] = {}

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

        binder_card = cls(
            id=id,
            binder_id=binder_id,
            collection_card_id=collection_card_id,
        )

        return binder_card
