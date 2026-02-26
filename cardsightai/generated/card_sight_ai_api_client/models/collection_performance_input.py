from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_gainer_card_input import TopGainerCardInput
    from ..models.top_value_card_input import TopValueCardInput


T = TypeVar("T", bound="CollectionPerformanceInput")


@_attrs_define
class CollectionPerformanceInput:
    """
    Attributes:
        average_card_value (Union[Unset, str]): Average current value per card
        average_roi (Union[Unset, float]): Average ROI across all cards with buy prices
        top_gainer (Union[Unset, TopGainerCardInput]):
        top_value (Union[Unset, TopValueCardInput]):
    """

    average_card_value: Union[Unset, str] = UNSET
    average_roi: Union[Unset, float] = UNSET
    top_gainer: Union[Unset, "TopGainerCardInput"] = UNSET
    top_value: Union[Unset, "TopValueCardInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_card_value = self.average_card_value

        average_roi = self.average_roi

        top_gainer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.top_gainer, Unset):
            top_gainer = self.top_gainer.to_dict()

        top_value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.top_value, Unset):
            top_value = self.top_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_card_value is not UNSET:
            field_dict["averageCardValue"] = average_card_value
        if average_roi is not UNSET:
            field_dict["averageROI"] = average_roi
        if top_gainer is not UNSET:
            field_dict["topGainer"] = top_gainer
        if top_value is not UNSET:
            field_dict["topValue"] = top_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_gainer_card_input import TopGainerCardInput
        from ..models.top_value_card_input import TopValueCardInput

        d = dict(src_dict)
        average_card_value = d.pop("averageCardValue", UNSET)

        average_roi = d.pop("averageROI", UNSET)

        _top_gainer = d.pop("topGainer", UNSET)
        top_gainer: Union[Unset, TopGainerCardInput]
        if isinstance(_top_gainer, Unset):
            top_gainer = UNSET
        else:
            top_gainer = TopGainerCardInput.from_dict(_top_gainer)

        _top_value = d.pop("topValue", UNSET)
        top_value: Union[Unset, TopValueCardInput]
        if isinstance(_top_value, Unset):
            top_value = UNSET
        else:
            top_value = TopValueCardInput.from_dict(_top_value)

        collection_performance_input = cls(
            average_card_value=average_card_value,
            average_roi=average_roi,
            top_gainer=top_gainer,
            top_value=top_value,
        )

        collection_performance_input.additional_properties = d
        return collection_performance_input

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
