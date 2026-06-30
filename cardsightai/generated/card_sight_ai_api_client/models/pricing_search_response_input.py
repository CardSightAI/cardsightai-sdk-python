from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pricing_search_query_echo_input import PricingSearchQueryEchoInput
    from ..models.pricing_search_record_input import PricingSearchRecordInput
    from ..models.search_meta_input import SearchMetaInput


T = TypeVar("T", bound="PricingSearchResponseInput")


@_attrs_define
class PricingSearchResponseInput:
    """
    Attributes:
        query (PricingSearchQueryEchoInput):
        results (list['PricingSearchRecordInput']): Flat list of matched listings, ranked by title relevance. Spans
            multiple cards and may include unmatched listings.
        meta (SearchMetaInput):
    """

    query: "PricingSearchQueryEchoInput"
    results: list["PricingSearchRecordInput"]
    meta: "SearchMetaInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "results": results,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_search_query_echo_input import PricingSearchQueryEchoInput
        from ..models.pricing_search_record_input import PricingSearchRecordInput
        from ..models.search_meta_input import SearchMetaInput

        d = dict(src_dict)
        query = PricingSearchQueryEchoInput.from_dict(d.pop("query"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PricingSearchRecordInput.from_dict(results_item_data)

            results.append(results_item)

        meta = SearchMetaInput.from_dict(d.pop("meta"))

        pricing_search_response_input = cls(
            query=query,
            results=results,
            meta=meta,
        )

        pricing_search_response_input.additional_properties = d
        return pricing_search_response_input

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
