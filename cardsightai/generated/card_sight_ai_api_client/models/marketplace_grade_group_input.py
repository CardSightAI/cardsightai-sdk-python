from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketplace_record_input import MarketplaceRecordInput


T = TypeVar("T", bound="MarketplaceGradeGroupInput")


@_attrs_define
class MarketplaceGradeGroupInput:
    """
    Attributes:
        grade_value (str): Grade value
        grade_id (UUID): Grade UUID
        count (int): Number of listings
        records (list['MarketplaceRecordInput']): Active listings for this grade
    """

    grade_value: str
    grade_id: UUID
    count: int
    records: list["MarketplaceRecordInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grade_value = self.grade_value

        grade_id = str(self.grade_id)

        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grade_value": grade_value,
                "grade_id": grade_id,
                "count": count,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_record_input import MarketplaceRecordInput

        d = dict(src_dict)
        grade_value = d.pop("grade_value")

        grade_id = UUID(d.pop("grade_id"))

        count = d.pop("count")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = MarketplaceRecordInput.from_dict(records_item_data)

            records.append(records_item)

        marketplace_grade_group_input = cls(
            grade_value=grade_value,
            grade_id=grade_id,
            count=count,
            records=records,
        )

        marketplace_grade_group_input.additional_properties = d
        return marketplace_grade_group_input

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
