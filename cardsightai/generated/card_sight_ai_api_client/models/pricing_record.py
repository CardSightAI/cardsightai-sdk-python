from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.pricing_record_listing_type_type_0 import PricingRecordListingTypeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="PricingRecord")


@_attrs_define
class PricingRecord:
    """
    Attributes:
        price (float): Price in USD. For auctions this is the final sale price (the "bid" side); for fixed/Buy It Now
            this is the seller's asking price (the "ask" side) and is NOT necessarily a completed sale.
        source (str): Data source (e.g., "ebay")
        title (Union[None, Unset, str]): Listing title from marketplace
        date (Union[None, Unset, str]): Date the listing ended, in ISO 8601 format
        listing_type (Union[None, PricingRecordListingTypeType0, Unset]): Listing type: "auction" = a completed auction
            sale (bid side), "fixed" = a Buy It Now asking price (ask side).
        url (Union[None, Unset, str]): URL to the original listing
        image_url (Union[None, Unset, str]): Primary image URL for the listing
        parallel_id (Union[None, UUID, Unset]): Parallel variant UUID. Null for base card listings.
        parallel_name (Union[None, Unset, str]): Parallel variant name. Null for base card listings.
    """

    price: float
    source: str
    title: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, str] = UNSET
    listing_type: Union[None, PricingRecordListingTypeType0, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    parallel_id: Union[None, UUID, Unset] = UNSET
    parallel_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        source = self.source

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        listing_type: Union[None, Unset, str]
        if isinstance(self.listing_type, Unset):
            listing_type = UNSET
        elif isinstance(self.listing_type, PricingRecordListingTypeType0):
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
                "price": price,
                "source": source,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if date is not UNSET:
            field_dict["date"] = date
        if listing_type is not UNSET:
            field_dict["listing_type"] = listing_type
        if url is not UNSET:
            field_dict["url"] = url
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if parallel_id is not UNSET:
            field_dict["parallel_id"] = parallel_id
        if parallel_name is not UNSET:
            field_dict["parallel_name"] = parallel_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price = d.pop("price")

        source = d.pop("source")

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_listing_type(data: object) -> Union[None, PricingRecordListingTypeType0, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_type_0 = PricingRecordListingTypeType0(data)

                return listing_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PricingRecordListingTypeType0, Unset], data)

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

        pricing_record = cls(
            price=price,
            source=source,
            title=title,
            date=date,
            listing_type=listing_type,
            url=url,
            image_url=image_url,
            parallel_id=parallel_id,
            parallel_name=parallel_name,
        )

        return pricing_record
