from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BulkPricingResultError")


@_attrs_define
class BulkPricingResultError:
    """Error details when unsuccessful

    Attributes:
        code (str): Error code
        message (str): Error message
    """

    code: str
    message: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        bulk_pricing_result_error = cls(
            code=code,
            message=message,
        )

        return bulk_pricing_result_error
