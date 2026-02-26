from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collection import Collection


T = TypeVar("T", bound="PaginatedCollectionsResponse")


@_attrs_define
class PaginatedCollectionsResponse:
    """
    Attributes:
        collections (list['Collection']):
        total_count (float):
        skip (float):
        take (float):
    """

    collections: list["Collection"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.collection import Collection

        d = dict(src_dict)
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_collections_response = cls(
            collections=collections,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_collections_response
