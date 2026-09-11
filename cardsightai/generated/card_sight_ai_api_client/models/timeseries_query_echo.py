from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeseriesQueryEcho")


@_attrs_define
class TimeseriesQueryEcho:
    """
    Attributes:
        interval (str): Rollup bucket size applied
        periods (int): Effective bucket count (the service applies per-interval defaults when omitted and clamps
            oversized values)
        as_of_date (str): Effective viewpoint date (UTC) the window ends on
        listing_type (str): Listing type filter applied
        parallel_id (Union[None, UUID, Unset]): Parallel UUID filter applied
        grade_id (Union[None, UUID, Unset]): Grade UUID filter applied
    """

    interval: str
    periods: int
    as_of_date: str
    listing_type: str
    parallel_id: Union[None, UUID, Unset] = UNSET
    grade_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        periods = self.periods

        as_of_date = self.as_of_date

        listing_type = self.listing_type

        parallel_id: Union[None, Unset, str]
        if isinstance(self.parallel_id, Unset):
            parallel_id = UNSET
        elif isinstance(self.parallel_id, UUID):
            parallel_id = str(self.parallel_id)
        else:
            parallel_id = self.parallel_id

        grade_id: Union[None, Unset, str]
        if isinstance(self.grade_id, Unset):
            grade_id = UNSET
        elif isinstance(self.grade_id, UUID):
            grade_id = str(self.grade_id)
        else:
            grade_id = self.grade_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interval": interval,
                "periods": periods,
                "as_of_date": as_of_date,
                "listing_type": listing_type,
            }
        )
        if parallel_id is not UNSET:
            field_dict["parallel_id"] = parallel_id
        if grade_id is not UNSET:
            field_dict["grade_id"] = grade_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = d.pop("interval")

        periods = d.pop("periods")

        as_of_date = d.pop("as_of_date")

        listing_type = d.pop("listing_type")

        def _parse_parallel_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parallel_id_type_0 = UUID(data)

                return parallel_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        parallel_id = _parse_parallel_id(d.pop("parallel_id", UNSET))

        def _parse_grade_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grade_id_type_0 = UUID(data)

                return grade_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        grade_id = _parse_grade_id(d.pop("grade_id", UNSET))

        timeseries_query_echo = cls(
            interval=interval,
            periods=periods,
            as_of_date=as_of_date,
            listing_type=listing_type,
            parallel_id=parallel_id,
            grade_id=grade_id,
        )

        return timeseries_query_echo
