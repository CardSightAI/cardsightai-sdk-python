from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.feedback_response import FeedbackResponse


T = TypeVar("T", bound="FeedbackSubmitResponse")


@_attrs_define
class FeedbackSubmitResponse:
    """
    Attributes:
        success (bool):
        message (str):
        data (FeedbackResponse):
    """

    success: bool
    message: str
    data: "FeedbackResponse"

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
                "message": message,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_response import FeedbackResponse

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        data = FeedbackResponse.from_dict(d.pop("data"))

        feedback_submit_response = cls(
            success=success,
            message=message,
            data=data,
        )

        return feedback_submit_response
