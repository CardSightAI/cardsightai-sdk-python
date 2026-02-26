from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageJsonResponse")


@_attrs_define
class ImageJsonResponse:
    """
    Attributes:
        data (str): Base64 data URI (ready for use in HTML img src)
        content_type (str): MIME type of the image
        size (Union[Unset, float]): Size of the image in bytes
    """

    data: str
    content_type: str
    size: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        content_type = self.content_type

        size = self.size

        field_dict: dict[str, Any] = {}

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

        image_json_response = cls(
            data=data,
            content_type=content_type,
            size=size,
        )

        return image_json_response
