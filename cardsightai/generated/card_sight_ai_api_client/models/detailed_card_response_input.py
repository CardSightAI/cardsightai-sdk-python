from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value_input import FieldValueInput
    from ..models.parallel_summary_input import ParallelSummaryInput


T = TypeVar("T", bound="DetailedCardResponseInput")


@_attrs_define
class DetailedCardResponseInput:
    """
    Attributes:
        release_id (str): UUID of the release this card belongs to. Provided for convenience to avoid additional
            lookups.
        set_id (str): UUID of the set this card belongs to. Links to the set entity. Determines which collection within
            the release contains this card.
        id (str): Unique identifier for the card. Format: UUID v4. This ID is permanent and used for all API operations
            involving this card.
        name (str): Primary subject of the card. Usually a player name for sports cards (e.g., "Michael Jordan") or
            character/subject for non-sports.
        set_name (str): Name of the set
        parallel_count (float): Number of parallel variants for this card
        parallels (list['ParallelSummaryInput']): List of parallel variants available for this card
        number (Union[Unset, str]): Card number within the set. Examples: "23", "RC-15", "L-5". May include letters for
            special subsets. Null for unnumbered cards.
        description (Union[Unset, str]): Additional card details such as team, position, special notations, or card back
            information. May be null.
        is_parallel_only (Union[Unset, bool]): Indicates this card exists only as a parallel, not as a base card. For
            example, if a set has 15 base cards but a parallel variant has 20 cards, the 5 extra cards would have
            isParallelOnly: true.
        release_name (Union[Unset, str]): Name of the release
        release_year (Union[Unset, str]): Year of the release
        numbered_to (Union[Unset, float]): Limited print run number for this specific card
        attributes (Union[Unset, list[str]]): Array of attribute short names
        variation_of (Union[Unset, str]): UUID of the base card if this is a variation. Only present for variation
            cards, omitted for base cards.
        fields (Union[Unset, list['FieldValueInput']]):
    """

    release_id: str
    set_id: str
    id: str
    name: str
    set_name: str
    parallel_count: float
    parallels: list["ParallelSummaryInput"]
    number: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_parallel_only: Union[Unset, bool] = UNSET
    release_name: Union[Unset, str] = UNSET
    release_year: Union[Unset, str] = UNSET
    numbered_to: Union[Unset, float] = UNSET
    attributes: Union[Unset, list[str]] = UNSET
    variation_of: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValueInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        set_id = self.set_id

        id = self.id

        name = self.name

        set_name = self.set_name

        parallel_count = self.parallel_count

        parallels = []
        for parallels_item_data in self.parallels:
            parallels_item = parallels_item_data.to_dict()
            parallels.append(parallels_item)

        number = self.number

        description = self.description

        is_parallel_only = self.is_parallel_only

        release_name = self.release_name

        release_year = self.release_year

        numbered_to = self.numbered_to

        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        variation_of = self.variation_of

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for componentsschemas_field_values_input_item_data in self.fields:
                componentsschemas_field_values_input_item = componentsschemas_field_values_input_item_data.to_dict()
                fields.append(componentsschemas_field_values_input_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "releaseId": release_id,
                "setId": set_id,
                "id": id,
                "name": name,
                "setName": set_name,
                "parallelCount": parallel_count,
                "parallels": parallels,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
        if is_parallel_only is not UNSET:
            field_dict["isParallelOnly"] = is_parallel_only
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if release_year is not UNSET:
            field_dict["releaseYear"] = release_year
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if variation_of is not UNSET:
            field_dict["variationOf"] = variation_of
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_value_input import FieldValueInput
        from ..models.parallel_summary_input import ParallelSummaryInput

        d = dict(src_dict)
        release_id = d.pop("releaseId")

        set_id = d.pop("setId")

        id = d.pop("id")

        name = d.pop("name")

        set_name = d.pop("setName")

        parallel_count = d.pop("parallelCount")

        parallels = []
        _parallels = d.pop("parallels")
        for parallels_item_data in _parallels:
            parallels_item = ParallelSummaryInput.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        number = d.pop("number", UNSET)

        description = d.pop("description", UNSET)

        is_parallel_only = d.pop("isParallelOnly", UNSET)

        release_name = d.pop("releaseName", UNSET)

        release_year = d.pop("releaseYear", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        attributes = cast(list[str], d.pop("attributes", UNSET))

        variation_of = d.pop("variationOf", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_input_item_data in _fields or []:
            componentsschemas_field_values_input_item = FieldValueInput.from_dict(
                componentsschemas_field_values_input_item_data
            )

            fields.append(componentsschemas_field_values_input_item)

        detailed_card_response_input = cls(
            release_id=release_id,
            set_id=set_id,
            id=id,
            name=name,
            set_name=set_name,
            parallel_count=parallel_count,
            parallels=parallels,
            number=number,
            description=description,
            is_parallel_only=is_parallel_only,
            release_name=release_name,
            release_year=release_year,
            numbered_to=numbered_to,
            attributes=attributes,
            variation_of=variation_of,
            fields=fields,
        )

        detailed_card_response_input.additional_properties = d
        return detailed_card_response_input

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
