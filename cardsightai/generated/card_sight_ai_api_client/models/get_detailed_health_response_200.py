from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_detailed_health_response_200_status import GetDetailedHealthResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_detailed_health_response_200_checks import GetDetailedHealthResponse200Checks


T = TypeVar("T", bound="GetDetailedHealthResponse200")


@_attrs_define
class GetDetailedHealthResponse200:
    """DetailedHealthResponse

    Attributes:
        status (GetDetailedHealthResponse200Status): Overall health status: healthy (all dependencies up), degraded
            (some non-critical dependencies down), unhealthy (critical dependencies down)
        timestamp (str): ISO 8601 timestamp when the health check was performed
        checks (Union[Unset, GetDetailedHealthResponse200Checks]): Health status of individual dependencies (database,
            Redis, etc.)
    """

    status: GetDetailedHealthResponse200Status
    timestamp: str
    checks: Union[Unset, "GetDetailedHealthResponse200Checks"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        timestamp = self.timestamp

        checks: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "timestamp": timestamp,
            }
        )
        if checks is not UNSET:
            field_dict["checks"] = checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_detailed_health_response_200_checks import GetDetailedHealthResponse200Checks

        d = dict(src_dict)
        status = GetDetailedHealthResponse200Status(d.pop("status"))

        timestamp = d.pop("timestamp")

        _checks = d.pop("checks", UNSET)
        checks: Union[Unset, GetDetailedHealthResponse200Checks]
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = GetDetailedHealthResponse200Checks.from_dict(_checks)

        get_detailed_health_response_200 = cls(
            status=status,
            timestamp=timestamp,
            checks=checks,
        )

        return get_detailed_health_response_200
