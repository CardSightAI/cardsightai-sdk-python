from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

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
        estimated_cost_to_complete (Union[Unset, str]): Estimated cost to acquire missing cards of this parallel
        average_card_value (Union[Unset, str]): Average value per card for this parallel
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
    estimated_cost_to_complete: Union[Unset, str] = UNSET
    average_card_value: Union[Unset, str] = UNSET

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

        estimated_cost_to_complete = self.estimated_cost_to_complete

        average_card_value = self.average_card_value

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
        if estimated_cost_to_complete is not UNSET:
            field_dict["estimatedCostToComplete"] = estimated_cost_to_complete
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

        parallel_id = d.pop("parallelId")

        parallel_name = d.pop("parallelName")

        total_cards = d.pop("totalCards")

        owned_cards = d.pop("ownedCards")

        missing_cards = cast(list[str], d.pop("missingCards"))

        completion_percentage = d.pop("completionPercentage")

        estimated_cost_to_complete = d.pop("estimatedCostToComplete", UNSET)

        average_card_value = d.pop("averageCardValue", UNSET)

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
            estimated_cost_to_complete=estimated_cost_to_complete,
            average_card_value=average_card_value,
        )

        return parallel_set_progress
