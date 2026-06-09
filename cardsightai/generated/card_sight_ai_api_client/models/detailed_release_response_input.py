from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value_input import FieldValueInput
    from ..models.set_summary_with_counts_input import SetSummaryWithCountsInput


T = TypeVar("T", bound="DetailedReleaseResponseInput")


@_attrs_define
class DetailedReleaseResponseInput:
    """
    Attributes:
        id (str): Unique identifier for the release. Format: UUID v4. This ID is permanent and used for all API
            operations involving this release.
        segment_id (str): UUID of the segment this release belongs to. Links to the segment entity. Determines the
            market category (Sports, Entertainment, etc.).
        manufacturer_id (str): UUID of the manufacturer that produced this release. Links to the manufacturer entity.
        year (str): Year the release was issued. Format: YYYY (e.g., "2023"). Used for chronological filtering and
            sorting.
        name (str): Full name of the release. Typically includes year, brand, and sport/category. Example: "2023 Topps
            Chrome Baseball"
        is_identifiable (bool): Whether any set in this release can be identified by the CardSightAI identification
            service. True if at least one set has is_identifiable = true.
        sets (list['SetSummaryWithCountsInput']): Sets within this release
        description (Union[Unset, str]): Additional details about the release, such as special features, number of
            cards, or notable inclusions. May be null.
        fields (Union[Unset, list['FieldValueInput']]):
    """

    id: str
    segment_id: str
    manufacturer_id: str
    year: str
    name: str
    is_identifiable: bool
    sets: list["SetSummaryWithCountsInput"]
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValueInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        manufacturer_id = self.manufacturer_id

        year = self.year

        name = self.name

        is_identifiable = self.is_identifiable

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        description = self.description

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
                "id": id,
                "segmentId": segment_id,
                "manufacturerId": manufacturer_id,
                "year": year,
                "name": name,
                "is_identifiable": is_identifiable,
                "sets": sets,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_value_input import FieldValueInput
        from ..models.set_summary_with_counts_input import SetSummaryWithCountsInput

        d = dict(src_dict)
        id = d.pop("id")

        segment_id = d.pop("segmentId")

        manufacturer_id = d.pop("manufacturerId")

        year = d.pop("year")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = SetSummaryWithCountsInput.from_dict(sets_item_data)

            sets.append(sets_item)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_input_item_data in _fields or []:
            componentsschemas_field_values_input_item = FieldValueInput.from_dict(
                componentsschemas_field_values_input_item_data
            )

            fields.append(componentsschemas_field_values_input_item)

        detailed_release_response_input = cls(
            id=id,
            segment_id=segment_id,
            manufacturer_id=manufacturer_id,
            year=year,
            name=name,
            is_identifiable=is_identifiable,
            sets=sets,
            description=description,
            fields=fields,
        )

        detailed_release_response_input.additional_properties = d
        return detailed_release_response_input

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
