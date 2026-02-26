from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_gainer_card import TopGainerCard
    from ..models.top_value_card import TopValueCard


T = TypeVar("T", bound="CollectionPerformance")


@_attrs_define
class CollectionPerformance:
    """
    Attributes:
        average_card_value (Union[Unset, str]): Average current value per card
        average_roi (Union[Unset, float]): Average ROI across all cards with buy prices
        top_gainer (Union[Unset, TopGainerCard]):
        top_value (Union[Unset, TopValueCard]):
    """

    average_card_value: Union[Unset, str] = UNSET
    average_roi: Union[Unset, float] = UNSET
    top_gainer: Union[Unset, "TopGainerCard"] = UNSET
    top_value: Union[Unset, "TopValueCard"] = UNSET

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
        from ..models.top_gainer_card import TopGainerCard
        from ..models.top_value_card import TopValueCard

        d = dict(src_dict)
        average_card_value = d.pop("averageCardValue", UNSET)

        average_roi = d.pop("averageROI", UNSET)

        _top_gainer = d.pop("topGainer", UNSET)
        top_gainer: Union[Unset, TopGainerCard]
        if isinstance(_top_gainer, Unset):
            top_gainer = UNSET
        else:
            top_gainer = TopGainerCard.from_dict(_top_gainer)

        _top_value = d.pop("topValue", UNSET)
        top_value: Union[Unset, TopValueCard]
        if isinstance(_top_value, Unset):
            top_value = UNSET
        else:
            top_value = TopValueCard.from_dict(_top_value)

        collection_performance = cls(
            average_card_value=average_card_value,
            average_roi=average_roi,
            top_gainer=top_gainer,
            top_value=top_value,
        )

        return collection_performance
