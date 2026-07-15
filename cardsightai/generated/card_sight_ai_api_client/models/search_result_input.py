from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_result_input_type import SearchResultInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResultInput")


@_attrs_define
class SearchResultInput:
    """
    Attributes:
        type_ (SearchResultInputType): Entity type of this search result.
        id (str): Unique identifier (UUID) for this entity. Use this ID to fetch full details from the corresponding
            entity endpoint.
        name (str): Primary name of the entity. Player/subject name for cards, set name for sets, release name for
            releases.
        relevance (float): Relevance score combining full-text search rank and fuzzy similarity. Higher values indicate
            stronger matches. Results are sorted by this score descending.
        year (Union[Unset, str]): Release year associated with this result.
        set_name (Union[Unset, str]): Set name. Present for card and parallel results.
        release_name (Union[Unset, str]): Release name. Present for card, set, and parallel results.
        manufacturer_name (Union[Unset, str]): Manufacturer name.
        parallel_name (Union[Unset, str]): Name of the matching parallel variant. Present when a parallel name
            contributed to this result's relevance.
        numbered_to (Union[Unset, int]): Serial print-run limit of the matching parallel (e.g. 25 for a /25). Present on
            parallel results, and on card results matched via `/N` slash notation.
    """

    type_: SearchResultInputType
    id: str
    name: str
    relevance: float
    year: Union[Unset, str] = UNSET
    set_name: Union[Unset, str] = UNSET
    release_name: Union[Unset, str] = UNSET
    manufacturer_name: Union[Unset, str] = UNSET
    parallel_name: Union[Unset, str] = UNSET
    numbered_to: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        name = self.name

        relevance = self.relevance

        year = self.year

        set_name = self.set_name

        release_name = self.release_name

        manufacturer_name = self.manufacturer_name

        parallel_name = self.parallel_name

        numbered_to = self.numbered_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "relevance": relevance,
            }
        )
        if year is not UNSET:
            field_dict["year"] = year
        if set_name is not UNSET:
            field_dict["setName"] = set_name
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if manufacturer_name is not UNSET:
            field_dict["manufacturerName"] = manufacturer_name
        if parallel_name is not UNSET:
            field_dict["parallelName"] = parallel_name
        if numbered_to is not UNSET:
            field_dict["numberedTo"] = numbered_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SearchResultInputType(d.pop("type"))

        id = d.pop("id")

        name = d.pop("name")

        relevance = d.pop("relevance")

        year = d.pop("year", UNSET)

        set_name = d.pop("setName", UNSET)

        release_name = d.pop("releaseName", UNSET)

        manufacturer_name = d.pop("manufacturerName", UNSET)

        parallel_name = d.pop("parallelName", UNSET)

        numbered_to = d.pop("numberedTo", UNSET)

        search_result_input = cls(
            type_=type_,
            id=id,
            name=name,
            relevance=relevance,
            year=year,
            set_name=set_name,
            release_name=release_name,
            manufacturer_name=manufacturer_name,
            parallel_name=parallel_name,
            numbered_to=numbered_to,
        )

        search_result_input.additional_properties = d
        return search_result_input

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
