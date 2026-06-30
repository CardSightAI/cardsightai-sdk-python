from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.marketplace_search_query_echo import MarketplaceSearchQueryEcho
    from ..models.marketplace_search_record import MarketplaceSearchRecord
    from ..models.search_meta import SearchMeta


T = TypeVar("T", bound="MarketplaceSearchResponse")


@_attrs_define
class MarketplaceSearchResponse:
    """
    Attributes:
        query (MarketplaceSearchQueryEcho):
        results (list['MarketplaceSearchRecord']): Flat list of matched active listings, ranked by title relevance.
            Spans multiple cards and may include unmatched listings.
        meta (SearchMeta):
    """

    query: "MarketplaceSearchQueryEcho"
    results: list["MarketplaceSearchRecord"]
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
        from ..models.marketplace_search_query_echo import MarketplaceSearchQueryEcho
        from ..models.marketplace_search_record import MarketplaceSearchRecord
        from ..models.search_meta import SearchMeta

        d = dict(src_dict)
        query = MarketplaceSearchQueryEcho.from_dict(d.pop("query"))

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = MarketplaceSearchRecord.from_dict(results_item_data)

            results.append(results_item)

        meta = SearchMeta.from_dict(d.pop("meta"))

        marketplace_search_response = cls(
            query=query,
            results=results,
            meta=meta,
        )

        return marketplace_search_response
