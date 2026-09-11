from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parallel_suggestion_input_confidence import ParallelSuggestionInputConfidence
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParallelSuggestionInput")


@_attrs_define
class ParallelSuggestionInput:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4. This ID represents the parallel variant, not
            individual cards.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange". Describes the
            visual variant or rarity tier.
        description (Union[Unset, str]): Additional details about the parallel such as print run, special features, or
            visual description. May be null.
        is_partial (Union[Unset, bool]): Present and true only if this parallel applies to specific cards (e.g., cards
            1-400 of a 800-card set). Omitted if parallel applies to the entire set.
        numbered_to (Union[Unset, float]): Limited print run number for this parallel
        cards (Union[Unset, list[str]]): Card UUIDs that have this parallel. Only present when isPartial is true.
        confidence (Union[Unset, ParallelSuggestionInputConfidence]): How strongly this parallel is supported for the
            scanned card. Assessed per entry, independent of the entry's position in the list. Present when available while
            this field is in beta; a missing value means not assessed, not Low.
    """

    id: str
    name: str
    description: Union[Unset, str] = UNSET
    is_partial: Union[Unset, bool] = UNSET
    numbered_to: Union[Unset, float] = UNSET
    cards: Union[Unset, list[str]] = UNSET
    confidence: Union[Unset, ParallelSuggestionInputConfidence] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_partial = self.is_partial

        numbered_to = self.numbered_to

        cards: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        confidence: Union[Unset, str] = UNSET
        if not isinstance(self.confidence, Unset):
            confidence = self.confidence.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_partial is not UNSET:
            field_dict["isPartial"] = is_partial
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to
        if cards is not UNSET:
            field_dict["cards"] = cards
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_partial = d.pop("isPartial", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        cards = cast(list[str], d.pop("cards", UNSET))

        _confidence = d.pop("confidence", UNSET)
        confidence: Union[Unset, ParallelSuggestionInputConfidence]
        if isinstance(_confidence, Unset):
            confidence = UNSET
        else:
            confidence = ParallelSuggestionInputConfidence(_confidence)

        parallel_suggestion_input = cls(
            id=id,
            name=name,
            description=description,
            is_partial=is_partial,
            numbered_to=numbered_to,
            cards=cards,
            confidence=confidence,
        )

        parallel_suggestion_input.additional_properties = d
        return parallel_suggestion_input

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
