from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.release_calendar_entry import ReleaseCalendarEntry


T = TypeVar("T", bound="PaginatedReleaseCalendarResponse")


@_attrs_define
class PaginatedReleaseCalendarResponse:
    """
    Attributes:
        release_calendar (list['ReleaseCalendarEntry']): List of release calendar entries
        total_count (float): Total number of entries matching the query
        skip (float): Number of items skipped (offset)
        take (float): Number of items included in this page
    """

    release_calendar: list["ReleaseCalendarEntry"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        release_calendar = []
        for release_calendar_item_data in self.release_calendar:
            release_calendar_item = release_calendar_item_data.to_dict()
            release_calendar.append(release_calendar_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.release_calendar_entry import ReleaseCalendarEntry

        d = dict(src_dict)
        release_calendar = []
        _release_calendar = d.pop("release_calendar")
        for release_calendar_item_data in _release_calendar:
            release_calendar_item = ReleaseCalendarEntry.from_dict(release_calendar_item_data)

            release_calendar.append(release_calendar_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_release_calendar_response = cls(
            release_calendar=release_calendar,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_release_calendar_response
