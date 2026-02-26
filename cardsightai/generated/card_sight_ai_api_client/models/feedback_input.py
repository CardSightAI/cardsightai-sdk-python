from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.feedback_input_feedback_type import FeedbackInputFeedbackType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackInput")


@_attrs_define
class FeedbackInput:
    """
    Attributes:
        message (str):
        feedback_type (Union[Unset, FeedbackInputFeedbackType]): FeedbackType
    """

    message: str
    feedback_type: Union[Unset, FeedbackInputFeedbackType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        feedback_type: Union[Unset, str] = UNSET
        if not isinstance(self.feedback_type, Unset):
            feedback_type = self.feedback_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
            }
        )
        if feedback_type is not UNSET:
            field_dict["feedback_type"] = feedback_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        _feedback_type = d.pop("feedback_type", UNSET)
        feedback_type: Union[Unset, FeedbackInputFeedbackType]
        if isinstance(_feedback_type, Unset):
            feedback_type = UNSET
        else:
            feedback_type = FeedbackInputFeedbackType(_feedback_type)

        feedback_input = cls(
            message=message,
            feedback_type=feedback_type,
        )

        return feedback_input
