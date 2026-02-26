from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parallel_with_set_input_prices import ParallelWithSetInputPrices


T = TypeVar("T", bound="ParallelWithSetInput")


@_attrs_define
class ParallelWithSetInput:
    """
    Attributes:
        id (str): Unique identifier for the parallel type. Format: UUID v4. This ID represents the parallel variant, not
            individual cards.
        name (str): Name of the parallel variant. Examples: "Gold Refractor", "Black Prizm", "Orange". Describes the
            visual variant or rarity tier.
        set_id (str): Set UUID
        set_name (str): Set name
        release_id (str): Release UUID
        release_name (str): Release name
        release_year (str): Release year
        card_count (float): Number of base cards in the set
        description (Union[Unset, str]): Additional details about the parallel such as print run, special features, or
            visual description. May be null.
        is_partial (Union[Unset, bool]): Present and true only if this parallel applies to specific cards (e.g., cards
            1-400 of a 800-card set). Omitted if parallel applies to the entire set.
        numbered_to (Union[Unset, float]): Limited print run number for this parallel
        prices (Union[Unset, ParallelWithSetInputPrices]): Average pricing data for this parallel variant. Only included
            when price data is available.
        cards (Union[Unset, list[str]]): Card UUIDs that have this parallel. Only present when isPartial is true.
    """

    id: str
    name: str
    set_id: str
    set_name: str
    release_id: str
    release_name: str
    release_year: str
    card_count: float
    description: Union[Unset, str] = UNSET
    is_partial: Union[Unset, bool] = UNSET
    numbered_to: Union[Unset, float] = UNSET
    prices: Union[Unset, "ParallelWithSetInputPrices"] = UNSET
    cards: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        set_id = self.set_id

        set_name = self.set_name

        release_id = self.release_id

        release_name = self.release_name

        release_year = self.release_year

        card_count = self.card_count

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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "setId": set_id,
                "setName": set_name,
                "releaseId": release_id,
                "releaseName": release_name,
                "releaseYear": release_year,
                "cardCount": card_count,
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
        from ..models.parallel_with_set_input_prices import ParallelWithSetInputPrices

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        set_id = d.pop("setId")

        set_name = d.pop("setName")

        release_id = d.pop("releaseId")

        release_name = d.pop("releaseName")

        release_year = d.pop("releaseYear")

        card_count = d.pop("cardCount")

        description = d.pop("description", UNSET)

        is_partial = d.pop("isPartial", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, ParallelWithSetInputPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = ParallelWithSetInputPrices.from_dict(_prices)

        cards = cast(list[str], d.pop("cards", UNSET))

        parallel_with_set_input = cls(
            id=id,
            name=name,
            set_id=set_id,
            set_name=set_name,
            release_id=release_id,
            release_name=release_name,
            release_year=release_year,
            card_count=card_count,
            description=description,
            is_partial=is_partial,
            numbered_to=numbered_to,
            prices=prices,
            cards=cards,
        )

        parallel_with_set_input.additional_properties = d
        return parallel_with_set_input

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
