from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IdentifiableSet")


@_attrs_define
class IdentifiableSet:
    """
    Attributes:
        year (str): Release year (e.g., "2024")
        release_name (str): Release/product name (e.g., "Topps Chrome")
        segment_name (str): Segment (sport/category) name (e.g., "Baseball")
        set_name (str): Set name (e.g., "Base Set")
        set_id (str): Set unique ID
    """

    year: str
    release_name: str
    segment_name: str
    set_name: str
    set_id: str

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        release_name = self.release_name

        segment_name = self.segment_name

        set_name = self.set_name

        set_id = self.set_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "year": year,
                "release_name": release_name,
                "segment_name": segment_name,
                "set_name": set_name,
                "set_id": set_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        release_name = d.pop("release_name")

        segment_name = d.pop("segment_name")

        set_name = d.pop("set_name")

        set_id = d.pop("set_id")

        identifiable_set = cls(
            year=year,
            release_name=release_name,
            segment_name=segment_name,
            set_name=set_name,
            set_id=set_id,
        )

        return identifiable_set
