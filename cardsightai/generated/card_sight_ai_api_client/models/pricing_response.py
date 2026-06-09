from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pricing_card_context import PricingCardContext
    from ..models.pricing_company_group import PricingCompanyGroup
    from ..models.pricing_meta import PricingMeta
    from ..models.pricing_query_echo import PricingQueryEcho
    from ..models.raw_pricing_section import RawPricingSection


T = TypeVar("T", bound="PricingResponse")


@_attrs_define
class PricingResponse:
    """
    Attributes:
        card (PricingCardContext):
        query (PricingQueryEcho):
        raw (RawPricingSection):
        graded (list['PricingCompanyGroup']): Graded pricing data grouped by company and grade
        meta (PricingMeta):
    """

    card: "PricingCardContext"
    query: "PricingQueryEcho"
    raw: "RawPricingSection"
    graded: list["PricingCompanyGroup"]
    meta: "PricingMeta"

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
        from ..models.pricing_card_context import PricingCardContext
        from ..models.pricing_company_group import PricingCompanyGroup
        from ..models.pricing_meta import PricingMeta
        from ..models.pricing_query_echo import PricingQueryEcho
        from ..models.raw_pricing_section import RawPricingSection

        d = dict(src_dict)
        card = PricingCardContext.from_dict(d.pop("card"))

        query = PricingQueryEcho.from_dict(d.pop("query"))

        raw = RawPricingSection.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = PricingCompanyGroup.from_dict(graded_item_data)

            graded.append(graded_item)

        meta = PricingMeta.from_dict(d.pop("meta"))

        pricing_response = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
            meta=meta,
        )

        return pricing_response
