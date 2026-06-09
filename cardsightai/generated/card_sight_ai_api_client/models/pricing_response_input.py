from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pricing_card_context_input import PricingCardContextInput
    from ..models.pricing_company_group_input import PricingCompanyGroupInput
    from ..models.pricing_meta_input import PricingMetaInput
    from ..models.pricing_query_echo_input import PricingQueryEchoInput
    from ..models.raw_pricing_section_input import RawPricingSectionInput


T = TypeVar("T", bound="PricingResponseInput")


@_attrs_define
class PricingResponseInput:
    """
    Attributes:
        card (PricingCardContextInput):
        query (PricingQueryEchoInput):
        raw (RawPricingSectionInput):
        graded (list['PricingCompanyGroupInput']): Graded pricing data grouped by company and grade
        meta (PricingMetaInput):
    """

    card: "PricingCardContextInput"
    query: "PricingQueryEchoInput"
    raw: "RawPricingSectionInput"
    graded: list["PricingCompanyGroupInput"]
    meta: "PricingMetaInput"
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
        from ..models.pricing_card_context_input import PricingCardContextInput
        from ..models.pricing_company_group_input import PricingCompanyGroupInput
        from ..models.pricing_meta_input import PricingMetaInput
        from ..models.pricing_query_echo_input import PricingQueryEchoInput
        from ..models.raw_pricing_section_input import RawPricingSectionInput

        d = dict(src_dict)
        card = PricingCardContextInput.from_dict(d.pop("card"))

        query = PricingQueryEchoInput.from_dict(d.pop("query"))

        raw = RawPricingSectionInput.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = PricingCompanyGroupInput.from_dict(graded_item_data)

            graded.append(graded_item)

        meta = PricingMetaInput.from_dict(d.pop("meta"))

        pricing_response_input = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
            meta=meta,
        )

        pricing_response_input.additional_properties = d
        return pricing_response_input

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
