from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Parallel")


@_attrs_define
class Parallel:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4. This ID represents the parallel variant, not
            individual cards.
        set_id (str): UUID of the set this parallel belongs to. Links to the set entity. Each set can have multiple
            parallel types.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange". Describes the
            visual variant or rarity tier.
        description (Union[Unset, str]): Additional details about the parallel such as print run, special features, or
            visual description. May be null.
        is_partial (Union[Unset, bool]): Present and true only if this parallel applies to specific cards (e.g., cards
            1-400 of a 800-card set). Omitted if parallel applies to the entire set.
    """

    id: str
    set_id: str
    name: str
    description: Union[Unset, str] = UNSET
    is_partial: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        set_id = self.set_id

        name = self.name

        description = self.description

        is_partial = self.is_partial

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "setId": set_id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_partial is not UNSET:
            field_dict["isPartial"] = is_partial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        set_id = d.pop("setId")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_partial = d.pop("isPartial", UNSET)

        parallel = cls(
            id=id,
            set_id=set_id,
            name=name,
            description=description,
            is_partial=is_partial,
        )

        return parallel
