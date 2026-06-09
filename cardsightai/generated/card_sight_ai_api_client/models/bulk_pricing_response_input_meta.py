from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkPricingResponseInputMeta")


@_attrs_define
class BulkPricingResponseInputMeta:
    """Summary counts

    Attributes:
        requested (int): Number of cards requested
        successful (int): Number of cards with successful results
        failed (int): Number of cards that failed
    """

    requested: int
    successful: int
    failed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        successful = self.successful

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        bulk_pricing_response_input_meta = cls(
            requested=requested,
            successful=successful,
            failed=failed,
        )

        bulk_pricing_response_input_meta.additional_properties = d
        return bulk_pricing_response_input_meta

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
