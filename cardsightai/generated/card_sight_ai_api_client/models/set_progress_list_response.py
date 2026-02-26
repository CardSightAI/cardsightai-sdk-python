from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.set_progress import SetProgress
    from ..models.set_progress_summary import SetProgressSummary


T = TypeVar("T", bound="SetProgressListResponse")


@_attrs_define
class SetProgressListResponse:
    """
    Attributes:
        summary (SetProgressSummary):
        sets (list['SetProgress']): Array of set progress entries
        total_count (float): Total number of sets matching filters
        skip (float): Number of records skipped
        take (float): Number of records returned
    """

    summary: "SetProgressSummary"
    sets: list["SetProgress"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
                "sets": sets,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.set_progress import SetProgress
        from ..models.set_progress_summary import SetProgressSummary

        d = dict(src_dict)
        summary = SetProgressSummary.from_dict(d.pop("summary"))

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = SetProgress.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        set_progress_list_response = cls(
            summary=summary,
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return set_progress_list_response
