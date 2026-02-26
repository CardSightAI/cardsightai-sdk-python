from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.best_performing_group_input import BestPerformingGroupInput
    from ..models.most_valuable_group_input import MostValuableGroupInput


T = TypeVar("T", bound="CollectionBreakdownSummaryInput")


@_attrs_define
class CollectionBreakdownSummaryInput:
    """
    Attributes:
        total_groups (float): Total number of groups
        total_cards (float): Total number of cards in collection
        total_quantity (float): Total quantity including duplicates
        grouped_by (str): The dimension used for grouping
        total_value (Union[Unset, str]): Total collection value
        total_invested (Union[Unset, str]): Total amount invested
        overall_roi (Union[Unset, float]): Overall ROI percentage
        most_valuable_group (Union[Unset, MostValuableGroupInput]):
        best_performing_group (Union[Unset, BestPerformingGroupInput]):
    """

    total_groups: float
    total_cards: float
    total_quantity: float
    grouped_by: str
    total_value: Union[Unset, str] = UNSET
    total_invested: Union[Unset, str] = UNSET
    overall_roi: Union[Unset, float] = UNSET
    most_valuable_group: Union[Unset, "MostValuableGroupInput"] = UNSET
    best_performing_group: Union[Unset, "BestPerformingGroupInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.best_performing_group_input import BestPerformingGroupInput
        from ..models.most_valuable_group_input import MostValuableGroupInput

        d = dict(src_dict)
        total_groups = d.pop("totalGroups")

        total_cards = d.pop("totalCards")

        total_quantity = d.pop("totalQuantity")

        grouped_by = d.pop("groupedBy")

        total_value = d.pop("totalValue", UNSET)

        total_invested = d.pop("totalInvested", UNSET)

        overall_roi = d.pop("overallRoi", UNSET)

        _most_valuable_group = d.pop("mostValuableGroup", UNSET)
        most_valuable_group: Union[Unset, MostValuableGroupInput]
        if isinstance(_most_valuable_group, Unset):
            most_valuable_group = UNSET
        else:
            most_valuable_group = MostValuableGroupInput.from_dict(_most_valuable_group)

        _best_performing_group = d.pop("bestPerformingGroup", UNSET)
        best_performing_group: Union[Unset, BestPerformingGroupInput]
        if isinstance(_best_performing_group, Unset):
            best_performing_group = UNSET
        else:
            best_performing_group = BestPerformingGroupInput.from_dict(_best_performing_group)

        collection_breakdown_summary_input = cls(
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
