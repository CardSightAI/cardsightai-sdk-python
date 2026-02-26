from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.card_with_optional_parallel import CardWithOptionalParallel


T = TypeVar("T", bound="RandomCardsResponse")


@_attrs_define
class RandomCardsResponse:
    """
    Attributes:
        cards (list['CardWithOptionalParallel']): Array of random cards. When includeParallels=true, some cards may be
            converted to parallels based on weighted probability.
        count (float): Actual number of cards returned. May be less than requested count if insufficient matches.
    """

    cards: list["CardWithOptionalParallel"]
    count: float

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cards": cards,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_with_optional_parallel import CardWithOptionalParallel

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = CardWithOptionalParallel.from_dict(cards_item_data)

            cards.append(cards_item)

        count = d.pop("count")

        random_cards_response = cls(
            cards=cards,
            count=count,
        )

        return random_cards_response
