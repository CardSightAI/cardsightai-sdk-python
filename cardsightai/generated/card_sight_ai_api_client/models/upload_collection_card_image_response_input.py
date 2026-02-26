from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadCollectionCardImageResponseInput")


@_attrs_define
class UploadCollectionCardImageResponseInput:
    """
    Attributes:
        image_id (UUID): Unique identifier for the image record
        uploaded_at (str): Timestamp when the image was uploaded
        full_image_url (str): URL to retrieve the full-resolution image
        thumbnail_url (str): URL to retrieve the thumbnail image
    """

    image_id: UUID
    uploaded_at: str
    full_image_url: str
    thumbnail_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_id = str(self.image_id)

        uploaded_at = self.uploaded_at

        full_image_url = self.full_image_url

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "imageId": image_id,
                "uploadedAt": uploaded_at,
                "fullImageUrl": full_image_url,
                "thumbnailUrl": thumbnail_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_id = UUID(d.pop("imageId"))

        uploaded_at = d.pop("uploadedAt")

        full_image_url = d.pop("fullImageUrl")

        thumbnail_url = d.pop("thumbnailUrl")

        upload_collection_card_image_response_input = cls(
            image_id=image_id,
            uploaded_at=uploaded_at,
            full_image_url=full_image_url,
            thumbnail_url=thumbnail_url,
        )

        upload_collection_card_image_response_input.additional_properties = d
        return upload_collection_card_image_response_input

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
