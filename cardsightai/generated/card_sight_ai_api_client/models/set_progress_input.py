from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetProgressInput")


@_attrs_define
class SetProgressInput:
    """
    Attributes:
        set_id (str): Set UUID
        set_name (str): Set name
        release_name (str): Release name
        release_year (str): Release year
        total_cards (float): Total number of cards in set
        owned_cards (float): Number of unique cards owned
        missing_cards (list[str]): Array of missing card UUIDs
        completion_percentage (float): Percentage complete (0-100)
        estimated_cost_to_complete (Union[Unset, str]): Estimated cost to acquire missing cards
        difficulty_score (Union[Unset, float]): Difficulty score based on card availability (0-100)
        average_card_value (Union[Unset, str]): Average value per card in set
    """

    set_id: str
    set_name: str
    release_name: str
    release_year: str
    total_cards: float
    owned_cards: float
    missing_cards: list[str]
    completion_percentage: float
    estimated_cost_to_complete: Union[Unset, str] = UNSET
    difficulty_score: Union[Unset, float] = UNSET
    average_card_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        release_name = self.release_name

        release_year = self.release_year

        total_cards = self.total_cards

        owned_cards = self.owned_cards

        missing_cards = self.missing_cards

        completion_percentage = self.completion_percentage

        estimated_cost_to_complete = self.estimated_cost_to_complete

        difficulty_score = self.difficulty_score

        average_card_value = self.average_card_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "setId": set_id,
                "setName": set_name,
                "releaseName": release_name,
                "releaseYear": release_year,
                "totalCards": total_cards,
                "ownedCards": owned_cards,
                "missingCards": missing_cards,
                "completionPercentage": completion_percentage,
            }
        )
        if estimated_cost_to_complete is not UNSET:
            field_dict["estimatedCostToComplete"] = estimated_cost_to_complete
        if difficulty_score is not UNSET:
            field_dict["difficultyScore"] = difficulty_score
        if average_card_value is not UNSET:
            field_dict["averageCardValue"] = average_card_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_id = d.pop("setId")

        set_name = d.pop("setName")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        total_cards = d.pop("totalCards")

        owned_cards = d.pop("ownedCards")

        missing_cards = cast(list[str], d.pop("missingCards"))

        completion_percentage = d.pop("completionPercentage")

        estimated_cost_to_complete = d.pop("estimatedCostToComplete", UNSET)

        difficulty_score = d.pop("difficultyScore", UNSET)

        average_card_value = d.pop("averageCardValue", UNSET)

        set_progress_input = cls(
            set_id=set_id,
            set_name=set_name,
            release_name=release_name,
            release_year=release_year,
            total_cards=total_cards,
            owned_cards=owned_cards,
            missing_cards=missing_cards,
            completion_percentage=completion_percentage,
            estimated_cost_to_complete=estimated_cost_to_complete,
            difficulty_score=difficulty_score,
            average_card_value=average_card_value,
        )

        set_progress_input.additional_properties = d
        return set_progress_input

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
