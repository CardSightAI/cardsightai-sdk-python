from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_summary import CardSummary
    from ..models.server_message import ServerMessage


T = TypeVar("T", bound="PaginatedCardsResponse")


@_attrs_define
class PaginatedCardsResponse:
    """
    Attributes:
        cards (list['CardSummary']): Array of card entities with summary information
        total_count (float): Total number of cards matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
        messages (Union[Unset, list['ServerMessage']]): Optional server advisory messages, e.g. a warning that an
            unrecognized query parameter was ignored. Omitted when there are none.
    """

    cards: list["CardSummary"]
    total_count: float
    skip: float
    take: float
    messages: Union[Unset, list["ServerMessage"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cards = []
        for cards_item_data in self.cards:
            cards_item = cards_item_data.to_dict()
            cards.append(cards_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cards": cards,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_summary import CardSummary
        from ..models.server_message import ServerMessage

        d = dict(src_dict)
        cards = []
        _cards = d.pop("cards")
        for cards_item_data in _cards:
            cards_item = CardSummary.from_dict(cards_item_data)

            cards.append(cards_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ServerMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        paginated_cards_response = cls(
            cards=cards,
            total_count=total_count,
            skip=skip,
            take=take,
            messages=messages,
        )

        return paginated_cards_response
