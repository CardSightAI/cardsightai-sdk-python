from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection_input import CollectionInput


T = TypeVar("T", bound="PaginatedCollectionsResponseInput")


@_attrs_define
class PaginatedCollectionsResponseInput:
    """
    Attributes:
        collections (list['CollectionInput']):
        total_count (float):
        skip (float):
        take (float):
    """

    collections: list["CollectionInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collections": collections,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_input import CollectionInput

        d = dict(src_dict)
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = CollectionInput.from_dict(collections_item_data)

            collections.append(collections_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_collections_response_input = cls(
            collections=collections,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_collections_response_input.additional_properties = d
        return paginated_collections_response_input

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
