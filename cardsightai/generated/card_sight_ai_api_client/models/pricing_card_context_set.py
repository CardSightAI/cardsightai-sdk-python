from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="PricingCardContextSet")


@_attrs_define
class PricingCardContextSet:
    """Set context

    Attributes:
        set_id (UUID): Set UUID
        name (str): Set name
        year (str): Release year
        release (str): Release name
    """

    set_id: UUID
    name: str
    year: str
    release: str

    def to_dict(self) -> dict[str, Any]:
        set_id = str(self.set_id)

        name = self.name

        year = self.year

        release = self.release

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "set_id": set_id,
                "name": name,
                "year": year,
                "release": release,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_id = UUID(d.pop("set_id"))

        name = d.pop("name")

        year = d.pop("year")

        release = d.pop("release")

        pricing_card_context_set = cls(
            set_id=set_id,
            name=name,
            year=year,
            release=release,
        )

        return pricing_card_context_set
