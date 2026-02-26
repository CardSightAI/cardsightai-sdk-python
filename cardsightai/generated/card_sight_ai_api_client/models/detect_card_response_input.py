from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DetectCardResponseInput")


@_attrs_define
class DetectCardResponseInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detected = self.detected

        count = self.count

        request_id = self.request_id

        processing_time = self.processing_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        detect_card_response_input = cls(
            detected=detected,
            count=count,
            request_id=request_id,
            processing_time=processing_time,
        )

        detect_card_response_input.additional_properties = d
        return detect_card_response_input

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
