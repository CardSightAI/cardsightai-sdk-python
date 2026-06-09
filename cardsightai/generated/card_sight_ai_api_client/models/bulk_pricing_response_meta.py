from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BulkPricingResponseMeta")


@_attrs_define
class BulkPricingResponseMeta:
    """Summary counts

    Attributes:
        requested (int): Number of cards requested
        successful (int): Number of cards with successful results
        failed (int): Number of cards that failed
    """

    requested: int
    successful: int
    failed: int

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        successful = self.successful

        failed = self.failed

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requested": requested,
                "successful": successful,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requested = d.pop("requested")

        successful = d.pop("successful")

        failed = d.pop("failed")

        bulk_pricing_response_meta = cls(
            requested=requested,
            successful=successful,
            failed=failed,
        )

        return bulk_pricing_response_meta
