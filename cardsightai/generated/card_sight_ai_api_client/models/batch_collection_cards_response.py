from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_operation_error import BatchOperationError
    from ..models.collection_card import CollectionCard


T = TypeVar("T", bound="BatchCollectionCardsResponse")


@_attrs_define
class BatchCollectionCardsResponse:
    """
    Attributes:
        cards (list['CollectionCard']): Successfully created cards
        errors (Union[Unset, list['BatchOperationError']]): Any errors that occurred during batch creation
    """

    cards: list["CollectionCard"]
    errors: Union[Unset, list["BatchOperationError"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cards": cards,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_operation_error import BatchOperationError
        from ..models.collection_card import CollectionCard

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = CollectionCard.from_dict(cards_item_data)

            cards.append(cards_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = BatchOperationError.from_dict(errors_item_data)

            errors.append(errors_item)

        batch_collection_cards_response = cls(
            cards=cards,
            errors=errors,
        )

        return batch_collection_cards_response
