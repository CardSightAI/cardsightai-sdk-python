from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_message_type import ServerMessageType

T = TypeVar("T", bound="ServerMessage")


@_attrs_define
class ServerMessage:
    """
    Attributes:
        type_ (ServerMessageType): Message severity level
        message (str): Human-readable message text
    """

    type_: ServerMessageType
    message: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ServerMessageType(d.pop("type"))

        message = d.pop("message")

        server_message = cls(
            type_=type_,
            message=message,
        )

        return server_message
