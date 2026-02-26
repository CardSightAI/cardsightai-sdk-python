from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddCardToBinder")


@_attrs_define
class AddCardToBinder:
    """
    Attributes:
        collection_card_id (UUID): UUID of the collection card to add to the binder
    """

    collection_card_id: UUID

    def to_dict(self) -> dict[str, Any]:
        collection_card_id = str(self.collection_card_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collectionCardId": collection_card_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_card_id = UUID(d.pop("collectionCardId"))

        add_card_to_binder = cls(
            collection_card_id=collection_card_id,
        )

        return add_card_to_binder
