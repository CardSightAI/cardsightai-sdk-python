from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.release_summary import ReleaseSummary


T = TypeVar("T", bound="RandomReleasesResponse")


@_attrs_define
class RandomReleasesResponse:
    """
    Attributes:
        releases (list['ReleaseSummary']): Array of random releases matching the specified filters
        count (float): Actual number of releases returned. May be less than requested count if insufficient matches.
    """

    releases: list["ReleaseSummary"]
    count: float

    def to_dict(self) -> dict[str, Any]:
        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "releases": releases,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_summary import ReleaseSummary

        d = dict(src_dict)
        releases = []
        _releases = d.pop("releases")
        for releases_item_data in _releases:
            releases_item = ReleaseSummary.from_dict(releases_item_data)

            releases.append(releases_item)

        count = d.pop("count")

        random_releases_response = cls(
            releases=releases,
            count=count,
        )

        return random_releases_response
