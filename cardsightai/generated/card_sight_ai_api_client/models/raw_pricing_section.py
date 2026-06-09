from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pricing_record import PricingRecord


T = TypeVar("T", bound="RawPricingSection")


@_attrs_define
class RawPricingSection:
    """
    Attributes:
        period_days (Union[None, int]): Period in days that was applied
        count (int): Number of records
        records (list['PricingRecord']): Pricing records for ungraded cards
    """

    period_days: Union[None, int]
    count: int
    records: list["PricingRecord"]

    def to_dict(self) -> dict[str, Any]:
        period_days: Union[None, int]
        period_days = self.period_days

        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "period_days": period_days,
                "count": count,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_record import PricingRecord

        d = dict(src_dict)

        def _parse_period_days(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        period_days = _parse_period_days(d.pop("period_days"))

        count = d.pop("count")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = PricingRecord.from_dict(records_item_data)

            records.append(records_item)

        raw_pricing_section = cls(
            period_days=period_days,
            count=count,
            records=records,
        )

        return raw_pricing_section
