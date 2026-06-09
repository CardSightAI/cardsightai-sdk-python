from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pricing_record_input import PricingRecordInput


T = TypeVar("T", bound="RawPricingSectionInput")


@_attrs_define
class RawPricingSectionInput:
    """
    Attributes:
        period_days (Union[None, int]): Period in days that was applied
        count (int): Number of records
        records (list['PricingRecordInput']): Pricing records for ungraded cards
    """

    period_days: Union[None, int]
    count: int
    records: list["PricingRecordInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_days: Union[None, int]
        period_days = self.period_days

        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.pricing_record_input import PricingRecordInput

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
            records_item = PricingRecordInput.from_dict(records_item_data)

            records.append(records_item)

        raw_pricing_section_input = cls(
            period_days=period_days,
            count=count,
            records=records,
        )

        raw_pricing_section_input.additional_properties = d
        return raw_pricing_section_input

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
