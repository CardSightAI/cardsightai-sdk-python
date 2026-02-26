from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_card_in_group_input import TopCardInGroupInput


T = TypeVar("T", bound="BreakdownGroupInput")


@_attrs_define
class BreakdownGroupInput:
    """
    Attributes:
        group_key (str): The grouping key (e.g., set name, year, grade)
        card_count (float): Number of cards in this group
        unique_card_count (float): Number of unique cards (ignoring duplicates)
        total_quantity (float): Total quantity including duplicates
        percentage_of_collection (float): Percentage this group represents of total collection
        group_id (Union[Unset, str]): The UUID of the group entity if applicable
        total_buy_price (Union[Unset, str]): Total purchase price for cards in group
        total_current_value (Union[Unset, str]): Total current market value
        total_sold_price (Union[Unset, str]): Total sold price for sold cards
        average_buy_price (Union[Unset, str]): Average purchase price per card
        average_current_value (Union[Unset, str]): Average current value per card
        roi (Union[Unset, float]): Return on investment percentage
        top_cards (Union[Unset, list['TopCardInGroupInput']]): Top 5 most valuable cards in this group
    """

    group_key: str
    card_count: float
    unique_card_count: float
    total_quantity: float
    percentage_of_collection: float
    group_id: Union[Unset, str] = UNSET
    total_buy_price: Union[Unset, str] = UNSET
    total_current_value: Union[Unset, str] = UNSET
    total_sold_price: Union[Unset, str] = UNSET
    average_buy_price: Union[Unset, str] = UNSET
    average_current_value: Union[Unset, str] = UNSET
    roi: Union[Unset, float] = UNSET
    top_cards: Union[Unset, list["TopCardInGroupInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_key = self.group_key

        card_count = self.card_count

        unique_card_count = self.unique_card_count

        total_quantity = self.total_quantity

        percentage_of_collection = self.percentage_of_collection

        group_id = self.group_id

        total_buy_price = self.total_buy_price

        total_current_value = self.total_current_value

        total_sold_price = self.total_sold_price

        average_buy_price = self.average_buy_price

        average_current_value = self.average_current_value

        roi = self.roi

        top_cards: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_cards, Unset):
            top_cards = []
            for top_cards_item_data in self.top_cards:
                top_cards_item = top_cards_item_data.to_dict()
                top_cards.append(top_cards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupKey": group_key,
                "cardCount": card_count,
                "uniqueCardCount": unique_card_count,
                "totalQuantity": total_quantity,
                "percentageOfCollection": percentage_of_collection,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if total_buy_price is not UNSET:
            field_dict["totalBuyPrice"] = total_buy_price
        if total_current_value is not UNSET:
            field_dict["totalCurrentValue"] = total_current_value
        if total_sold_price is not UNSET:
            field_dict["totalSoldPrice"] = total_sold_price
        if average_buy_price is not UNSET:
            field_dict["averageBuyPrice"] = average_buy_price
        if average_current_value is not UNSET:
            field_dict["averageCurrentValue"] = average_current_value
        if roi is not UNSET:
            field_dict["roi"] = roi
        if top_cards is not UNSET:
            field_dict["topCards"] = top_cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_card_in_group_input import TopCardInGroupInput

        d = dict(src_dict)
        group_key = d.pop("groupKey")

        card_count = d.pop("cardCount")

        unique_card_count = d.pop("uniqueCardCount")

        total_quantity = d.pop("totalQuantity")

        percentage_of_collection = d.pop("percentageOfCollection")

        group_id = d.pop("groupId", UNSET)

        total_buy_price = d.pop("totalBuyPrice", UNSET)

        total_current_value = d.pop("totalCurrentValue", UNSET)

        total_sold_price = d.pop("totalSoldPrice", UNSET)

        average_buy_price = d.pop("averageBuyPrice", UNSET)

        average_current_value = d.pop("averageCurrentValue", UNSET)

        roi = d.pop("roi", UNSET)

        top_cards = []
        _top_cards = d.pop("topCards", UNSET)
        for top_cards_item_data in _top_cards or []:
            top_cards_item = TopCardInGroupInput.from_dict(top_cards_item_data)

            top_cards.append(top_cards_item)

        breakdown_group_input = cls(
            group_key=group_key,
            card_count=card_count,
            unique_card_count=unique_card_count,
            total_quantity=total_quantity,
            percentage_of_collection=percentage_of_collection,
            group_id=group_id,
            total_buy_price=total_buy_price,
            total_current_value=total_current_value,
            total_sold_price=total_sold_price,
            average_buy_price=average_buy_price,
            average_current_value=average_current_value,
            roi=roi,
            top_cards=top_cards,
        )

        breakdown_group_input.additional_properties = d
        return breakdown_group_input

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
