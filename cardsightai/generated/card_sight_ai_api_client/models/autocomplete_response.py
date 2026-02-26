from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AutocompleteResponse")


@_attrs_define
class AutocompleteResponse:
    """
    Attributes:
        suggestions (list[str]): List of autocomplete suggestions, maximum 10 items, sorted alphabetically
    """

    suggestions: list[str]

    def to_dict(self) -> dict[str, Any]:
        suggestions = self.suggestions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "suggestions": suggestions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggestions = cast(list[str], d.pop("suggestions"))

        autocomplete_response = cls(
            suggestions=suggestions,
        )

        return autocomplete_response
