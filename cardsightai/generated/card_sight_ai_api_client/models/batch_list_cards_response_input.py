from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_operation_error_input import BatchOperationErrorInput
    from ..models.list_card_input import ListCardInput


T = TypeVar("T", bound="BatchListCardsResponseInput")


@_attrs_define
class BatchListCardsResponseInput:
    """
    Attributes:
        cards (list['ListCardInput']): Successfully created cards
        errors (Union[Unset, list['BatchOperationErrorInput']]): Any errors that occurred during batch creation
    """

    cards: list["ListCardInput"]
    errors: Union[Unset, list["BatchOperationErrorInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.batch_operation_error_input import BatchOperationErrorInput
        from ..models.list_card_input import ListCardInput

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = ListCardInput.from_dict(cards_item_data)

            cards.append(cards_item)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = BatchOperationErrorInput.from_dict(errors_item_data)

            errors.append(errors_item)

        batch_list_cards_response_input = cls(
            cards=cards,
            errors=errors,
        )

        batch_list_cards_response_input.additional_properties = d
        return batch_list_cards_response_input

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
