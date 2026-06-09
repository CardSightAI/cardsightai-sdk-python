from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.marketplace_record_listing_type_type_0 import MarketplaceRecordListingTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketplaceRecord")


@_attrs_define
class MarketplaceRecord:
    """
    Attributes:
        title (str): Listing title
        source (str): Marketplace source
        price (Union[None, Unset, float]): Current price or starting bid in USD
        listing_type (Union[MarketplaceRecordListingTypeType0, None, Unset]): Type of listing
        url (Union[None, Unset, str]): URL to the listing
        image_url (Union[None, Unset, str]): Primary image URL
        condition (Union[None, Unset, str]): Condition description from seller
        end_date (Union[None, Unset, str]): Listing end date in ISO 8601 format
        bid_count (Union[None, Unset, int]): Number of bids (auctions only)
        parallel_id (Union[None, UUID, Unset]): Parallel variant UUID. Null for base card listings.
        parallel_name (Union[None, Unset, str]): Parallel variant name. Null for base card listings.
    """

    title: str
    source: str
    price: Union[None, Unset, float] = UNSET
    listing_type: Union[MarketplaceRecordListingTypeType0, None, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    condition: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    bid_count: Union[None, Unset, int] = UNSET
    parallel_id: Union[None, UUID, Unset] = UNSET
    parallel_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        source = self.source

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        listing_type: Union[None, Unset, str]
        if isinstance(self.listing_type, Unset):
            listing_type = UNSET
        elif isinstance(self.listing_type, MarketplaceRecordListingTypeType0):
            listing_type = self.listing_type.value
        else:
            listing_type = self.listing_type

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        image_url: Union[None, Unset, str]
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        condition: Union[None, Unset, str]
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        bid_count: Union[None, Unset, int]
        if isinstance(self.bid_count, Unset):
            bid_count = UNSET
        else:
            bid_count = self.bid_count

        parallel_id: Union[None, Unset, str]
        if isinstance(self.parallel_id, Unset):
            parallel_id = UNSET
        elif isinstance(self.parallel_id, UUID):
            parallel_id = str(self.parallel_id)
        else:
            parallel_id = self.parallel_id

        parallel_name: Union[None, Unset, str]
        if isinstance(self.parallel_name, Unset):
            parallel_name = UNSET
        else:
            parallel_name = self.parallel_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "source": source,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if listing_type is not UNSET:
            field_dict["listing_type"] = listing_type
        if url is not UNSET:
            field_dict["url"] = url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if condition is not UNSET:
            field_dict["condition"] = condition
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if bid_count is not UNSET:
            field_dict["bid_count"] = bid_count
        if parallel_id is not UNSET:
            field_dict["parallel_id"] = parallel_id
        if parallel_name is not UNSET:
            field_dict["parallel_name"] = parallel_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        source = d.pop("source")

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_listing_type(data: object) -> Union[MarketplaceRecordListingTypeType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_type_0 = MarketplaceRecordListingTypeType0(data)

                return listing_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[MarketplaceRecordListingTypeType0, None, Unset], data)

        listing_type = _parse_listing_type(d.pop("listing_type", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        def _parse_condition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        condition = _parse_condition(d.pop("condition", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_bid_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bid_count = _parse_bid_count(d.pop("bid_count", UNSET))

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

        def _parse_parallel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parallel_name = _parse_parallel_name(d.pop("parallel_name", UNSET))

        marketplace_record = cls(
            title=title,
            source=source,
            price=price,
            listing_type=listing_type,
            url=url,
            image_url=image_url,
            condition=condition,
            end_date=end_date,
            bid_count=bid_count,
            parallel_id=parallel_id,
            parallel_name=parallel_name,
        )

        return marketplace_record
