from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pricing_search_record_input_listing_type_type_0 import PricingSearchRecordInputListingTypeType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_grade_input import SearchGradeInput
    from ..models.search_matched_card_input import SearchMatchedCardInput


T = TypeVar("T", bound="PricingSearchRecordInput")


@_attrs_define
class PricingSearchRecordInput:
    """
    Attributes:
        price (float): Price in USD. For auctions this is the final sale price (the "bid" side); for fixed/Buy It Now
            this is the seller's asking price (the "ask" side) and is NOT necessarily a completed sale.
        source (str): Data source (e.g., "ebay")
        title (Union[None, Unset, str]): Listing title from marketplace
        date (Union[None, Unset, str]): Date the listing ended, in ISO 8601 format
        listing_type (Union[None, PricingSearchRecordInputListingTypeType0, Unset]): Listing type: "auction" = a
            completed auction sale (bid side), "fixed" = a Buy It Now asking price (ask side).
        url (Union[None, Unset, str]): URL to the original listing
        image_url (Union[None, Unset, str]): Primary image URL for the listing
        parallel_id (Union[None, UUID, Unset]): Parallel variant UUID. Null for base card listings.
        parallel_name (Union[None, Unset, str]): Parallel variant name. Null for base card listings.
        matched_card (Union[Unset, SearchMatchedCardInput]):
        grade (Union[Unset, SearchGradeInput]):
    """

    price: float
    source: str
    title: Union[None, Unset, str] = UNSET
    date: Union[None, Unset, str] = UNSET
    listing_type: Union[None, PricingSearchRecordInputListingTypeType0, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    parallel_id: Union[None, UUID, Unset] = UNSET
    parallel_name: Union[None, Unset, str] = UNSET
    matched_card: Union[Unset, "SearchMatchedCardInput"] = UNSET
    grade: Union[Unset, "SearchGradeInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        elif isinstance(self.listing_type, PricingSearchRecordInputListingTypeType0):
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

        matched_card: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matched_card, Unset):
            matched_card = self.matched_card.to_dict()

        grade: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grade, Unset):
            grade = self.grade.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if matched_card is not UNSET:
            field_dict["matched_card"] = matched_card
        if grade is not UNSET:
            field_dict["grade"] = grade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_grade_input import SearchGradeInput
        from ..models.search_matched_card_input import SearchMatchedCardInput

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

        def _parse_listing_type(data: object) -> Union[None, PricingSearchRecordInputListingTypeType0, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                listing_type_type_0 = PricingSearchRecordInputListingTypeType0(data)

                return listing_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PricingSearchRecordInputListingTypeType0, Unset], data)

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

        _matched_card = d.pop("matched_card", UNSET)
        matched_card: Union[Unset, SearchMatchedCardInput]
        if isinstance(_matched_card, Unset):
            matched_card = UNSET
        else:
            matched_card = SearchMatchedCardInput.from_dict(_matched_card)

        _grade = d.pop("grade", UNSET)
        grade: Union[Unset, SearchGradeInput]
        if isinstance(_grade, Unset):
            grade = UNSET
        else:
            grade = SearchGradeInput.from_dict(_grade)

        pricing_search_record_input = cls(
            price=price,
            source=source,
            title=title,
            date=date,
            listing_type=listing_type,
            url=url,
            image_url=image_url,
            parallel_id=parallel_id,
            parallel_name=parallel_name,
            matched_card=matched_card,
            grade=grade,
        )

        pricing_search_record_input.additional_properties = d
        return pricing_search_record_input

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
