from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pricing_card_context_input_parallel_type_0 import PricingCardContextInputParallelType0
    from ..models.pricing_card_context_input_set import PricingCardContextInputSet


T = TypeVar("T", bound="PricingCardContextInput")


@_attrs_define
class PricingCardContextInput:
    """
    Attributes:
        card_id (UUID): Card UUID
        name (str): Card name/subject
        set_ (PricingCardContextInputSet): Set context
        number (Union[None, Unset, str]): Card number in set
        parallel (Union['PricingCardContextInputParallelType0', None, Unset]): Parallel context if filtered by parallel
    """

    card_id: UUID
    name: str
    set_: "PricingCardContextInputSet"
    number: Union[None, Unset, str] = UNSET
    parallel: Union["PricingCardContextInputParallelType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_card_context_input_parallel_type_0 import PricingCardContextInputParallelType0

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
        elif isinstance(self.parallel, PricingCardContextInputParallelType0):
            parallel = self.parallel.to_dict()
        else:
            parallel = self.parallel

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
        if parallel is not UNSET:
            field_dict["parallel"] = parallel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_card_context_input_parallel_type_0 import PricingCardContextInputParallelType0
        from ..models.pricing_card_context_input_set import PricingCardContextInputSet

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        name = d.pop("name")

        set_ = PricingCardContextInputSet.from_dict(d.pop("set"))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_parallel(data: object) -> Union["PricingCardContextInputParallelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parallel_type_0 = PricingCardContextInputParallelType0.from_dict(data)

                return parallel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PricingCardContextInputParallelType0", None, Unset], data)

        parallel = _parse_parallel(d.pop("parallel", UNSET))

        pricing_card_context_input = cls(
            card_id=card_id,
            name=name,
            set_=set_,
            number=number,
            parallel=parallel,
        )

        pricing_card_context_input.additional_properties = d
        return pricing_card_context_input

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
