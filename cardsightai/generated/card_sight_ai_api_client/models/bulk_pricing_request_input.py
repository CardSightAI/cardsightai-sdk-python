from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_pricing_request_input_listing_type import BulkPricingRequestInputListingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkPricingRequestInput")


@_attrs_define
class BulkPricingRequestInput:
    """
    Attributes:
        card_ids (list[UUID]): Array of card UUIDs to fetch pricing for (1-100). Matches the max page size of catalog
            search results.
        parallel_id (Union[None, UUID, Unset]): Filter by parallel variant UUID. null = base card only.
        grade_id (Union[None, UUID, Unset]): Filter by grade UUID. null = ungraded only.
        period (Union[Unset, str]): Lookback period. Examples: "7d", "14d", "2w", "3m", "1y", "all". Omit or "all" for
            no time limit. Default: 'all'.
        listing_type (Union[Unset, BulkPricingRequestInputListingType]): Filter by listing type. auction=completed
            auction sales (bid side), fixed=Buy It Now asking prices (ask side), both=all Default:
            BulkPricingRequestInputListingType.BOTH.
        limit (Union[Unset, int]): Maximum number of records per card
    """

    card_ids: list[UUID]
    parallel_id: Union[None, UUID, Unset] = UNSET
    grade_id: Union[None, UUID, Unset] = UNSET
    period: Union[Unset, str] = "all"
    listing_type: Union[Unset, BulkPricingRequestInputListingType] = BulkPricingRequestInputListingType.BOTH
    limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_ids = []
        for card_ids_item_data in self.card_ids:
            card_ids_item = str(card_ids_item_data)
            card_ids.append(card_ids_item)

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

        period = self.period

        listing_type: Union[Unset, str] = UNSET
        if not isinstance(self.listing_type, Unset):
            listing_type = self.listing_type.value

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card_ids": card_ids,
            }
        )
        if parallel_id is not UNSET:
            field_dict["parallel_id"] = parallel_id
        if grade_id is not UNSET:
            field_dict["grade_id"] = grade_id
        if period is not UNSET:
            field_dict["period"] = period
        if listing_type is not UNSET:
            field_dict["listing_type"] = listing_type
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

        period = d.pop("period", UNSET)

        _listing_type = d.pop("listing_type", UNSET)
        listing_type: Union[Unset, BulkPricingRequestInputListingType]
        if isinstance(_listing_type, Unset):
            listing_type = UNSET
        else:
            listing_type = BulkPricingRequestInputListingType(_listing_type)

        limit = d.pop("limit", UNSET)

        bulk_pricing_request_input = cls(
            card_ids=card_ids,
            parallel_id=parallel_id,
            grade_id=grade_id,
            period=period,
            listing_type=listing_type,
            limit=limit,
        )

        bulk_pricing_request_input.additional_properties = d
        return bulk_pricing_request_input

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
