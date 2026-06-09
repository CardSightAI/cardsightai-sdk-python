from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pricing_card_context_parallel_type_0 import PricingCardContextParallelType0
    from ..models.pricing_card_context_set import PricingCardContextSet


T = TypeVar("T", bound="PricingCardContext")


@_attrs_define
class PricingCardContext:
    """
    Attributes:
        card_id (UUID): Card UUID
        name (str): Card name/subject
        set_ (PricingCardContextSet): Set context
        number (Union[None, Unset, str]): Card number in set
        parallel (Union['PricingCardContextParallelType0', None, Unset]): Parallel context if filtered by parallel
    """

    card_id: UUID
    name: str
    set_: "PricingCardContextSet"
    number: Union[None, Unset, str] = UNSET
    parallel: Union["PricingCardContextParallelType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_card_context_parallel_type_0 import PricingCardContextParallelType0

        card_id = str(self.card_id)

        name = self.name

        set_ = self.set_.to_dict()

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        parallel: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parallel, Unset):
            parallel = UNSET
        elif isinstance(self.parallel, PricingCardContextParallelType0):
            parallel = self.parallel.to_dict()
        else:
            parallel = self.parallel

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
        if parallel is not UNSET:
            field_dict["parallel"] = parallel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_card_context_parallel_type_0 import PricingCardContextParallelType0
        from ..models.pricing_card_context_set import PricingCardContextSet

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        name = d.pop("name")

        set_ = PricingCardContextSet.from_dict(d.pop("set"))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_parallel(data: object) -> Union["PricingCardContextParallelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parallel_type_0 = PricingCardContextParallelType0.from_dict(data)

                return parallel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PricingCardContextParallelType0", None, Unset], data)

        parallel = _parse_parallel(d.pop("parallel", UNSET))

        pricing_card_context = cls(
            card_id=card_id,
            name=name,
            set_=set_,
            number=number,
            parallel=parallel,
        )

        return pricing_card_context
