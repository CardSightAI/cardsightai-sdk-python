from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PricingSearchQueryEcho")


@_attrs_define
class PricingSearchQueryEcho:
    """
    Attributes:
        q (str): Search query applied
        listing_type (str): Listing type filter applied
        as_of_date (str): Date the data was retrieved
        period (Union[Unset, str]): Period filter applied
        limit (Union[Unset, int]): Result limit applied
    """

    q: str
    listing_type: str
    as_of_date: str
    period: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        listing_type = self.listing_type

        as_of_date = self.as_of_date

        period = self.period

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "q": q,
                "listing_type": listing_type,
                "as_of_date": as_of_date,
            }
        )
        if period is not UNSET:
            field_dict["period"] = period
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        q = d.pop("q")

        listing_type = d.pop("listing_type")

        as_of_date = d.pop("as_of_date")

        period = d.pop("period", UNSET)

        limit = d.pop("limit", UNSET)

        pricing_search_query_echo = cls(
            q=q,
            listing_type=listing_type,
            as_of_date=as_of_date,
            period=period,
            limit=limit,
        )

        return pricing_search_query_echo
