from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        error (str): Error message
        code (str): Error code for programmatic handling
    """

    error: str
    code: str

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        code = d.pop("code")

        error_response = cls(
            error=error,
            code=code,
        )

        return error_response
