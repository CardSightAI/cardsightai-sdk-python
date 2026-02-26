from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.segment import Segment


T = TypeVar("T", bound="PaginatedSegmentsResponse")


@_attrs_define
class PaginatedSegmentsResponse:
    """
    Attributes:
        segments (list['Segment']): Array of market segment entities (e.g., Sports, Entertainment, Gaming)
        total_count (float): Total number of segments matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    segments: list["Segment"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segments": segments,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment import Segment

        d = dict(src_dict)
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = Segment.from_dict(segments_item_data)

            segments.append(segments_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_segments_response = cls(
            segments=segments,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_segments_response
