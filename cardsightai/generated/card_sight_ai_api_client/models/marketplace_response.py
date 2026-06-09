from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.marketplace_company_group import MarketplaceCompanyGroup
    from ..models.marketplace_meta import MarketplaceMeta
    from ..models.pricing_card_context import PricingCardContext
    from ..models.pricing_query_echo import PricingQueryEcho
    from ..models.raw_marketplace_section import RawMarketplaceSection


T = TypeVar("T", bound="MarketplaceResponse")


@_attrs_define
class MarketplaceResponse:
    """
    Attributes:
        card (PricingCardContext):
        query (PricingQueryEcho):
        raw (RawMarketplaceSection):
        graded (list['MarketplaceCompanyGroup']): Graded active listings grouped by company and grade
        meta (MarketplaceMeta):
    """

    card: "PricingCardContext"
    query: "PricingQueryEcho"
    raw: "RawMarketplaceSection"
    graded: list["MarketplaceCompanyGroup"]
    meta: "MarketplaceMeta"

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
        from ..models.marketplace_company_group import MarketplaceCompanyGroup
        from ..models.marketplace_meta import MarketplaceMeta
        from ..models.pricing_card_context import PricingCardContext
        from ..models.pricing_query_echo import PricingQueryEcho
        from ..models.raw_marketplace_section import RawMarketplaceSection

        d = dict(src_dict)
        card = PricingCardContext.from_dict(d.pop("card"))

        query = PricingQueryEcho.from_dict(d.pop("query"))

        raw = RawMarketplaceSection.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = MarketplaceCompanyGroup.from_dict(graded_item_data)

            graded.append(graded_item)

        meta = MarketplaceMeta.from_dict(d.pop("meta"))

        marketplace_response = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
            meta=meta,
        )

        return marketplace_response
