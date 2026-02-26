from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parallel_summary_input import ParallelSummaryInput


T = TypeVar("T", bound="DetailedSetResponseInput")


@_attrs_define
class DetailedSetResponseInput:
    """
    Attributes:
        id (str): Unique identifier for the set. Format: UUID v4. This ID is permanent and used for all API operations
            involving this set.
        release_id (str): UUID of the release this set belongs to. Links to the release entity. A release typically
            contains multiple sets.
        name (str): Name of the set within the release. Examples: "Base Set", "Rookie Autographs", "Legends". Describes
            the theme or type of cards in this set.
        is_identifiable (bool): Whether cards in this set can be identified by the CardSightAI identification service.
        release_name (str): Name of the release
        release_year (str): Year of the release
        card_count (float): Number of base cards
        parallel_count (float): Number of parallel types
        parallels (list['ParallelSummaryInput']): List of parallel variants in this set
        description (Union[Unset, str]): Additional details about the set, such as card count, special features, or
            checklist highlights. May be null.
    """

    id: str
    release_id: str
    name: str
    is_identifiable: bool
    release_name: str
    release_year: str
    card_count: float
    parallel_count: float
    parallels: list["ParallelSummaryInput"]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        release_id = self.release_id

        name = self.name

        is_identifiable = self.is_identifiable

        release_name = self.release_name

        release_year = self.release_year

        card_count = self.card_count

        parallel_count = self.parallel_count

        parallels = []
        for parallels_item_data in self.parallels:
            parallels_item = parallels_item_data.to_dict()
            parallels.append(parallels_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "releaseId": release_id,
                "name": name,
                "is_identifiable": is_identifiable,
                "releaseName": release_name,
                "releaseYear": release_year,
                "cardCount": card_count,
                "parallelCount": parallel_count,
                "parallels": parallels,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parallel_summary_input import ParallelSummaryInput

        d = dict(src_dict)
        id = d.pop("id")

        release_id = d.pop("releaseId")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        card_count = d.pop("cardCount")

        parallel_count = d.pop("parallelCount")

        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = ParallelSummaryInput.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        description = d.pop("description", UNSET)

        detailed_set_response_input = cls(
            id=id,
            release_id=release_id,
            name=name,
            is_identifiable=is_identifiable,
            release_name=release_name,
            release_year=release_year,
            card_count=card_count,
            parallel_count=parallel_count,
            parallels=parallels,
            description=description,
        )

        detailed_set_response_input.additional_properties = d
        return detailed_set_response_input

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
