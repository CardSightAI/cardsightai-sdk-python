from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_result import SearchResult


T = TypeVar("T", bound="CatalogSearchResponse")


@_attrs_define
class CatalogSearchResponse:
    """
    Attributes:
        results (list['SearchResult']): Array of search results ordered by relevance score (descending). Contains a mix
            of cards, sets, and releases unless filtered by type.
        total_count (float): Total number of results matching the query across all included types.
        skip (float): Number of results skipped (offset) for pagination.
        take (float): Number of results included in this page.
    """

    results: list["SearchResult"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "results": results,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result import SearchResult

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResult.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        catalog_search_response = cls(
            results=results,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return catalog_search_response
