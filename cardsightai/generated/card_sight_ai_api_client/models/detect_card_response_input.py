from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_message_input import ServerMessageInput


T = TypeVar("T", bound="DetectCardResponseInput")


@_attrs_define
class DetectCardResponseInput:
    """
    Attributes:
        detected (bool): Whether one or more trading cards were detected in the image
        count (int): Number of trading cards detected in the image
        request_id (str): Unique identifier for tracking this detection request
        processing_time (float): Total processing time in milliseconds
        messages (Union[Unset, list['ServerMessageInput']]): Server advisory messages (e.g., image quality warnings)
    """

    detected: bool
    count: int
    request_id: str
    processing_time: float
    messages: Union[Unset, list["ServerMessageInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detected = self.detected

        count = self.count

        request_id = self.request_id

        processing_time = self.processing_time

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

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
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_message_input import ServerMessageInput

        d = dict(src_dict)
        detected = d.pop("detected")

        count = d.pop("count")

        request_id = d.pop("requestId")

        processing_time = d.pop("processingTime")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ServerMessageInput.from_dict(messages_item_data)

            messages.append(messages_item)

        detect_card_response_input = cls(
            detected=detected,
            count=count,
            request_id=request_id,
            processing_time=processing_time,
            messages=messages,
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
