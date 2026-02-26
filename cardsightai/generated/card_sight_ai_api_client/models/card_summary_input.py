from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_summary_input_parallels_item import CardSummaryInputParallelsItem
    from ..models.card_summary_input_prices import CardSummaryInputPrices


T = TypeVar("T", bound="CardSummaryInput")


@_attrs_define
class CardSummaryInput:
    """
    Attributes:
        release_id (str): UUID of the release this card belongs to. Provided for convenience to avoid additional
            lookups.
        set_id (str): UUID of the set this card belongs to. Links to the set entity. Determines which collection within
            the release contains this card.
        id (str): Unique identifier for the card. Format: UUID v4. This ID is permanent and used for all API operations
            involving this card.
        name (str): Primary subject of the card. Usually a player name for sports cards (e.g., "Michael Jordan") or
            character/subject for non-sports.
        set_name (str): Name of the set this card belongs to
        number (Union[Unset, str]): Card number within the set. Examples: "23", "RC-15", "L-5". May include letters for
            special subsets. Null for unnumbered cards.
        description (Union[Unset, str]): Additional card details such as team, position, special notations, or card back
            information. May be null.
        is_parallel_only (Union[Unset, bool]): Indicates this card exists only as a parallel, not as a base card. For
            example, if a set has 15 base cards but a parallel variant has 20 cards, the 5 extra cards would have
            isParallelOnly: true.
        release_name (Union[Unset, str]): Name of the release
        release_year (Union[Unset, str]): Year of the release
        attributes (Union[Unset, list[str]]): Array of attribute short names
        prices (Union[Unset, CardSummaryInputPrices]): Average pricing data for the base card. Only included when price
            data is available.
        variation_of (Union[Unset, str]): UUID of the base card if this is a variation. Only present for variation
            cards, omitted for base cards.
        parallels (Union[Unset, list['CardSummaryInputParallelsItem']]): Simplified list of parallel variants for this
            card. Includes id, name, and numberedTo.
    """

    release_id: str
    set_id: str
    id: str
    name: str
    set_name: str
    number: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_parallel_only: Union[Unset, bool] = UNSET
    release_name: Union[Unset, str] = UNSET
    release_year: Union[Unset, str] = UNSET
    attributes: Union[Unset, list[str]] = UNSET
    prices: Union[Unset, "CardSummaryInputPrices"] = UNSET
    variation_of: Union[Unset, str] = UNSET
    parallels: Union[Unset, list["CardSummaryInputParallelsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        set_id = self.set_id

        id = self.id

        name = self.name

        set_name = self.set_name

        number = self.number

        description = self.description

        is_parallel_only = self.is_parallel_only

        release_name = self.release_name

        release_year = self.release_year

        attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        prices: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prices, Unset):
            prices = self.prices.to_dict()

        variation_of = self.variation_of

        parallels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parallels, Unset):
            parallels = []
            for parallels_item_data in self.parallels:
                parallels_item = parallels_item_data.to_dict()
                parallels.append(parallels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "releaseId": release_id,
                "setId": set_id,
                "id": id,
                "name": name,
                "setName": set_name,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
        if is_parallel_only is not UNSET:
            field_dict["isParallelOnly"] = is_parallel_only
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if release_year is not UNSET:
            field_dict["releaseYear"] = release_year
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if prices is not UNSET:
            field_dict["prices"] = prices
        if variation_of is not UNSET:
            field_dict["variationOf"] = variation_of
        if parallels is not UNSET:
            field_dict["parallels"] = parallels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_summary_input_parallels_item import CardSummaryInputParallelsItem
        from ..models.card_summary_input_prices import CardSummaryInputPrices

        d = dict(src_dict)
        release_id = d.pop("releaseId")

        set_id = d.pop("setId")

        id = d.pop("id")

        name = d.pop("name")

        set_name = d.pop("setName")

        number = d.pop("number", UNSET)

        description = d.pop("description", UNSET)

        is_parallel_only = d.pop("isParallelOnly", UNSET)

        release_name = d.pop("releaseName", UNSET)

        release_year = d.pop("releaseYear", UNSET)

        attributes = cast(list[str], d.pop("attributes", UNSET))

        _prices = d.pop("prices", UNSET)
        prices: Union[Unset, CardSummaryInputPrices]
        if isinstance(_prices, Unset):
            prices = UNSET
        else:
            prices = CardSummaryInputPrices.from_dict(_prices)

        variation_of = d.pop("variationOf", UNSET)

        parallels = []
        _parallels = d.pop("parallels", UNSET)
        for parallels_item_data in _parallels or []:
            parallels_item = CardSummaryInputParallelsItem.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        card_summary_input = cls(
            release_id=release_id,
            set_id=set_id,
            id=id,
            name=name,
            set_name=set_name,
            number=number,
            description=description,
            is_parallel_only=is_parallel_only,
            release_name=release_name,
            release_year=release_year,
            attributes=attributes,
            prices=prices,
            variation_of=variation_of,
            parallels=parallels,
        )

        card_summary_input.additional_properties = d
        return card_summary_input

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
