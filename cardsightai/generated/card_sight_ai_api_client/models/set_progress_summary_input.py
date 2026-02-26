from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetProgressSummaryInput")


@_attrs_define
class SetProgressSummaryInput:
    """
    Attributes:
        total_sets (float): Total number of sets represented in collection
        near_complete_sets (float): Number of sets >80% complete
        fully_complete_sets (float): Number of fully complete sets
        total_estimated_cost (Union[Unset, str]): Total cost to complete all sets
    """

    total_sets: float
    near_complete_sets: float
    fully_complete_sets: float
    total_estimated_cost: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_sets = self.total_sets

        near_complete_sets = self.near_complete_sets

        fully_complete_sets = self.fully_complete_sets

        total_estimated_cost = self.total_estimated_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSets": total_sets,
                "nearCompleteSets": near_complete_sets,
                "fullyCompleteSets": fully_complete_sets,
            }
        )
        if total_estimated_cost is not UNSET:
            field_dict["totalEstimatedCost"] = total_estimated_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_sets = d.pop("totalSets")

        near_complete_sets = d.pop("nearCompleteSets")

        fully_complete_sets = d.pop("fullyCompleteSets")

        total_estimated_cost = d.pop("totalEstimatedCost", UNSET)

        set_progress_summary_input = cls(
            total_sets=total_sets,
            near_complete_sets=near_complete_sets,
            fully_complete_sets=fully_complete_sets,
            total_estimated_cost=total_estimated_cost,
        )

        set_progress_summary_input.additional_properties = d
        return set_progress_summary_input

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
