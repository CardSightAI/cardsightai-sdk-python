from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feedback_response_input import FeedbackResponseInput


T = TypeVar("T", bound="FeedbackSubmitResponseInput")


@_attrs_define
class FeedbackSubmitResponseInput:
    """
    Attributes:
        success (bool):
        message (str):
        data (FeedbackResponseInput):
    """

    success: bool
    message: str
    data: "FeedbackResponseInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.feedback_response_input import FeedbackResponseInput

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        data = FeedbackResponseInput.from_dict(d.pop("data"))

        feedback_submit_response_input = cls(
            success=success,
            message=message,
            data=data,
        )

        feedback_submit_response_input.additional_properties = d
        return feedback_submit_response_input

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
