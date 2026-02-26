from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identification_data_input_confidence import IdentificationDataInputConfidence

if TYPE_CHECKING:
    from ..models.card_details_input import CardDetailsInput


T = TypeVar("T", bound="IdentificationDataInput")


@_attrs_define
class IdentificationDataInput:
    """
    Attributes:
        confidence (IdentificationDataInputConfidence): AI confidence level for this detection (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        card (CardDetailsInput):
    """

    confidence: IdentificationDataInputConfidence
    card: "CardDetailsInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        card = self.card.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "card": card,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_details_input import CardDetailsInput

        d = dict(src_dict)
        confidence = IdentificationDataInputConfidence(d.pop("confidence"))

        card = CardDetailsInput.from_dict(d.pop("card"))

        identification_data_input = cls(
            confidence=confidence,
            card=card,
        )

        identification_data_input.additional_properties = d
        return identification_data_input

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
