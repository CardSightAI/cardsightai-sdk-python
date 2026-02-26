from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DetailedParallelResponse")


@_attrs_define
class DetailedParallelResponse:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange".
        is_partial (bool): True if this parallel applies to specific cards only (e.g., cards 1-400 of a 800-card set).
            False if it applies to the entire set.
        set_id (str): UUID of the set this parallel belongs to.
        set_name (str): Name of the set this parallel belongs to.
        release_id (str): UUID of the release containing this parallel's set.
        release_name (str): Name of the release (e.g., "2023 Topps Chrome Baseball").
        release_year (str): Year the release was issued (e.g., "2023").
        description (Union[Unset, str]): Additional details about the parallel such as special features or visual
            description. May be null.
        numbered_to (Union[Unset, float]): Limited print run number. Example: 50 means /50 parallel. Null for unlimited
            parallels.
        cards (Union[Unset, list[str]]): Array of card UUIDs that have this parallel variant. Only present when
            isPartial=true. Empty array if partial but no cards mapped.
    """

    id: str
    name: str
    is_partial: bool
    set_id: str
    set_name: str
    release_id: str
    release_name: str
    release_year: str
    description: Union[Unset, str] = UNSET
    numbered_to: Union[Unset, float] = UNSET
    cards: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_partial = self.is_partial

        set_id = self.set_id

        set_name = self.set_name

        release_id = self.release_id

        release_name = self.release_name

        release_year = self.release_year

        description = self.description

        numbered_to = self.numbered_to

        cards: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "isPartial": is_partial,
                "setId": set_id,
                "setName": set_name,
                "releaseId": release_id,
                "releaseName": release_name,
                "releaseYear": release_year,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_partial = d.pop("isPartial")

        set_id = d.pop("setId")

        set_name = d.pop("setName")

        release_id = d.pop("releaseId")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        description = d.pop("description", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        cards = cast(list[str], d.pop("cards", UNSET))

        detailed_parallel_response = cls(
            id=id,
            name=name,
            is_partial=is_partial,
            set_id=set_id,
            set_name=set_name,
            release_id=release_id,
            release_name=release_name,
            release_year=release_year,
            description=description,
            numbered_to=numbered_to,
            cards=cards,
        )

        return detailed_parallel_response
