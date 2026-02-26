from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionCard")


@_attrs_define
class CollectionCard:
    """
    Attributes:
        id (UUID): Unique identifier for the collection card
        collection_id (UUID): ID of the collection this card belongs to
        card_id (UUID): ID of the card
        quantity (float): Quantity of this card in the collection Default: 1.0.
        parallel_id (Union[Unset, UUID]): ID of the card parallel if applicable
        grade_id (Union[Unset, UUID]): UUID of the grade if card is graded
        buy_price (Union[Unset, str]): Purchase price of the card
        buy_date (Union[Unset, str]): Date the card was purchased (YYYY-MM-DD)
        sell_price (Union[Unset, str]): Listed selling price of the card
        sold_price (Union[Unset, str]): Actual sold price of the card
        sold_date (Union[Unset, str]): Date the card was sold (YYYY-MM-DD)
    """

    id: UUID
    collection_id: UUID
    card_id: UUID
    quantity: float = 1.0
    parallel_id: Union[Unset, UUID] = UNSET
    grade_id: Union[Unset, UUID] = UNSET
    buy_price: Union[Unset, str] = UNSET
    buy_date: Union[Unset, str] = UNSET
    sell_price: Union[Unset, str] = UNSET
    sold_price: Union[Unset, str] = UNSET
    sold_date: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        collection_id = str(self.collection_id)

        card_id = str(self.card_id)

        quantity = self.quantity

        parallel_id: Union[Unset, str] = UNSET
        if not isinstance(self.parallel_id, Unset):
            parallel_id = str(self.parallel_id)

        grade_id: Union[Unset, str] = UNSET
        if not isinstance(self.grade_id, Unset):
            grade_id = str(self.grade_id)

        buy_price = self.buy_price

        buy_date = self.buy_date

        sell_price = self.sell_price

        sold_price = self.sold_price

        sold_date = self.sold_date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "collectionId": collection_id,
                "cardId": card_id,
                "quantity": quantity,
            }
        )
        if parallel_id is not UNSET:
            field_dict["parallelId"] = parallel_id
        if grade_id is not UNSET:
            field_dict["gradeId"] = grade_id
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
        id = UUID(d.pop("id"))

        collection_id = UUID(d.pop("collectionId"))

        card_id = UUID(d.pop("cardId"))

        quantity = d.pop("quantity")

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

        buy_price = d.pop("buyPrice", UNSET)

        buy_date = d.pop("buyDate", UNSET)

        sell_price = d.pop("sellPrice", UNSET)

        sold_price = d.pop("soldPrice", UNSET)

        sold_date = d.pop("soldDate", UNSET)

        collection_card = cls(
            id=id,
            collection_id=collection_id,
            card_id=card_id,
            quantity=quantity,
            parallel_id=parallel_id,
            grade_id=grade_id,
            buy_price=buy_price,
            buy_date=buy_date,
            sell_price=sell_price,
            sold_price=sold_price,
            sold_date=sold_date,
        )

        return collection_card
