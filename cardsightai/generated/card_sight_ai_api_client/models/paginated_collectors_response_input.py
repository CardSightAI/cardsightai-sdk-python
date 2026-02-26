from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collector_input import CollectorInput


T = TypeVar("T", bound="PaginatedCollectorsResponseInput")


@_attrs_define
class PaginatedCollectorsResponseInput:
    """
    Attributes:
        collectors (list['CollectorInput']):
        total_count (float):
        skip (float):
        take (float):
    """

    collectors: list["CollectorInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collectors = []
        for collectors_item_data in self.collectors:
            collectors_item = collectors_item_data.to_dict()
            collectors.append(collectors_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.collector_input import CollectorInput

        d = dict(src_dict)
        collectors = []
        _collectors = d.pop("collectors")
        for collectors_item_data in _collectors:
            collectors_item = CollectorInput.from_dict(collectors_item_data)

            collectors.append(collectors_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_collectors_response_input = cls(
            collectors=collectors,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_collectors_response_input.additional_properties = d
        return paginated_collectors_response_input

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
