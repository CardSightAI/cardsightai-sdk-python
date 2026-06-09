from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.marketplace_company_group_input import MarketplaceCompanyGroupInput
    from ..models.marketplace_meta_input import MarketplaceMetaInput
    from ..models.pricing_card_context_input import PricingCardContextInput
    from ..models.pricing_query_echo_input import PricingQueryEchoInput
    from ..models.raw_marketplace_section_input import RawMarketplaceSectionInput


T = TypeVar("T", bound="MarketplaceResponseInput")


@_attrs_define
class MarketplaceResponseInput:
    """
    Attributes:
        card (PricingCardContextInput):
        query (PricingQueryEchoInput):
        raw (RawMarketplaceSectionInput):
        graded (list['MarketplaceCompanyGroupInput']): Graded active listings grouped by company and grade
        meta (MarketplaceMetaInput):
    """

    card: "PricingCardContextInput"
    query: "PricingQueryEchoInput"
    raw: "RawMarketplaceSectionInput"
    graded: list["MarketplaceCompanyGroupInput"]
    meta: "MarketplaceMetaInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        query = self.query.to_dict()

        raw = self.raw.to_dict()

        graded = []
        for graded_item_data in self.graded:
            graded_item = graded_item_data.to_dict()
            graded.append(graded_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "query": query,
                "raw": raw,
                "graded": graded,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.marketplace_company_group_input import MarketplaceCompanyGroupInput
        from ..models.marketplace_meta_input import MarketplaceMetaInput
        from ..models.pricing_card_context_input import PricingCardContextInput
        from ..models.pricing_query_echo_input import PricingQueryEchoInput
        from ..models.raw_marketplace_section_input import RawMarketplaceSectionInput

        d = dict(src_dict)
        card = PricingCardContextInput.from_dict(d.pop("card"))

        query = PricingQueryEchoInput.from_dict(d.pop("query"))

        raw = RawMarketplaceSectionInput.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = MarketplaceCompanyGroupInput.from_dict(graded_item_data)

            graded.append(graded_item)

        meta = MarketplaceMetaInput.from_dict(d.pop("meta"))

        marketplace_response_input = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
            meta=meta,
        )

        marketplace_response_input.additional_properties = d
        return marketplace_response_input

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
