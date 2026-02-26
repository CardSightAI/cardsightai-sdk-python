from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CollectionOverviewInput")


@_attrs_define
class CollectionOverviewInput:
    """
    Attributes:
        total_cards (float): Total number of card entries in collection
        unique_cards (float): Number of unique cards (ignoring duplicates)
        total_quantity (float): Total quantity including all duplicates
    """

    total_cards: float
    unique_cards: float
    total_quantity: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_cards = self.total_cards

        unique_cards = self.unique_cards

        total_quantity = self.total_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        collection_overview_input = cls(
            total_cards=total_cards,
            unique_cards=unique_cards,
            total_quantity=total_quantity,
        )

        collection_overview_input.additional_properties = d
        return collection_overview_input

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
