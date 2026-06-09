from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value import FieldValue


T = TypeVar("T", bound="CardSuggestion")


@_attrs_define
class CardSuggestion:
    """
    Attributes:
        id (Union[Unset, str]): UUID of the suggested card
        set_name (Union[Unset, str]): Set name for the suggested card
        fields (Union[Unset, list['FieldValue']]):
    """

    id: Union[Unset, str] = UNSET
    set_name: Union[Unset, str] = UNSET
    fields: Union[Unset, list["FieldValue"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        set_name = self.set_name

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
        if set_name is not UNSET:
            field_dict["setName"] = set_name
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_value import FieldValue

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        set_name = d.pop("setName", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_item_data in _fields or []:
            componentsschemas_field_values_item = FieldValue.from_dict(componentsschemas_field_values_item_data)

            fields.append(componentsschemas_field_values_item)

        card_suggestion = cls(
            id=id,
            set_name=set_name,
            fields=fields,
        )

        return card_suggestion
