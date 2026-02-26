from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BasicHealthResponse")


@_attrs_define
class BasicHealthResponse:
    """
    Attributes:
        status (str): Overall health status of the API (e.g., "healthy")
        timestamp (str): ISO 8601 timestamp when the health check was performed
    """

    status: str
    timestamp: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        timestamp = d.pop("timestamp")

        basic_health_response = cls(
            status=status,
            timestamp=timestamp,
        )

        return basic_health_response
