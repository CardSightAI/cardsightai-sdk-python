from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionBreakdownSummaryInput")


@_attrs_define
class CollectionBreakdownSummaryInput:
    """
    Attributes:
        total_groups (float): Total number of groups
        total_cards (float): Total number of cards in collection
        total_quantity (float): Total quantity including duplicates
        grouped_by (str): The dimension used for grouping
        total_invested (Union[Unset, str]): Total amount invested (sum of buy prices)
    """

    total_groups: float
    total_cards: float
    total_quantity: float
    grouped_by: str
    total_invested: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_groups = self.total_groups

        total_cards = self.total_cards

        total_quantity = self.total_quantity

        grouped_by = self.grouped_by

        total_invested = self.total_invested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalGroups": total_groups,
                "totalCards": total_cards,
                "totalQuantity": total_quantity,
                "groupedBy": grouped_by,
            }
        )
        if total_invested is not UNSET:
            field_dict["totalInvested"] = total_invested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_groups = d.pop("totalGroups")

        total_cards = d.pop("totalCards")

        total_quantity = d.pop("totalQuantity")

        grouped_by = d.pop("groupedBy")

        total_invested = d.pop("totalInvested", UNSET)

        collection_breakdown_summary_input = cls(
            total_groups=total_groups,
            total_cards=total_cards,
            total_quantity=total_quantity,
            grouped_by=grouped_by,
            total_invested=total_invested,
        )

        collection_breakdown_summary_input.additional_properties = d
        return collection_breakdown_summary_input

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
