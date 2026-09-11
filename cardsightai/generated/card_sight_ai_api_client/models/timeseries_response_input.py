from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pricing_card_context_input import PricingCardContextInput
    from ..models.raw_timeseries_section_input import RawTimeseriesSectionInput
    from ..models.timeseries_company_group_input import TimeseriesCompanyGroupInput
    from ..models.timeseries_query_echo_input import TimeseriesQueryEchoInput


T = TypeVar("T", bound="TimeseriesResponseInput")


@_attrs_define
class TimeseriesResponseInput:
    """
    Attributes:
        card (PricingCardContextInput):
        query (TimeseriesQueryEchoInput):
        raw (RawTimeseriesSectionInput):
        graded (list['TimeseriesCompanyGroupInput']): Per-grade candle series grouped by grading company, so graded and
            ungraded prices never blend into one candle range. Grades with no listings in the window are omitted; empty when
            the card has no graded listings in the window. When the grade_id filter pins a specific grade, this contains at
            most that one grade.
    """

    card: "PricingCardContextInput"
    query: "TimeseriesQueryEchoInput"
    raw: "RawTimeseriesSectionInput"
    graded: list["TimeseriesCompanyGroupInput"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        query = self.query.to_dict()

        raw = self.raw.to_dict()

        graded = []
        for graded_item_data in self.graded:
            graded_item = graded_item_data.to_dict()
            graded.append(graded_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.pricing_card_context_input import PricingCardContextInput
        from ..models.raw_timeseries_section_input import RawTimeseriesSectionInput
        from ..models.timeseries_company_group_input import TimeseriesCompanyGroupInput
        from ..models.timeseries_query_echo_input import TimeseriesQueryEchoInput

        d = dict(src_dict)
        card = PricingCardContextInput.from_dict(d.pop("card"))

        query = TimeseriesQueryEchoInput.from_dict(d.pop("query"))

        raw = RawTimeseriesSectionInput.from_dict(d.pop("raw"))

        graded = []
        _graded = d.pop("graded")
        for graded_item_data in _graded:
            graded_item = TimeseriesCompanyGroupInput.from_dict(graded_item_data)

            graded.append(graded_item)

        timeseries_response_input = cls(
            card=card,
            query=query,
            raw=raw,
            graded=graded,
        )

        timeseries_response_input.additional_properties = d
        return timeseries_response_input

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
