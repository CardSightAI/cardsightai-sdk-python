from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segment_input import SegmentInput


T = TypeVar("T", bound="PaginatedSegmentsResponseInput")


@_attrs_define
class PaginatedSegmentsResponseInput:
    """
    Attributes:
        segments (list['SegmentInput']): Array of market segment entities (e.g., Sports, Entertainment, Gaming)
        total_count (float): Total number of segments matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    segments: list["SegmentInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.segment_input import SegmentInput

        d = dict(src_dict)
        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = SegmentInput.from_dict(segments_item_data)

            segments.append(segments_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_segments_response_input = cls(
            segments=segments,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_segments_response_input.additional_properties = d
        return paginated_segments_response_input

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
