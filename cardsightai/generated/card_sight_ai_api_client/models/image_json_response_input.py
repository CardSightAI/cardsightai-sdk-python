from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageJsonResponseInput")


@_attrs_define
class ImageJsonResponseInput:
    """
    Attributes:
        data (str): Base64 data URI (ready for use in HTML img src)
        content_type (str): MIME type of the image
        size (Union[Unset, float]): Size of the image in bytes
    """

    data: str
    content_type: str
    size: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        content_type = self.content_type

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "contentType": content_type,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data")

        content_type = d.pop("contentType")

        size = d.pop("size", UNSET)

        image_json_response_input = cls(
            data=data,
            content_type=content_type,
            size=size,
        )

        image_json_response_input.additional_properties = d
        return image_json_response_input

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
