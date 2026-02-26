from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Release")


@_attrs_define
class Release:
    """
    Attributes:
        id (str): Unique identifier for the release. Format: UUID v4. This ID is permanent and used for all API
            operations involving this release.
        segment_id (str): UUID of the segment this release belongs to. Links to the segment entity. Determines the
            market category (Sports, Entertainment, etc.).
        manufacturer_id (str): UUID of the manufacturer that produced this release. Links to the manufacturer entity.
        year (str): Year the release was issued. Format: YYYY (e.g., "2023"). Used for chronological filtering and
            sorting.
        name (str): Full name of the release. Typically includes year, brand, and sport/category. Example: "2023 Topps
            Chrome Baseball"
        is_identifiable (bool): Whether any set in this release can be identified by the CardSightAI identification
            service. True if at least one set has is_identifiable = true.
        description (Union[Unset, str]): Additional details about the release, such as special features, number of
            cards, or notable inclusions. May be null.
    """

    id: str
    segment_id: str
    manufacturer_id: str
    year: str
    name: str
    is_identifiable: bool
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        segment_id = self.segment_id

        manufacturer_id = self.manufacturer_id

        year = self.year

        name = self.name

        is_identifiable = self.is_identifiable

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "segmentId": segment_id,
                "manufacturerId": manufacturer_id,
                "year": year,
                "name": name,
                "is_identifiable": is_identifiable,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        segment_id = d.pop("segmentId")

        manufacturer_id = d.pop("manufacturerId")

        year = d.pop("year")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        description = d.pop("description", UNSET)

        release = cls(
            id=id,
            segment_id=segment_id,
            manufacturer_id=manufacturer_id,
            year=year,
            name=name,
            is_identifiable=is_identifiable,
            description=description,
        )

        return release
