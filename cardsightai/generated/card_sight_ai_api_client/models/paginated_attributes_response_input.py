from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.detailed_attribute_response_input import DetailedAttributeResponseInput


T = TypeVar("T", bound="PaginatedAttributesResponseInput")


@_attrs_define
class PaginatedAttributesResponseInput:
    """
    Attributes:
        attributes (list['DetailedAttributeResponseInput']): Array of card attribute entities (e.g., Rookie Card,
            Autograph, Memorabilia)
        total_count (float): Total number of attributes matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    attributes: list["DetailedAttributeResponseInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.detailed_attribute_response_input import DetailedAttributeResponseInput

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = DetailedAttributeResponseInput.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_attributes_response_input = cls(
            attributes=attributes,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_attributes_response_input.additional_properties = d
        return paginated_attributes_response_input

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
