from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseSummary")


@_attrs_define
class ReleaseSummary:
    """
    Attributes:
        manufacturer_id (str): UUID of the manufacturer that produced this release. Links to the manufacturer entity.
        segment_id (str): UUID of the segment this release belongs to. Links to the segment entity. Determines the
            market category (Sports, Entertainment, etc.).
        id (str): Unique identifier for the release. Format: UUID v4. This ID is permanent and used for all API
            operations involving this release.
        year (str): Year the release was issued. Format: YYYY (e.g., "2023"). Used for chronological filtering and
            sorting.
        name (str): Full name of the release. Typically includes year, brand, and sport/category. Example: "2023 Topps
            Chrome Baseball"
        is_identifiable (bool): Whether any set in this release can be identified by the CardSightAI identification
            service. True if at least one set has is_identifiable = true.
        description (Union[Unset, str]):
    """

    manufacturer_id: str
    segment_id: str
    id: str
    year: str
    name: str
    is_identifiable: bool
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        manufacturer_id = self.manufacturer_id

        segment_id = self.segment_id

        id = self.id

        year = self.year

        name = self.name

        is_identifiable = self.is_identifiable

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "manufacturerId": manufacturer_id,
                "segmentId": segment_id,
                "id": id,
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
        manufacturer_id = d.pop("manufacturerId")

        segment_id = d.pop("segmentId")

        id = d.pop("id")

        year = d.pop("year")

        name = d.pop("name")

        is_identifiable = d.pop("is_identifiable")

        description = d.pop("description", UNSET)

        release_summary = cls(
            manufacturer_id=manufacturer_id,
            segment_id=segment_id,
            id=id,
            year=year,
            name=name,
            is_identifiable=is_identifiable,
            description=description,
        )

        return release_summary
