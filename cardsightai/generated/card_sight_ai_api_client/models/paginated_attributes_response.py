from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.detailed_attribute_response import DetailedAttributeResponse


T = TypeVar("T", bound="PaginatedAttributesResponse")


@_attrs_define
class PaginatedAttributesResponse:
    """
    Attributes:
        attributes (list['DetailedAttributeResponse']): Array of card attribute entities (e.g., Rookie Card, Autograph,
            Memorabilia)
        total_count (float): Total number of attributes matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    attributes: list["DetailedAttributeResponse"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detailed_attribute_response import DetailedAttributeResponse

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = DetailedAttributeResponse.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_attributes_response = cls(
            attributes=attributes,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_attributes_response
