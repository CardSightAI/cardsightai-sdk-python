from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parallel_summary_prices import ParallelSummaryPrices


T = TypeVar("T", bound="ParallelSummary")


@_attrs_define
class ParallelSummary:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4. This ID represents the parallel variant, not
            individual cards.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange". Describes the
            visual variant or rarity tier.
        description (Union[Unset, str]): Additional details about the parallel such as print run, special features, or
            visual description. May be null.
        is_partial (Union[Unset, bool]): Present and true only if this parallel applies to specific cards (e.g., cards
            1-400 of a 800-card set). Omitted if parallel applies to the entire set.
        numbered_to (Union[Unset, float]): Limited print run number for this parallel
        prices (Union[Unset, ParallelSummaryPrices]): Average pricing data for this parallel variant. Only included when
            price data is available.
        cards (Union[Unset, list[str]]): Card UUIDs that have this parallel. Only present when isPartial is true.
    """

    id: str
    name: str
    description: Union[Unset, str] = UNSET
    is_partial: Union[Unset, bool] = UNSET
    numbered_to: Union[Unset, float] = UNSET
    prices: Union[Unset, "ParallelSummaryPrices"] = UNSET
    cards: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_partial = self.is_partial

        numbered_to = self.numbered_to

        prices: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict()

        cards: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_partial is not UNSET:
            field_dict["isPartial"] = is_partial
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to
        if prices is not UNSET:
            field_dict["prices"] = prices
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parallel_summary_prices import ParallelSummaryPrices

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_partial = d.pop("isPartial", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, ParallelSummaryPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = ParallelSummaryPrices.from_dict(_prices)

        cards = cast(list[str], d.pop("cards", UNSET))

        parallel_summary = cls(
            id=id,
            name=name,
            description=description,
            is_partial=is_partial,
            numbered_to=numbered_to,
            prices=prices,
            cards=cards,
        )

        return parallel_summary
