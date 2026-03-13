from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_result_input import SearchResultInput


T = TypeVar("T", bound="CatalogSearchResponseInput")


@_attrs_define
class CatalogSearchResponseInput:
    """
    Attributes:
        results (list['SearchResultInput']): Array of search results ordered by relevance score (descending). Contains a
            mix of cards, sets, and releases unless filtered by type.
        total_count (float): Total number of results matching the query across all included types.
        skip (float): Number of results skipped (offset) for pagination.
        take (float): Number of results included in this page.
    """

    results: list["SearchResultInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.search_result_input import SearchResultInput

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResultInput.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        catalog_search_response_input = cls(
            results=results,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        catalog_search_response_input.additional_properties = d
        return catalog_search_response_input

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
