from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BatchOperationError")


@_attrs_define
class BatchOperationError:
    """
    Attributes:
        index (float): Index of the failed item in the request array
        card_id (str): Card UUID that failed to process
        error (str): Error message describing why the operation failed
    """

    index: float
    card_id: str
    error: str

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        card_id = self.card_id

        error = self.error

        field_dict: dict[str, Any] = {}

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

        batch_operation_error = cls(
            index=index,
            card_id=card_id,
            error=error,
        )

        return batch_operation_error
