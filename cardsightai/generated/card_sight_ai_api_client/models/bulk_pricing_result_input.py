from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_pricing_result_input_error import BulkPricingResultInputError
    from ..models.pricing_response_input import PricingResponseInput


T = TypeVar("T", bound="BulkPricingResultInput")


@_attrs_define
class BulkPricingResultInput:
    """
    Attributes:
        card_id (UUID): Card UUID
        success (bool): Whether pricing was successfully retrieved
        data (Union[Unset, PricingResponseInput]):
        error (Union[Unset, BulkPricingResultInputError]): Error details when unsuccessful
    """

    card_id: UUID
    success: bool
    data: Union[Unset, "PricingResponseInput"] = UNSET
    error: Union[Unset, "BulkPricingResultInputError"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_id = str(self.card_id)

        success = self.success

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card_id": card_id,
                "success": success,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_pricing_result_input_error import BulkPricingResultInputError
        from ..models.pricing_response_input import PricingResponseInput

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, PricingResponseInput]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PricingResponseInput.from_dict(_data)

        _error = d.pop("error", UNSET)
        error: Union[Unset, BulkPricingResultInputError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = BulkPricingResultInputError.from_dict(_error)

        bulk_pricing_result_input = cls(
            card_id=card_id,
            success=success,
            data=data,
            error=error,
        )

        bulk_pricing_result_input.additional_properties = d
        return bulk_pricing_result_input

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
