from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_message_input_role import ConversationMessageInputRole

T = TypeVar("T", bound="ConversationMessageInput")


@_attrs_define
class ConversationMessageInput:
    """
    Attributes:
        role (ConversationMessageInputRole): The role of the message sender
        content (str): The message content
    """

    role: ConversationMessageInputRole
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = ConversationMessageInputRole(d.pop("role"))

        content = d.pop("content")

        conversation_message_input = cls(
            role=role,
            content=content,
        )

        conversation_message_input.additional_properties = d
        return conversation_message_input

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
