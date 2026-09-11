from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value import FieldValue


T = TypeVar("T", bound="CardSuggestion")


@_attrs_define
class CardSuggestion:
    """
    Attributes:
        id (Union[Unset, str]): UUID of the card. Present only for exact card matches.
        segment_id (Union[Unset, str]): UUID of the segment. Present for both exact card and set-level matches.
        release_id (Union[Unset, str]): UUID of the release. Present for both exact card and set-level matches.
        set_id (Union[Unset, str]): UUID of the set. Present for both exact card and set-level matches.
        year (Union[Unset, str]): Release year from catalog (e.g., "2023", "1989")
        manufacturer (Union[Unset, str]): Card manufacturer from catalog (e.g., "Topps", "Panini", "Upper Deck")
        release_name (Union[Unset, str]): Release/product name from catalog (e.g., "Topps Chrome", "Prizm Basketball")
        set_name (Union[Unset, str]): Set name from catalog (e.g., "Base Set", "Rookie Variations")
        name (Union[Unset, str]): Player or subject name. Present only for exact card matches.
        number (Union[Unset, str]): Card number. Present only for exact card matches.
        description (Union[Unset, str]): Descriptive text for the card when available. Omitted if no description exists.
        numbered_to (Union[Unset, int]): Print run for numbered cards (e.g., 25 for a /25 card). Omitted if the card is
            not numbered.
        attributes (Union[Unset, list[str]]): Notable attributes of the card (e.g., ["Rookie", "Autograph"]). Omitted if
            the card has no attributes.
        variation_of (Union[Unset, str]): UUID of the parent card when this card is a variation. Omitted if the card is
            not a variation.
        fields (Union[Unset, list['FieldValue']]):
    """

    id: Union[Unset, str] = UNSET
    segment_id: Union[Unset, str] = UNSET
    release_id: Union[Unset, str] = UNSET
    set_id: Union[Unset, str] = UNSET
    year: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    release_name: Union[Unset, str] = UNSET
    set_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    numbered_to: Union[Unset, int] = UNSET
    attributes: Union[Unset, list[str]] = UNSET
    variation_of: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValue"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        release_id = self.release_id

        set_id = self.set_id

        year = self.year

        manufacturer = self.manufacturer

        release_name = self.release_name

        set_name = self.set_name

        name = self.name

        number = self.number

        description = self.description

        numbered_to = self.numbered_to

        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        variation_of = self.variation_of

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for componentsschemas_field_values_item_data in self.fields:
                componentsschemas_field_values_item = componentsschemas_field_values_item_data.to_dict()
                fields.append(componentsschemas_field_values_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if set_id is not UNSET:
            field_dict["setId"] = set_id
        if year is not UNSET:
            field_dict["year"] = year
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if set_name is not UNSET:
            field_dict["setName"] = set_name
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.field_value import FieldValue

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        segment_id = d.pop("segmentId", UNSET)

        release_id = d.pop("releaseId", UNSET)

        set_id = d.pop("setId", UNSET)

        year = d.pop("year", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        release_name = d.pop("releaseName", UNSET)

        set_name = d.pop("setName", UNSET)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        description = d.pop("description", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        attributes = cast(list[str], d.pop("attributes", UNSET))

        variation_of = d.pop("variationOf", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_item_data in _fields or []:
            componentsschemas_field_values_item = FieldValue.from_dict(componentsschemas_field_values_item_data)

            fields.append(componentsschemas_field_values_item)

        card_suggestion = cls(
            id=id,
            segment_id=segment_id,
            release_id=release_id,
            set_id=set_id,
            year=year,
            manufacturer=manufacturer,
            release_name=release_name,
            set_name=set_name,
            name=name,
            number=number,
            description=description,
            numbered_to=numbered_to,
            attributes=attributes,
            variation_of=variation_of,
            fields=fields,
        )

        return card_suggestion
