from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CollectionOverview")


@_attrs_define
class CollectionOverview:
    """
    Attributes:
        total_cards (float): Total number of card entries in collection
        unique_cards (float): Number of unique cards (ignoring duplicates)
        total_quantity (float): Total quantity including all duplicates
    """

    total_cards: float
    unique_cards: float
    total_quantity: float

    def to_dict(self) -> dict[str, Any]:
        total_cards = self.total_cards

        unique_cards = self.unique_cards

        total_quantity = self.total_quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "totalCards": total_cards,
                "uniqueCards": unique_cards,
                "totalQuantity": total_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_cards = d.pop("totalCards")

        unique_cards = d.pop("uniqueCards")

        total_quantity = d.pop("totalQuantity")

        collection_overview = cls(
            total_cards=total_cards,
            unique_cards=unique_cards,
            total_quantity=total_quantity,
        )

        return collection_overview
