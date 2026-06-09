from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionBreakdownSummary")


@_attrs_define
class CollectionBreakdownSummary:
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

    def to_dict(self) -> dict[str, Any]:
        total_groups = self.total_groups

        total_cards = self.total_cards

        total_quantity = self.total_quantity

        grouped_by = self.grouped_by

        total_invested = self.total_invested

        field_dict: dict[str, Any] = {}

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

        collection_breakdown_summary = cls(
            total_groups=total_groups,
            total_cards=total_cards,
            total_quantity=total_quantity,
            grouped_by=grouped_by,
            total_invested=total_invested,
        )

        return collection_breakdown_summary
