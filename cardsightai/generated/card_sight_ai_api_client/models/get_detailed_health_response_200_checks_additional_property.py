from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.get_detailed_health_response_200_checks_additional_property_status import (
    GetDetailedHealthResponse200ChecksAdditionalPropertyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDetailedHealthResponse200ChecksAdditionalProperty")


@_attrs_define
class GetDetailedHealthResponse200ChecksAdditionalProperty:
    """
    Attributes:
        status (GetDetailedHealthResponse200ChecksAdditionalPropertyStatus): Health status of the component
        message (Union[Unset, str]): Optional message describing the health status
        response_time (Union[Unset, float]): Response time in milliseconds
    """

    status: GetDetailedHealthResponse200ChecksAdditionalPropertyStatus
    message: Union[Unset, str] = UNSET
    response_time: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        message = self.message

        response_time = self.response_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if response_time is not UNSET:
            field_dict["responseTime"] = response_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = GetDetailedHealthResponse200ChecksAdditionalPropertyStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        response_time = d.pop("responseTime", UNSET)

        get_detailed_health_response_200_checks_additional_property = cls(
            status=status,
            message=message,
            response_time=response_time,
        )

        return get_detailed_health_response_200_checks_additional_property
