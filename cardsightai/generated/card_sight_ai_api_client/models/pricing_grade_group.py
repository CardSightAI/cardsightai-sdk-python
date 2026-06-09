from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pricing_record import PricingRecord


T = TypeVar("T", bound="PricingGradeGroup")


@_attrs_define
class PricingGradeGroup:
    """
    Attributes:
        grade_value (str): Grade value (e.g., "10", "9.5")
        grade_id (UUID): Grade UUID
        period_days (Union[None, int]): Period in days that was applied
        count (int): Number of records in this group
        records (list['PricingRecord']): Pricing records for this grade
    """

    grade_value: str
    grade_id: UUID
    period_days: Union[None, int]
    count: int
    records: list["PricingRecord"]

    def to_dict(self) -> dict[str, Any]:
        grade_value = self.grade_value

        grade_id = str(self.grade_id)

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
                "grade_value": grade_value,
                "grade_id": grade_id,
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
        grade_value = d.pop("grade_value")

        grade_id = UUID(d.pop("grade_id"))

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

        pricing_grade_group = cls(
            grade_value=grade_value,
            grade_id=grade_id,
            period_days=period_days,
            count=count,
            records=records,
        )

        return pricing_grade_group
