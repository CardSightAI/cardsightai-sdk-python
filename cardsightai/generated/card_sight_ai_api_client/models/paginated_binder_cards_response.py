from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.binder_card import BinderCard


T = TypeVar("T", bound="PaginatedBinderCardsResponse")


@_attrs_define
class PaginatedBinderCardsResponse:
    """
    Attributes:
        cards (list['BinderCard']):
        total_count (float):
        skip (float):
        take (float):
    """

    cards: list["BinderCard"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.binder_card import BinderCard

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = BinderCard.from_dict(cards_item_data)

            cards.append(cards_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_binder_cards_response = cls(
            cards=cards,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_binder_cards_response
