from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetProgress")


@_attrs_define
class SetProgress:
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
        difficulty_score (Union[Unset, float]): Difficulty score based on card availability (0-100)
    """

    set_id: str
    set_name: str
    release_name: str
    release_year: str
    total_cards: float
    owned_cards: float
    missing_cards: list[str]
    completion_percentage: float
    difficulty_score: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        release_name = self.release_name

        release_year = self.release_year

        total_cards = self.total_cards

        owned_cards = self.owned_cards

        missing_cards = self.missing_cards

        completion_percentage = self.completion_percentage

        difficulty_score = self.difficulty_score

        field_dict: dict[str, Any] = {}

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
        if difficulty_score is not UNSET:
            field_dict["difficultyScore"] = difficulty_score

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

        difficulty_score = d.pop("difficultyScore", UNSET)

        set_progress = cls(
            set_id=set_id,
            set_name=set_name,
            release_name=release_name,
            release_year=release_year,
            total_cards=total_cards,
            owned_cards=owned_cards,
            missing_cards=missing_cards,
            completion_percentage=completion_percentage,
            difficulty_score=difficulty_score,
        )

        return set_progress
