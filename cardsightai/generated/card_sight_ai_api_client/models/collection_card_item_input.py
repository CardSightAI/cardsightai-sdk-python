from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionCardItemInput")


@_attrs_define
class CollectionCardItemInput:
    """
    Attributes:
        card_id (UUID): UUID of the card to add to the collection
        parallel_id (Union[Unset, UUID]): UUID of the card parallel if applicable
        grade_id (Union[Unset, UUID]): UUID of the grade if card is graded
        quantity (Union[Unset, float]): Quantity of this card to add Default: 1.0.
        buy_price (Union[Unset, str]): Purchase price (numeric string with up to 2 decimal places)
        buy_date (Union[Unset, str]): Purchase date in YYYY-MM-DD format
        sell_price (Union[Unset, str]): Listed selling price (numeric string with up to 2 decimal places)
        sold_price (Union[Unset, str]): Actual sold price (numeric string with up to 2 decimal places)
        sold_date (Union[Unset, str]): Sale date in YYYY-MM-DD format
    """

    card_id: UUID
    parallel_id: Union[Unset, UUID] = UNSET
    grade_id: Union[Unset, UUID] = UNSET
    quantity: Union[Unset, float] = 1.0
    buy_price: Union[Unset, str] = UNSET
    buy_date: Union[Unset, str] = UNSET
    sell_price: Union[Unset, str] = UNSET
    sold_price: Union[Unset, str] = UNSET
    sold_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = str(self.card_id)

        parallel_id: Union[Unset, str] = UNSET
        if not isinstance(self.parallel_id, Unset):
            parallel_id = str(self.parallel_id)

        grade_id: Union[Unset, str] = UNSET
        if not isinstance(self.grade_id, Unset):
            grade_id = str(self.grade_id)

        quantity = self.quantity

        buy_price = self.buy_price

        buy_date = self.buy_date

        sell_price = self.sell_price

        sold_price = self.sold_price

        sold_date = self.sold_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cardId": card_id,
            }
        )
        if parallel_id is not UNSET:
            field_dict["parallelId"] = parallel_id
        if grade_id is not UNSET:
            field_dict["gradeId"] = grade_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if buy_price is not UNSET:
            field_dict["buyPrice"] = buy_price
        if buy_date is not UNSET:
            field_dict["buyDate"] = buy_date
        if sell_price is not UNSET:
            field_dict["sellPrice"] = sell_price
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_id = UUID(d.pop("cardId"))

        _parallel_id = d.pop("parallelId", UNSET)
        parallel_id: Union[Unset, UUID]
        if isinstance(_parallel_id, Unset):
            parallel_id = UNSET
        else:
            parallel_id = UUID(_parallel_id)

        _grade_id = d.pop("gradeId", UNSET)
        grade_id: Union[Unset, UUID]
        if isinstance(_grade_id, Unset):
            grade_id = UNSET
        else:
            grade_id = UUID(_grade_id)

        quantity = d.pop("quantity", UNSET)

        buy_price = d.pop("buyPrice", UNSET)

        buy_date = d.pop("buyDate", UNSET)

        sell_price = d.pop("sellPrice", UNSET)

        sold_price = d.pop("soldPrice", UNSET)

        sold_date = d.pop("soldDate", UNSET)

        collection_card_item_input = cls(
            card_id=card_id,
            parallel_id=parallel_id,
            grade_id=grade_id,
            quantity=quantity,
            buy_price=buy_price,
            buy_date=buy_date,
            sell_price=sell_price,
            sold_price=sold_price,
            sold_date=sold_date,
        )

        collection_card_item_input.additional_properties = d
        return collection_card_item_input

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
