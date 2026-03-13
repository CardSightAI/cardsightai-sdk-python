from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identification_data_input import IdentificationDataInput


T = TypeVar("T", bound="IdentifyCardResponseInput")


@_attrs_define
class IdentifyCardResponseInput:
    """
    Attributes:
        success (bool): Whether the identification process completed successfully
        request_id (str): Unique identifier for tracking this identification request
        detections (Union[Unset, list['IdentificationDataInput']]): Array of card detections from the image. Multiple
            cards may be detected in a single image. Each detection may include grading data if the card is inside a graded
            slab. Empty if no cards found.
        processing_time (Union[Unset, float]): Total processing time in milliseconds for AI analysis and catalog
            matching
    """

    success: bool
    request_id: str
    detections: Union[Unset, list["IdentificationDataInput"]] = UNSET
    processing_time: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        request_id = self.request_id

        detections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.detections, Unset):
            detections = []
            for detections_item_data in self.detections:
                detections_item = detections_item_data.to_dict()
                detections.append(detections_item)

        processing_time = self.processing_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "requestId": request_id,
            }
        )
        if detections is not UNSET:
            field_dict["detections"] = detections
        if processing_time is not UNSET:
            field_dict["processingTime"] = processing_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identification_data_input import IdentificationDataInput

        d = dict(src_dict)
        success = d.pop("success")

        request_id = d.pop("requestId")

        detections = []
        _detections = d.pop("detections", UNSET)
        for detections_item_data in _detections or []:
            detections_item = IdentificationDataInput.from_dict(detections_item_data)

            detections.append(detections_item)

        processing_time = d.pop("processingTime", UNSET)

        identify_card_response_input = cls(
            success=success,
            request_id=request_id,
            detections=detections,
            processing_time=processing_time,
        )

        identify_card_response_input.additional_properties = d
        return identify_card_response_input

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
