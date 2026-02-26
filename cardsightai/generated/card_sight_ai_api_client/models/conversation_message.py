from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.conversation_message_role import ConversationMessageRole

T = TypeVar("T", bound="ConversationMessage")


@_attrs_define
class ConversationMessage:
    """
    Attributes:
        role (ConversationMessageRole): The role of the message sender
        content (str): The message content
    """

    role: ConversationMessageRole
    content: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        content = self.content

        field_dict: dict[str, Any] = {}

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
        role = ConversationMessageRole(d.pop("role"))

        content = d.pop("content")

        conversation_message = cls(
            role=role,
            content=content,
        )

        return conversation_message
