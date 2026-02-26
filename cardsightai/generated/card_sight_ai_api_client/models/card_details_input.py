from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_details_input_parallel import CardDetailsInputParallel


T = TypeVar("T", bound="CardDetailsInput")


@_attrs_define
class CardDetailsInput:
    """
    Attributes:
        id (Union[Unset, str]): UUID of the identified card. Present only for exact card matches.
        segment_id (Union[Unset, str]): UUID of the segment. Present for both exact card and set-level matches.
        release_id (Union[Unset, str]): UUID of the release. Present for both exact card and set-level matches.
        set_id (Union[Unset, str]): UUID of the set. Present for both exact card and set-level matches.
        year (Union[Unset, str]): Release year from catalog (e.g., "2023", "1989")
        manufacturer (Union[Unset, str]): Card manufacturer from catalog (e.g., "Topps", "Panini", "Upper Deck")
        release_name (Union[Unset, str]): Release/product name from catalog (e.g., "Topps Chrome", "Prizm Basketball")
        set_name (Union[Unset, str]): Set name from catalog (e.g., "Base Set", "Rookie Variations")
        name (Union[Unset, str]): Player or subject name. Present only for exact card matches.
        number (Union[Unset, str]): Card number. Present only for exact card matches.
        parallel (Union[Unset, CardDetailsInputParallel]): Parallel variant info. Present only for exact card matches
            with an identified parallel.
    """

    id: Union[Unset, str] = UNSET
    segment_id: Union[Unset, str] = UNSET
    release_id: Union[Unset, str] = UNSET
    set_id: Union[Unset, str] = UNSET
    year: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    release_name: Union[Unset, str] = UNSET
    set_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    parallel: Union[Unset, "CardDetailsInputParallel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        release_id = self.release_id

        set_id = self.set_id

        year = self.year

        manufacturer = self.manufacturer

        release_name = self.release_name

        set_name = self.set_name

        name = self.name

        number = self.number

        parallel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parallel, Unset):
            parallel = self.parallel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if set_id is not UNSET:
            field_dict["setId"] = set_id
        if year is not UNSET:
            field_dict["year"] = year
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if set_name is not UNSET:
            field_dict["setName"] = set_name
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if parallel is not UNSET:
            field_dict["parallel"] = parallel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_details_input_parallel import CardDetailsInputParallel

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        segment_id = d.pop("segmentId", UNSET)

        release_id = d.pop("releaseId", UNSET)

        set_id = d.pop("setId", UNSET)

        year = d.pop("year", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        release_name = d.pop("releaseName", UNSET)

        set_name = d.pop("setName", UNSET)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        _parallel = d.pop("parallel", UNSET)
        parallel: Union[Unset, CardDetailsInputParallel]
        if isinstance(_parallel, Unset):
            parallel = UNSET
        else:
            parallel = CardDetailsInputParallel.from_dict(_parallel)

        card_details_input = cls(
            id=id,
            segment_id=segment_id,
            release_id=release_id,
            set_id=set_id,
            year=year,
            manufacturer=manufacturer,
            release_name=release_name,
            set_name=set_name,
            name=name,
            number=number,
            parallel=parallel,
        )

        card_details_input.additional_properties = d
        return card_details_input

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
