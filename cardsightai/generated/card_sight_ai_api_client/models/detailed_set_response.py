from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value import FieldValue
    from ..models.parallel_summary import ParallelSummary


T = TypeVar("T", bound="DetailedSetResponse")


@_attrs_define
class DetailedSetResponse:
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
        parallels (list['ParallelSummary']): List of parallel variants in this set
        description (Union[Unset, str]): Additional details about the set, such as card count, special features, or
            checklist highlights. May be null.
        fields (Union[Unset, list['FieldValue']]):
    """

    id: str
    release_id: str
    name: str
    is_identifiable: bool
    release_name: str
    release_year: str
    card_count: float
    parallel_count: float
    parallels: list["ParallelSummary"]
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValue"]] = UNSET

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

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for componentsschemas_field_values_item_data in self.fields:
                componentsschemas_field_values_item = componentsschemas_field_values_item_data.to_dict()
                fields.append(componentsschemas_field_values_item)

        field_dict: dict[str, Any] = {}

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
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_value import FieldValue
        from ..models.parallel_summary import ParallelSummary

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
            parallels_item = ParallelSummary.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_item_data in _fields or []:
            componentsschemas_field_values_item = FieldValue.from_dict(componentsschemas_field_values_item_data)

            fields.append(componentsschemas_field_values_item)

        detailed_set_response = cls(
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
            fields=fields,
        )

        return detailed_set_response
