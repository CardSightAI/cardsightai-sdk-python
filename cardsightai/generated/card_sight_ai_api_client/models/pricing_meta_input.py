from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_breakdown_item_input import SourceBreakdownItemInput


T = TypeVar("T", bound="PricingMetaInput")


@_attrs_define
class PricingMetaInput:
    """
    Attributes:
        sources (list['SourceBreakdownItemInput']): Breakdown by data source
        total_records (int): Total records returned across all sections
        last_sale_date (Union[None, Unset, str]): Date of most recent sale
    """

    sources: list["SourceBreakdownItemInput"]
    total_records: int
    last_sale_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.source_breakdown_item_input import SourceBreakdownItemInput

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceBreakdownItemInput.from_dict(sources_item_data)

            sources.append(sources_item)

        total_records = d.pop("total_records")

        def _parse_last_sale_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_sale_date = _parse_last_sale_date(d.pop("last_sale_date", UNSET))

        pricing_meta_input = cls(
            sources=sources,
            total_records=total_records,
            last_sale_date=last_sale_date,
        )

        pricing_meta_input.additional_properties = d
        return pricing_meta_input

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
