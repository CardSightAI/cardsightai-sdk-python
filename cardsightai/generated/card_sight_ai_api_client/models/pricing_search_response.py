from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pricing_search_query_echo import PricingSearchQueryEcho
    from ..models.pricing_search_record import PricingSearchRecord
    from ..models.search_meta import SearchMeta


T = TypeVar("T", bound="PricingSearchResponse")


@_attrs_define
class PricingSearchResponse:
    """
    Attributes:
        query (PricingSearchQueryEcho):
        results (list['PricingSearchRecord']): Flat list of matched listings, ranked by title relevance. Spans multiple
            cards and may include unmatched listings.
        meta (SearchMeta):
    """

    query: "PricingSearchQueryEcho"
    results: list["PricingSearchRecord"]
    meta: "SearchMeta"

    def to_dict(self) -> dict[str, Any]:
        query = self.query.to_dict()

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

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
        from ..models.pricing_search_query_echo import PricingSearchQueryEcho
        from ..models.pricing_search_record import PricingSearchRecord
        from ..models.search_meta import SearchMeta

        d = dict(src_dict)
        query = PricingSearchQueryEcho.from_dict(d.pop("query"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PricingSearchRecord.from_dict(results_item_data)

            results.append(results_item)

        meta = SearchMeta.from_dict(d.pop("meta"))

        pricing_search_response = cls(
            query=query,
            results=results,
            meta=meta,
        )

        return pricing_search_response
