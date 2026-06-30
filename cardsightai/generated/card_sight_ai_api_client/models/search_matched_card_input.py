from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_set_context_input import CardSetContextInput


T = TypeVar("T", bound="SearchMatchedCardInput")


@_attrs_define
class SearchMatchedCardInput:
    """
    Attributes:
        card_id (UUID): Card UUID
        name (str): Card name/subject
        set_ (CardSetContextInput):
        number (Union[None, Unset, str]): Card number in set
    """

    card_id: UUID
    name: str
    set_: "CardSetContextInput"
    number: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = str(self.card_id)

        name = self.name

        set_ = self.set_.to_dict()

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card_id": card_id,
                "name": name,
                "set": set_,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_set_context_input import CardSetContextInput

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        name = d.pop("name")

        set_ = CardSetContextInput.from_dict(d.pop("set"))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        search_matched_card_input = cls(
            card_id=card_id,
            name=name,
            set_=set_,
            number=number,
        )

        search_matched_card_input.additional_properties = d
        return search_matched_card_input

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
