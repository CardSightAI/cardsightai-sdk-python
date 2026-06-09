from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ParallelSetProgress")


@_attrs_define
class ParallelSetProgress:
    """
    Attributes:
        set_id (str): Set UUID
        set_name (str): Set name
        release_name (str): Release name
        release_year (str): Release year
        parallel_id (str): Parallel UUID
        parallel_name (str): Parallel name (e.g., Refractor, Gold)
        total_cards (float): Total number of cards in set
        owned_cards (float): Number of this parallel owned
        missing_cards (list[str]): Array of missing card UUIDs for this parallel
        completion_percentage (float): Percentage complete for this parallel (0-100)
    """

    set_id: str
    set_name: str
    release_name: str
    release_year: str
    parallel_id: str
    parallel_name: str
    total_cards: float
    owned_cards: float
    missing_cards: list[str]
    completion_percentage: float

    def to_dict(self) -> dict[str, Any]:
        set_id = self.set_id

        set_name = self.set_name

        release_name = self.release_name

        release_year = self.release_year

        parallel_id = self.parallel_id

        parallel_name = self.parallel_name

        total_cards = self.total_cards

        owned_cards = self.owned_cards

        missing_cards = self.missing_cards

        completion_percentage = self.completion_percentage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "setId": set_id,
                "setName": set_name,
                "releaseName": release_name,
                "releaseYear": release_year,
                "parallelId": parallel_id,
                "parallelName": parallel_name,
                "totalCards": total_cards,
                "ownedCards": owned_cards,
                "missingCards": missing_cards,
                "completionPercentage": completion_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_id = d.pop("setId")

        set_name = d.pop("setName")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        parallel_id = d.pop("parallelId")

        parallel_name = d.pop("parallelName")

        total_cards = d.pop("totalCards")

        owned_cards = d.pop("ownedCards")

        missing_cards = cast(list[str], d.pop("missingCards"))

        completion_percentage = d.pop("completionPercentage")

        parallel_set_progress = cls(
            set_id=set_id,
            set_name=set_name,
            release_name=release_name,
            release_year=release_year,
            parallel_id=parallel_id,
            parallel_name=parallel_name,
            total_cards=total_cards,
            owned_cards=owned_cards,
            missing_cards=missing_cards,
            completion_percentage=completion_percentage,
        )

        return parallel_set_progress
