from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.identification_data_confidence import IdentificationDataConfidence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_details import CardDetails
    from ..models.slab_grading_detail import SlabGradingDetail


T = TypeVar("T", bound="IdentificationData")


@_attrs_define
class IdentificationData:
    """
    Attributes:
        confidence (IdentificationDataConfidence): AI confidence level for this detection (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        card (CardDetails):
        grading (Union[Unset, SlabGradingDetail]):
    """

    confidence: IdentificationDataConfidence
    card: "CardDetails"
    grading: Union[Unset, "SlabGradingDetail"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        card = self.card.to_dict()

        grading: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grading, Unset):
            grading = self.grading.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "card": card,
            }
        )
        if grading is not UNSET:
            field_dict["grading"] = grading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_details import CardDetails
        from ..models.slab_grading_detail import SlabGradingDetail

        d = dict(src_dict)
        confidence = IdentificationDataConfidence(d.pop("confidence"))

        card = CardDetails.from_dict(d.pop("card"))

        _grading = d.pop("grading", UNSET)
        grading: Union[Unset, SlabGradingDetail]
        if isinstance(_grading, Unset):
            grading = UNSET
        else:
            grading = SlabGradingDetail.from_dict(_grading)

        identification_data = cls(
            confidence=confidence,
            card=card,
            grading=grading,
        )

        return identification_data
