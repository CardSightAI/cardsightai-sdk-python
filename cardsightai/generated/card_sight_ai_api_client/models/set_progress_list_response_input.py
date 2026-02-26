from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_progress_input import SetProgressInput
    from ..models.set_progress_summary_input import SetProgressSummaryInput


T = TypeVar("T", bound="SetProgressListResponseInput")


@_attrs_define
class SetProgressListResponseInput:
    """
    Attributes:
        summary (SetProgressSummaryInput):
        sets (list['SetProgressInput']): Array of set progress entries
        total_count (float): Total number of sets matching filters
        skip (float): Number of records skipped
        take (float): Number of records returned
    """

    summary: "SetProgressSummaryInput"
    sets: list["SetProgressInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.set_progress_input import SetProgressInput
        from ..models.set_progress_summary_input import SetProgressSummaryInput

        d = dict(src_dict)
        summary = SetProgressSummaryInput.from_dict(d.pop("summary"))

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = SetProgressInput.from_dict(sets_item_data)

            sets.append(sets_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        set_progress_list_response_input = cls(
            summary=summary,
            sets=sets,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        set_progress_list_response_input.additional_properties = d
        return set_progress_list_response_input

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
