from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_message import ServerMessage


T = TypeVar("T", bound="DetectCardResponse")


@_attrs_define
class DetectCardResponse:
    """
    Attributes:
        detected (bool): Whether one or more trading cards were detected in the image
        count (int): Number of trading cards detected in the image
        request_id (str): Unique identifier for tracking this detection request
        processing_time (float): Total processing time in milliseconds
        messages (Union[Unset, list['ServerMessage']]): Server advisory messages (e.g., image quality warnings)
    """

    detected: bool
    count: int
    request_id: str
    processing_time: float
    messages: Union[Unset, list["ServerMessage"]] = UNSET

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
        from ..models.server_message import ServerMessage

        d = dict(src_dict)
        detected = d.pop("detected")

        count = d.pop("count")

        request_id = d.pop("requestId")

        processing_time = d.pop("processingTime")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ServerMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        detect_card_response = cls(
            detected=detected,
            count=count,
            request_id=request_id,
            processing_time=processing_time,
            messages=messages,
        )

        return detect_card_response
