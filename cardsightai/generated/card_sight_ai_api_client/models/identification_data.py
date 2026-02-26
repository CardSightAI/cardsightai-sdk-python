from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.identification_data_confidence import IdentificationDataConfidence

if TYPE_CHECKING:
    from ..models.card_details import CardDetails


T = TypeVar("T", bound="IdentificationData")


@_attrs_define
class IdentificationData:
    """
    Attributes:
        confidence (IdentificationDataConfidence): AI confidence level for this detection (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        card (CardDetails):
    """

    confidence: IdentificationDataConfidence
    card: "CardDetails"

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        card = self.card.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confidence": confidence,
                "card": card,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_details import CardDetails

        d = dict(src_dict)
        confidence = IdentificationDataConfidence(d.pop("confidence"))

        card = CardDetails.from_dict(d.pop("card"))

        identification_data = cls(
            confidence=confidence,
            card=card,
        )

        return identification_data
