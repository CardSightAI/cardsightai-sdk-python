from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.bulk_pricing_request_listing_type import BulkPricingRequestListingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkPricingRequest")


@_attrs_define
class BulkPricingRequest:
    """
    Attributes:
        card_ids (list[UUID]): Array of card UUIDs to fetch pricing for (1-100). Matches the max page size of catalog
            search results.
        period (str): Lookback period. Examples: "7d", "14d", "2w", "3m", "1y", "all". Omit or "all" for no time limit.
            Default: 'all'.
        listing_type (BulkPricingRequestListingType): Filter by listing type. auction=completed auction sales (bid
            side), fixed=Buy It Now asking prices (ask side), both=all Default: BulkPricingRequestListingType.BOTH.
        parallel_id (Union[None, UUID, Unset]): Filter by parallel variant UUID. null = base card only.
        grade_id (Union[None, UUID, Unset]): Filter by grade UUID. null = ungraded only.
        limit (Union[Unset, int]): Most-recent listings to return per card. Defaults to 25 (server-applied when omitted)
            — across a full 100-card request that is up to 2,500 datapoints. Max 100 (up to 10,000 datapoints per request).
            For a card's full history use GET /pricing/{card_id} with as_of_date.
    """

    card_ids: list[UUID]
    period: str = "all"
    listing_type: BulkPricingRequestListingType = BulkPricingRequestListingType.BOTH
    parallel_id: Union[None, UUID, Unset] = UNSET
    grade_id: Union[None, UUID, Unset] = UNSET
    limit: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        card_ids = []
        for card_ids_item_data in self.card_ids:
            card_ids_item = str(card_ids_item_data)
            card_ids.append(card_ids_item)

        period = self.period

        listing_type = self.listing_type.value

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

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "card_ids": card_ids,
                "period": period,
                "listing_type": listing_type,
            }
        )
        if parallel_id is not UNSET:
            field_dict["parallel_id"] = parallel_id
        if grade_id is not UNSET:
            field_dict["grade_id"] = grade_id
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card_ids = []
        _card_ids = d.pop("card_ids")
        for card_ids_item_data in _card_ids:
            card_ids_item = UUID(card_ids_item_data)

            card_ids.append(card_ids_item)

        period = d.pop("period")

        listing_type = BulkPricingRequestListingType(d.pop("listing_type"))

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

        limit = d.pop("limit", UNSET)

        bulk_pricing_request = cls(
            card_ids=card_ids,
            period=period,
            listing_type=listing_type,
            parallel_id=parallel_id,
            grade_id=grade_id,
            limit=limit,
        )

        return bulk_pricing_request
