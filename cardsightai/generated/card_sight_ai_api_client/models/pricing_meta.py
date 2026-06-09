from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_breakdown_item import SourceBreakdownItem


T = TypeVar("T", bound="PricingMeta")


@_attrs_define
class PricingMeta:
    """
    Attributes:
        sources (list['SourceBreakdownItem']): Breakdown by data source
        total_records (int): Total records returned across all sections
        last_sale_date (Union[None, Unset, str]): Date of most recent sale
    """

    sources: list["SourceBreakdownItem"]
    total_records: int
    last_sale_date: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        total_records = self.total_records

        last_sale_date: Union[None, Unset, str]
        if isinstance(self.last_sale_date, Unset):
            last_sale_date = UNSET
        else:
            last_sale_date = self.last_sale_date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sources": sources,
                "total_records": total_records,
            }
        )
        if last_sale_date is not UNSET:
            field_dict["last_sale_date"] = last_sale_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_breakdown_item import SourceBreakdownItem

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceBreakdownItem.from_dict(sources_item_data)

            sources.append(sources_item)

        total_records = d.pop("total_records")

        def _parse_last_sale_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_sale_date = _parse_last_sale_date(d.pop("last_sale_date", UNSET))

        pricing_meta = cls(
            sources=sources,
            total_records=total_records,
            last_sale_date=last_sale_date,
        )

        return pricing_meta
