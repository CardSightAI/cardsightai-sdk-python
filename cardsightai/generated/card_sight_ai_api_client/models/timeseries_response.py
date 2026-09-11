from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pricing_card_context import PricingCardContext
    from ..models.raw_timeseries_section import RawTimeseriesSection
    from ..models.timeseries_company_group import TimeseriesCompanyGroup
    from ..models.timeseries_query_echo import TimeseriesQueryEcho


T = TypeVar("T", bound="TimeseriesResponse")


@_attrs_define
class TimeseriesResponse:
    """
    Attributes:
        card (PricingCardContext):
        query (TimeseriesQueryEcho):
        raw (RawTimeseriesSection):
        graded (list['TimeseriesCompanyGroup']): Per-grade candle series grouped by grading company, so graded and
            ungraded prices never blend into one candle range. Grades with no listings in the window are omitted; empty when
            the card has no graded listings in the window. When the grade_id filter pins a specific grade, this contains at
            most that one grade.
    """

    card: "PricingCardContext"
    query: "TimeseriesQueryEcho"
    raw: "RawTimeseriesSection"
    graded: list["TimeseriesCompanyGroup"]

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        query = self.query.to_dict()

        raw = self.raw.to_dict()

        graded = []
        for graded_item_data in self.graded:
            graded_item = graded_item_data.to_dict()
            graded.append(graded_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "card": card,
                "query": query,
                "raw": raw,
                "graded": graded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_card_context import PricingCardContext
        from ..models.raw_timeseries_section import RawTimeseriesSection
        from ..models.timeseries_company_group import TimeseriesCompanyGroup
        from ..models.timeseries_query_echo import TimeseriesQueryEcho

        d = dict(src_dict)
        card = PricingCardContext.from_dict(d.pop("card"))

        query = TimeseriesQueryEcho.from_dict(d.pop("query"))

        raw = RawTimeseriesSection.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = TimeseriesCompanyGroup.from_dict(graded_item_data)

            graded.append(graded_item)

        timeseries_response = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
        )

        return timeseries_response
