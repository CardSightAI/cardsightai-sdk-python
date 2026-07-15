from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result import SearchResult
    from ..models.server_message import ServerMessage


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
        messages (Union[Unset, list['ServerMessage']]): Optional server advisory messages, e.g. a warning that an
            unrecognized query parameter was ignored. Omitted when there are none.
    """

    results: list["SearchResult"]
    total_count: float
    skip: float
    take: float
    messages: Union[Unset, list["ServerMessage"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "results": results,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_result import SearchResult
        from ..models.server_message import ServerMessage

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResult.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ServerMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        catalog_search_response = cls(
            results=results,
            total_count=total_count,
            skip=skip,
            take=take,
            messages=messages,
        )

        return catalog_search_response
