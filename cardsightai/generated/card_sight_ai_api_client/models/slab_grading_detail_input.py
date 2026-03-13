from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slab_grading_detail_input_confidence import SlabGradingDetailInputConfidence

if TYPE_CHECKING:
    from ..models.slab_company_input import SlabCompanyInput


T = TypeVar("T", bound="SlabGradingDetailInput")


@_attrs_define
class SlabGradingDetailInput:
    """
    Attributes:
        confidence (SlabGradingDetailInputConfidence): Detection confidence level for this slab (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        company (SlabCompanyInput):
    """

    confidence: SlabGradingDetailInputConfidence
    company: "SlabCompanyInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        company = self.company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slab_company_input import SlabCompanyInput

        d = dict(src_dict)
        confidence = SlabGradingDetailInputConfidence(d.pop("confidence"))

        company = SlabCompanyInput.from_dict(d.pop("company"))

        slab_grading_detail_input = cls(
            confidence=confidence,
            company=company,
        )

        slab_grading_detail_input.additional_properties = d
        return slab_grading_detail_input

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
