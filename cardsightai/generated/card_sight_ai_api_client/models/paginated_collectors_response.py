from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collector import Collector


T = TypeVar("T", bound="PaginatedCollectorsResponse")


@_attrs_define
class PaginatedCollectorsResponse:
    """
    Attributes:
        collectors (list['Collector']):
        total_count (float):
        skip (float):
        take (float):
    """

    collectors: list["Collector"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        collectors = []
        for collectors_item_data in self.collectors:
            collectors_item = collectors_item_data.to_dict()
            collectors.append(collectors_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collectors": collectors,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collector import Collector

        d = dict(src_dict)
        collectors = []
        _collectors = d.pop("collectors")
        for collectors_item_data in _collectors:
            collectors_item = Collector.from_dict(collectors_item_data)

            collectors.append(collectors_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_collectors_response = cls(
            collectors=collectors,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_collectors_response
