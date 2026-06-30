from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_set_context import CardSetContext


T = TypeVar("T", bound="SearchMatchedCard")


@_attrs_define
class SearchMatchedCard:
    """
    Attributes:
        card_id (UUID): Card UUID
        name (str): Card name/subject
        set_ (CardSetContext):
        number (Union[None, Unset, str]): Card number in set
    """

    card_id: UUID
    name: str
    set_: "CardSetContext"
    number: Union[None, Unset, str] = UNSET

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
        from ..models.card_set_context import CardSetContext

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        name = d.pop("name")

        set_ = CardSetContext.from_dict(d.pop("set"))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        search_matched_card = cls(
            card_id=card_id,
            name=name,
            set_=set_,
            number=number,
        )

        return search_matched_card
