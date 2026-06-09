from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.detailed_field_response import DetailedFieldResponse


T = TypeVar("T", bound="PaginatedFieldsResponse")


@_attrs_define
class PaginatedFieldsResponse:
    """
    Attributes:
        fields (list['DetailedFieldResponse']): Array of field definitions with total usage counts across cards, sets,
            releases, and segments
        total_count (float): Total number of fields matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    fields: list["DetailedFieldResponse"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detailed_field_response import DetailedFieldResponse

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = DetailedFieldResponse.from_dict(fields_item_data)

            fields.append(fields_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_fields_response = cls(
            fields=fields,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_fields_response
