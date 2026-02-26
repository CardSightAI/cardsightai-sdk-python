from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.parallel_with_set import ParallelWithSet


T = TypeVar("T", bound="PaginatedParallelsResponse")


@_attrs_define
class PaginatedParallelsResponse:
    """
    Attributes:
        parallels (list['ParallelWithSet']): Array of parallel variants with associated set information (e.g.,
            Refractor, Prizm, numbered parallels)
        total_count (float): Total number of parallels matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    parallels: list["ParallelWithSet"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        parallels = []
        for parallels_item_data in self.parallels:
            parallels_item = parallels_item_data.to_dict()
            parallels.append(parallels_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.parallel_with_set import ParallelWithSet

        d = dict(src_dict)
        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = ParallelWithSet.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_parallels_response = cls(
            parallels=parallels,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_parallels_response
