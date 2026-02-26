from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginatedSetsResponseSetsItem")


@_attrs_define
class PaginatedSetsResponseSetsItem:
    """
    Attributes:
        id (str): Unique identifier for the set. Format: UUID v4. This ID is permanent and used for all API operations
            involving this set.
        name (str): Name of the set within the release. Examples: "Base Set", "Rookie Autographs", "Legends". Describes
            the theme or type of cards in this set.
        is_identifiable (bool): Whether cards in this set can be identified by the CardSightAI identification service.
        card_count (float): Number of base cards in this set
        parallel_count (float): Number of parallel types in this set
        release_id (str): Release UUID
        release_name (str): Release name
        release_year (str): Release year
        description (Union[Unset, str]): Additional details about the set, such as card count, special features, or
            checklist highlights. May be null.
    """

    id: str
    name: str
    is_identifiable: bool
    card_count: float
    parallel_count: float
    release_id: str
    release_name: str
    release_year: str
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_identifiable = self.is_identifiable

        card_count = self.card_count

        parallel_count = self.parallel_count

        release_id = self.release_id

        release_name = self.release_name

        release_year = self.release_year

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_identifiable": is_identifiable,
                "cardCount": card_count,
                "parallelCount": parallel_count,
                "releaseId": release_id,
                "releaseName": release_name,
                "releaseYear": release_year,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        card_count = d.pop("cardCount")

        parallel_count = d.pop("parallelCount")

        release_id = d.pop("releaseId")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        description = d.pop("description", UNSET)

        paginated_sets_response_sets_item = cls(
            id=id,
            name=name,
            is_identifiable=is_identifiable,
            card_count=card_count,
            parallel_count=parallel_count,
            release_id=release_id,
            release_name=release_name,
            release_year=release_year,
            description=description,
        )

        return paginated_sets_response_sets_item
