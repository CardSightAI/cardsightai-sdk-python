from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.bulk_pricing_response_meta import BulkPricingResponseMeta
    from ..models.bulk_pricing_result import BulkPricingResult


T = TypeVar("T", bound="BulkPricingResponse")


@_attrs_define
class BulkPricingResponse:
    """
    Attributes:
        results (list['BulkPricingResult']): Pricing results for each requested card
        meta (BulkPricingResponseMeta): Summary counts
    """

    results: list["BulkPricingResult"]
    meta: "BulkPricingResponseMeta"

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "results": results,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_pricing_response_meta import BulkPricingResponseMeta
        from ..models.bulk_pricing_result import BulkPricingResult

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BulkPricingResult.from_dict(results_item_data)

            results.append(results_item)

        meta = BulkPricingResponseMeta.from_dict(d.pop("meta"))

        bulk_pricing_response = cls(
            results=results,
            meta=meta,
        )

        return bulk_pricing_response
