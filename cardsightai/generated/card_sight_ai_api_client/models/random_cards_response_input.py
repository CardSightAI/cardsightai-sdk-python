from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.card_with_optional_parallel_input import CardWithOptionalParallelInput


T = TypeVar("T", bound="RandomCardsResponseInput")


@_attrs_define
class RandomCardsResponseInput:
    """
    Attributes:
        cards (list['CardWithOptionalParallelInput']): Array of random cards. When includeParallels=true, some cards may
            be converted to parallels based on weighted probability.
        count (float): Actual number of cards returned. May be less than requested count if insufficient matches.
    """

    cards: list["CardWithOptionalParallelInput"]
    count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cards": cards,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_with_optional_parallel_input import CardWithOptionalParallelInput

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = CardWithOptionalParallelInput.from_dict(cards_item_data)

            cards.append(cards_item)

        count = d.pop("count")

        random_cards_response_input = cls(
            cards=cards,
            count=count,
        )

        random_cards_response_input.additional_properties = d
        return random_cards_response_input

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
