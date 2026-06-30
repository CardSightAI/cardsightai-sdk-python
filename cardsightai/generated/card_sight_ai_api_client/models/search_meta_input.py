from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.source_breakdown_item_input import SourceBreakdownItemInput


T = TypeVar("T", bound="SearchMetaInput")


@_attrs_define
class SearchMetaInput:
    """
    Attributes:
        sources (list['SourceBreakdownItemInput']): Breakdown by data source
        total_records (int): Total records returned
    """

    sources: list["SourceBreakdownItemInput"]
    total_records: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        total_records = self.total_records

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sources": sources,
                "total_records": total_records,
            }
        )

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

        search_meta_input = cls(
            sources=sources,
            total_records=total_records,
        )

        search_meta_input.additional_properties = d
        return search_meta_input

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
