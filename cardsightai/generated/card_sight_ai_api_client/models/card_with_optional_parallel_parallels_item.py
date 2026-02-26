from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardWithOptionalParallelParallelsItem")


@_attrs_define
class CardWithOptionalParallelParallelsItem:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4. This ID represents the parallel variant, not
            individual cards.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange". Describes the
            visual variant or rarity tier.
        numbered_to (Union[Unset, float]): Limited print run number for this parallel
    """

    id: str
    name: str
    numbered_to: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        numbered_to = self.numbered_to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        numbered_to = d.pop("numberedTo", UNSET)

        card_with_optional_parallel_parallels_item = cls(
            id=id,
            name=name,
            numbered_to=numbered_to,
        )

        return card_with_optional_parallel_parallels_item
