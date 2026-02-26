from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.best_performing_group import BestPerformingGroup
    from ..models.most_valuable_group import MostValuableGroup


T = TypeVar("T", bound="CollectionBreakdownSummary")


@_attrs_define
class CollectionBreakdownSummary:
    """
    Attributes:
        total_groups (float): Total number of groups
        total_cards (float): Total number of cards in collection
        total_quantity (float): Total quantity including duplicates
        grouped_by (str): The dimension used for grouping
        total_value (Union[Unset, str]): Total collection value
        total_invested (Union[Unset, str]): Total amount invested
        overall_roi (Union[Unset, float]): Overall ROI percentage
        most_valuable_group (Union[Unset, MostValuableGroup]):
        best_performing_group (Union[Unset, BestPerformingGroup]):
    """

    total_groups: float
    total_cards: float
    total_quantity: float
    grouped_by: str
    total_value: Union[Unset, str] = UNSET
    total_invested: Union[Unset, str] = UNSET
    overall_roi: Union[Unset, float] = UNSET
    most_valuable_group: Union[Unset, "MostValuableGroup"] = UNSET
    best_performing_group: Union[Unset, "BestPerformingGroup"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_groups = self.total_groups

        total_cards = self.total_cards

        total_quantity = self.total_quantity

        grouped_by = self.grouped_by

        total_value = self.total_value

        total_invested = self.total_invested

        overall_roi = self.overall_roi

        most_valuable_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.most_valuable_group, Unset):
            most_valuable_group = self.most_valuable_group.to_dict()

        best_performing_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.best_performing_group, Unset):
            best_performing_group = self.best_performing_group.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "totalGroups": total_groups,
                "totalCards": total_cards,
                "totalQuantity": total_quantity,
                "groupedBy": grouped_by,
            }
        )
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value
        if total_invested is not UNSET:
            field_dict["totalInvested"] = total_invested
        if overall_roi is not UNSET:
            field_dict["overallRoi"] = overall_roi
        if most_valuable_group is not UNSET:
            field_dict["mostValuableGroup"] = most_valuable_group
        if best_performing_group is not UNSET:
            field_dict["bestPerformingGroup"] = best_performing_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.best_performing_group import BestPerformingGroup
        from ..models.most_valuable_group import MostValuableGroup

        d = dict(src_dict)
        total_groups = d.pop("totalGroups")

        total_cards = d.pop("totalCards")

        total_quantity = d.pop("totalQuantity")

        grouped_by = d.pop("groupedBy")

        total_value = d.pop("totalValue", UNSET)

        total_invested = d.pop("totalInvested", UNSET)

        overall_roi = d.pop("overallRoi", UNSET)

        _most_valuable_group = d.pop("mostValuableGroup", UNSET)
        most_valuable_group: Union[Unset, MostValuableGroup]
        if isinstance(_most_valuable_group, Unset):
            most_valuable_group = UNSET
        else:
            most_valuable_group = MostValuableGroup.from_dict(_most_valuable_group)

        _best_performing_group = d.pop("bestPerformingGroup", UNSET)
        best_performing_group: Union[Unset, BestPerformingGroup]
        if isinstance(_best_performing_group, Unset):
            best_performing_group = UNSET
        else:
            best_performing_group = BestPerformingGroup.from_dict(_best_performing_group)

        collection_breakdown_summary = cls(
            total_groups=total_groups,
            total_cards=total_cards,
            total_quantity=total_quantity,
            grouped_by=grouped_by,
            total_value=total_value,
            total_invested=total_invested,
            overall_roi=overall_roi,
            most_valuable_group=most_valuable_group,
            best_performing_group=best_performing_group,
        )

        return collection_breakdown_summary
