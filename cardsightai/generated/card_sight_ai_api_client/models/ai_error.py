from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIError")


@_attrs_define
class AIError:
    """
    Attributes:
        error (str):
        code (str):
        details (Union[Unset, Any]):
    """

    error: str
    code: str
    details: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        code = self.code

        details = self.details

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
                "code": code,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        code = d.pop("code")

        details = d.pop("details", UNSET)

        ai_error = cls(
            error=error,
            code=code,
            details=details,
        )

        return ai_error
