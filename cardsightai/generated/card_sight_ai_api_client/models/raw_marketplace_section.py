from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.marketplace_record import MarketplaceRecord


T = TypeVar("T", bound="RawMarketplaceSection")


@_attrs_define
class RawMarketplaceSection:
    """
    Attributes:
        count (int): Number of active listings
        records (list['MarketplaceRecord']): Active marketplace listings
    """

    count: int
    records: list["MarketplaceRecord"]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_record import MarketplaceRecord

        d = dict(src_dict)
        count = d.pop("count")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = MarketplaceRecord.from_dict(records_item_data)

            records.append(records_item)

        raw_marketplace_section = cls(
            count=count,
            records=records,
        )

        return raw_marketplace_section
