from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BatchOperationErrorInput")


@_attrs_define
class BatchOperationErrorInput:
    """
    Attributes:
        index (float): Index of the failed item in the request array
        card_id (str): Card UUID that failed to process
        error (str): Error message describing why the operation failed
    """

    index: float
    card_id: str
    error: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        card_id = self.card_id

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "cardId": card_id,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        card_id = d.pop("cardId")

        error = d.pop("error")

        batch_operation_error_input = cls(
            index=index,
            card_id=card_id,
            error=error,
        )

        batch_operation_error_input.additional_properties = d
        return batch_operation_error_input

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
