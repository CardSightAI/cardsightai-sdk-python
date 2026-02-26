from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogReleaseYearBreakdown")


@_attrs_define
class CatalogReleaseYearBreakdown:
    """
    Attributes:
        year (str): Release year
        count (float): Number of releases in this year for this segment
    """

    year: str
    count: float

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "year": year,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        count = d.pop("count")

        catalog_release_year_breakdown = cls(
            year=year,
            count=count,
        )

        return catalog_release_year_breakdown
