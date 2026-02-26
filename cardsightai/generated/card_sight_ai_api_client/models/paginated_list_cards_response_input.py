from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_card_input import ListCardInput


T = TypeVar("T", bound="PaginatedListCardsResponseInput")


@_attrs_define
class PaginatedListCardsResponseInput:
    """
    Attributes:
        cards (list['ListCardInput']): Array of cards in this list with minimal metadata
        total_count (float): Total number of cards in this list
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    cards: list["ListCardInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cards": cards,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_card_input import ListCardInput

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = ListCardInput.from_dict(cards_item_data)

            cards.append(cards_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_list_cards_response_input = cls(
            cards=cards,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_list_cards_response_input.additional_properties = d
        return paginated_list_cards_response_input

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
