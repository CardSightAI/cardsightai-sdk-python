from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_result_input import SearchResultInput
    from ..models.server_message_input import ServerMessageInput


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
        messages (Union[Unset, list['ServerMessageInput']]): Optional server advisory messages, e.g. a warning that an
            unrecognized query parameter was ignored. Omitted when there are none.
    """

    results: list["SearchResultInput"]
    total_count: float
    skip: float
    take: float
    messages: Union[Unset, list["ServerMessageInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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
        from ..models.search_result_input import SearchResultInput
        from ..models.server_message_input import ServerMessageInput

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResultInput.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ServerMessageInput.from_dict(messages_item_data)

            messages.append(messages_item)

        catalog_search_response_input = cls(
            results=results,
            total_count=total_count,
            skip=skip,
            take=take,
            messages=messages,
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
