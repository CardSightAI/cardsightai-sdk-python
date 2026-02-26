from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parallel_with_set_input import ParallelWithSetInput


T = TypeVar("T", bound="PaginatedParallelsResponseInput")


@_attrs_define
class PaginatedParallelsResponseInput:
    """
    Attributes:
        parallels (list['ParallelWithSetInput']): Array of parallel variants with associated set information (e.g.,
            Refractor, Prizm, numbered parallels)
        total_count (float): Total number of parallels matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    parallels: list["ParallelWithSetInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parallels = []
        for parallels_item_data in self.parallels:
            parallels_item = parallels_item_data.to_dict()
            parallels.append(parallels_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parallels": parallels,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parallel_with_set_input import ParallelWithSetInput

        d = dict(src_dict)
        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = ParallelWithSetInput.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_parallels_response_input = cls(
            parallels=parallels,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_parallels_response_input.additional_properties = d
        return paginated_parallels_response_input

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
