from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="PricingCardContextParallelType0")


@_attrs_define
class PricingCardContextParallelType0:
    """
    Attributes:
        parallel_id (UUID): Parallel UUID
        name (str): Parallel name
    """

    parallel_id: UUID
    name: str

    def to_dict(self) -> dict[str, Any]:
        parallel_id = str(self.parallel_id)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "parallel_id": parallel_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parallel_id = UUID(d.pop("parallel_id"))

        name = d.pop("name")

        pricing_card_context_parallel_type_0 = cls(
            parallel_id=parallel_id,
            name=name,
        )

        return pricing_card_context_parallel_type_0
