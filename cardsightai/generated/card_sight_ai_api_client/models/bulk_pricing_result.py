from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_pricing_result_error import BulkPricingResultError
    from ..models.pricing_response import PricingResponse


T = TypeVar("T", bound="BulkPricingResult")


@_attrs_define
class BulkPricingResult:
    """
    Attributes:
        card_id (UUID): Card UUID
        success (bool): Whether pricing was successfully retrieved
        data (Union[Unset, PricingResponse]):
        error (Union[Unset, BulkPricingResultError]): Error details when unsuccessful
    """

    card_id: UUID
    success: bool
    data: Union[Unset, "PricingResponse"] = UNSET
    error: Union[Unset, "BulkPricingResultError"] = UNSET

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
        from ..models.bulk_pricing_result_error import BulkPricingResultError
        from ..models.pricing_response import PricingResponse

        d = dict(src_dict)
        card_id = UUID(d.pop("card_id"))

        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, PricingResponse]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PricingResponse.from_dict(_data)

        _error = d.pop("error", UNSET)
        error: Union[Unset, BulkPricingResultError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = BulkPricingResultError.from_dict(_error)

        bulk_pricing_result = cls(
            card_id=card_id,
            success=success,
            data=data,
            error=error,
        )

        return bulk_pricing_result
