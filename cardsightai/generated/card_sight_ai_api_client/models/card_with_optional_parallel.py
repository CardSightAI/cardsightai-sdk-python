from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_with_optional_parallel_parallels_item import CardWithOptionalParallelParallelsItem
    from ..models.field_value import FieldValue


T = TypeVar("T", bound="CardWithOptionalParallel")


@_attrs_define
class CardWithOptionalParallel:
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
        variation_of (Union[Unset, str]): UUID of the base card if this is a variation. Only present for variation
            cards, omitted for base cards.
        parallels (Union[Unset, list['CardWithOptionalParallelParallelsItem']]): Simplified list of parallel variants
            for this card. Includes id, name, and numberedTo.
        fields (Union[Unset, list['FieldValue']]):
        is_parallel (Union[Unset, bool]): True if this card was converted to a parallel variant through the random odds
            system
        parallel_id (Union[Unset, str]): UUID of the parallel type if this card is a parallel variant
        parallel_name (Union[Unset, str]): Name of the parallel variant (e.g., "Gold Refractor", "Black Prizm 1/1")
        numbered_to (Union[None, Unset, float]): Limited print run number for this parallel. Null for unlimited
            parallels.
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
    variation_of: Union[Unset, str] = UNSET
    parallels: Union[Unset, list["CardWithOptionalParallelParallelsItem"]] = UNSET
    fields: Union[Unset, list["FieldValue"]] = UNSET
    is_parallel: Union[Unset, bool] = UNSET
    parallel_id: Union[Unset, str] = UNSET
    parallel_name: Union[Unset, str] = UNSET
    numbered_to: Union[None, Unset, float] = UNSET

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

        variation_of = self.variation_of

        parallels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parallels, Unset):
            parallels = []
            for parallels_item_data in self.parallels:
                parallels_item = parallels_item_data.to_dict()
                parallels.append(parallels_item)

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for componentsschemas_field_values_item_data in self.fields:
                componentsschemas_field_values_item = componentsschemas_field_values_item_data.to_dict()
                fields.append(componentsschemas_field_values_item)

        is_parallel = self.is_parallel

        parallel_id = self.parallel_id

        parallel_name = self.parallel_name

        numbered_to: Union[None, Unset, float]
        if isinstance(self.numbered_to, Unset):
            numbered_to = UNSET
        else:
            numbered_to = self.numbered_to

        field_dict: dict[str, Any] = {}

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
        if variation_of is not UNSET:
            field_dict["variationOf"] = variation_of
        if parallels is not UNSET:
            field_dict["parallels"] = parallels
        if fields is not UNSET:
            field_dict["fields"] = fields
        if is_parallel is not UNSET:
            field_dict["isParallel"] = is_parallel
        if parallel_id is not UNSET:
            field_dict["parallelId"] = parallel_id
        if parallel_name is not UNSET:
            field_dict["parallelName"] = parallel_name
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_with_optional_parallel_parallels_item import CardWithOptionalParallelParallelsItem
        from ..models.field_value import FieldValue

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

        variation_of = d.pop("variationOf", UNSET)

        parallels = []
        _parallels = d.pop("parallels", UNSET)
        for parallels_item_data in _parallels or []:
            parallels_item = CardWithOptionalParallelParallelsItem.from_dict(parallels_item_data)

            parallels.append(parallels_item)

        fields = []
        _fields = d.pop("fields", UNSET)
        for componentsschemas_field_values_item_data in _fields or []:
            componentsschemas_field_values_item = FieldValue.from_dict(componentsschemas_field_values_item_data)

            fields.append(componentsschemas_field_values_item)

        is_parallel = d.pop("isParallel", UNSET)

        parallel_id = d.pop("parallelId", UNSET)

        parallel_name = d.pop("parallelName", UNSET)

        def _parse_numbered_to(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        numbered_to = _parse_numbered_to(d.pop("numberedTo", UNSET))

        card_with_optional_parallel = cls(
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
            variation_of=variation_of,
            parallels=parallels,
            fields=fields,
            is_parallel=is_parallel,
            parallel_id=parallel_id,
            parallel_name=parallel_name,
            numbered_to=numbered_to,
        )

        return card_with_optional_parallel
