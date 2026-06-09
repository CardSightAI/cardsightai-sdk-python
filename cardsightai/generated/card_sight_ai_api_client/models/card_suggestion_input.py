from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value_input import FieldValueInput


T = TypeVar("T", bound="CardSuggestionInput")


@_attrs_define
class CardSuggestionInput:
    """
    Attributes:
        id (Union[Unset, str]): UUID of the suggested card
        set_name (Union[Unset, str]): Set name for the suggested card
        fields (Union[Unset, list['FieldValueInput']]):
    """

    id: Union[Unset, str] = UNSET
    set_name: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValueInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        set_name = self.set_name

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for componentsschemas_field_values_input_item_data in self.fields:
                componentsschemas_field_values_input_item = componentsschemas_field_values_input_item_data.to_dict()
                fields.append(componentsschemas_field_values_input_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if set_name is not UNSET:
            field_dict["setName"] = set_name
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_value_input import FieldValueInput

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        set_name = d.pop("setName", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_input_item_data in _fields or []:
            componentsschemas_field_values_input_item = FieldValueInput.from_dict(
                componentsschemas_field_values_input_item_data
            )

            fields.append(componentsschemas_field_values_input_item)

        card_suggestion_input = cls(
            id=id,
            set_name=set_name,
            fields=fields,
        )

        card_suggestion_input.additional_properties = d
        return card_suggestion_input

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
