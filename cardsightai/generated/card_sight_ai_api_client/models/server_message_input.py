from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_input_type import ServerMessageInputType

T = TypeVar("T", bound="ServerMessageInput")


@_attrs_define
class ServerMessageInput:
    """
    Attributes:
        type_ (ServerMessageInputType): Message severity level
        message (str): Human-readable message text
    """

    type_: ServerMessageInputType
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        type_ = ServerMessageInputType(d.pop("type"))

        message = d.pop("message")

        server_message_input = cls(
            type_=type_,
            message=message,
        )

        server_message_input.additional_properties = d
        return server_message_input

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
