from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feedback_input_input_feedback_type import FeedbackInputInputFeedbackType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackInputInput")


@_attrs_define
class FeedbackInputInput:
    """
    Attributes:
        message (str): Detailed description of the feedback. Include specifics such as what is wrong, what you expected,
            or what you suggest. Max 1000 characters.
        feedback_type (Union[Unset, FeedbackInputInputFeedbackType]): Category of feedback. Accepted values: data_error
            (incorrect data), missing_data (something is missing from the catalog), suggestion (improvement idea), bug
            (something is broken), other (does not fit other categories)
    """

    message: str
    feedback_type: Union[Unset, FeedbackInputInputFeedbackType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        feedback_type: Union[Unset, str] = UNSET
        if not isinstance(self.feedback_type, Unset):
            feedback_type = self.feedback_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        feedback_type: Union[Unset, FeedbackInputInputFeedbackType]
        if isinstance(_feedback_type, Unset):
            feedback_type = UNSET
        else:
            feedback_type = FeedbackInputInputFeedbackType(_feedback_type)

        feedback_input_input = cls(
            message=message,
            feedback_type=feedback_type,
        )

        feedback_input_input.additional_properties = d
        return feedback_input_input

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
