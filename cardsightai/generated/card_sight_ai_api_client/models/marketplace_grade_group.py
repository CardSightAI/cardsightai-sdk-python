from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.marketplace_record import MarketplaceRecord


T = TypeVar("T", bound="MarketplaceGradeGroup")


@_attrs_define
class MarketplaceGradeGroup:
    """
    Attributes:
        grade_value (str): Grade value
        grade_id (UUID): Grade UUID
        count (int): Number of listings
        records (list['MarketplaceRecord']): Active listings for this grade
    """

    grade_value: str
    grade_id: UUID
    count: int
    records: list["MarketplaceRecord"]

    def to_dict(self) -> dict[str, Any]:
        grade_value = self.grade_value

        grade_id = str(self.grade_id)

        count = self.count

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        field_dict: dict[str, Any] = {}

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
        from ..models.marketplace_record import MarketplaceRecord

        d = dict(src_dict)
        grade_value = d.pop("grade_value")

        grade_id = UUID(d.pop("grade_id"))

        count = d.pop("count")

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = MarketplaceRecord.from_dict(records_item_data)

            records.append(records_item)

        marketplace_grade_group = cls(
            grade_value=grade_value,
            grade_id=grade_id,
            count=count,
            records=records,
        )

        return marketplace_grade_group
