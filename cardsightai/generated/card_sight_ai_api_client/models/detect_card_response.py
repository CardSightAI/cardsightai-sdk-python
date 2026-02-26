from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DetectCardResponse")


@_attrs_define
class DetectCardResponse:
    """
    Attributes:
        detected (bool): Whether one or more trading cards were detected in the image
        count (int): Number of trading cards detected in the image
        request_id (str): Unique identifier for tracking this detection request
        processing_time (float): Total processing time in milliseconds
    """

    detected: bool
    count: int
    request_id: str
    processing_time: float

    def to_dict(self) -> dict[str, Any]:
        detected = self.detected

        count = self.count

        request_id = self.request_id

        processing_time = self.processing_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "detected": detected,
                "count": count,
                "requestId": request_id,
                "processingTime": processing_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detected = d.pop("detected")

        count = d.pop("count")

        request_id = d.pop("requestId")

        processing_time = d.pop("processingTime")

        detect_card_response = cls(
            detected=detected,
            count=count,
            request_id=request_id,
            processing_time=processing_time,
        )

        return detect_card_response
