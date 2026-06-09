from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetProgressSummary")


@_attrs_define
class SetProgressSummary:
    """
    Attributes:
        total_sets (float): Total number of sets represented in collection
        near_complete_sets (float): Number of sets >80% complete
        fully_complete_sets (float): Number of fully complete sets
    """

    total_sets: float
    near_complete_sets: float
    fully_complete_sets: float

    def to_dict(self) -> dict[str, Any]:
        total_sets = self.total_sets

        near_complete_sets = self.near_complete_sets

        fully_complete_sets = self.fully_complete_sets

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "totalSets": total_sets,
                "nearCompleteSets": near_complete_sets,
                "fullyCompleteSets": fully_complete_sets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_sets = d.pop("totalSets")

        near_complete_sets = d.pop("nearCompleteSets")

        fully_complete_sets = d.pop("fullyCompleteSets")

        set_progress_summary = cls(
            total_sets=total_sets,
            near_complete_sets=near_complete_sets,
            fully_complete_sets=fully_complete_sets,
        )

        return set_progress_summary
