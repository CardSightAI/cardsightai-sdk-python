from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import File

T = TypeVar("T", bound="FileUpload")


@_attrs_define
class FileUpload:
    """
    Attributes:
        image (File): The image file to analyze
    """

    image: File

    def to_dict(self) -> dict[str, Any]:
        image = self.image.to_tuple()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "image": image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = File(payload=BytesIO(d.pop("image")))

        file_upload = cls(
            image=image,
        )

        return file_upload
