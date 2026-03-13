from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.slab_grading_detail_confidence import SlabGradingDetailConfidence

if TYPE_CHECKING:
    from ..models.slab_company import SlabCompany


T = TypeVar("T", bound="SlabGradingDetail")


@_attrs_define
class SlabGradingDetail:
    """
    Attributes:
        confidence (SlabGradingDetailConfidence): Detection confidence level for this slab (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        company (SlabCompany):
    """

    confidence: SlabGradingDetailConfidence
    company: "SlabCompany"

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        company = self.company.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "company": company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slab_company import SlabCompany

        d = dict(src_dict)
        confidence = SlabGradingDetailConfidence(d.pop("confidence"))

        company = SlabCompany.from_dict(d.pop("company"))

        slab_grading_detail = cls(
            confidence=confidence,
            company=company,
        )

        return slab_grading_detail
