from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketplace_record_input import MarketplaceRecordInput


T = TypeVar("T", bound="RawMarketplaceSectionInput")


@_attrs_define
class RawMarketplaceSectionInput:
    """
    Attributes:
        count (int): Number of active listings
        records (list['MarketplaceRecordInput']): Active marketplace listings
    """

    count: int
    records: list["MarketplaceRecordInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_record_input import MarketplaceRecordInput

        d = dict(src_dict)
        count = d.pop("count")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = MarketplaceRecordInput.from_dict(records_item_data)

            records.append(records_item)

        raw_marketplace_section_input = cls(
            count=count,
            records=records,
        )

        raw_marketplace_section_input.additional_properties = d
        return raw_marketplace_section_input

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
