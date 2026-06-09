from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.release_calendar_entry_input import ReleaseCalendarEntryInput


T = TypeVar("T", bound="PaginatedReleaseCalendarResponseInput")


@_attrs_define
class PaginatedReleaseCalendarResponseInput:
    """
    Attributes:
        release_calendar (list['ReleaseCalendarEntryInput']): List of release calendar entries
        total_count (float): Total number of entries matching the query
        skip (float): Number of items skipped (offset)
        take (float): Number of items included in this page
    """

    release_calendar: list["ReleaseCalendarEntryInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_calendar = []
        for release_calendar_item_data in self.release_calendar:
            release_calendar_item = release_calendar_item_data.to_dict()
            release_calendar.append(release_calendar_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "release_calendar": release_calendar,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_calendar_entry_input import ReleaseCalendarEntryInput

        d = dict(src_dict)
        release_calendar = []
        _release_calendar = d.pop("release_calendar")
        for release_calendar_item_data in _release_calendar:
            release_calendar_item = ReleaseCalendarEntryInput.from_dict(release_calendar_item_data)

            release_calendar.append(release_calendar_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_release_calendar_response_input = cls(
            release_calendar=release_calendar,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_release_calendar_response_input.additional_properties = d
        return paginated_release_calendar_response_input

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
