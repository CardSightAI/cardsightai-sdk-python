from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.release_summary import ReleaseSummary


T = TypeVar("T", bound="PaginatedReleasesResponse")


@_attrs_define
class PaginatedReleasesResponse:
    """
    Attributes:
        releases (list['ReleaseSummary']): Array of release entities with summary information (e.g., "2023 Topps Chrome
            Baseball")
        total_count (float): Total number of releases matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    releases: list["ReleaseSummary"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "releases": releases,
                "total_count": total_count,
                "skip": skip,
                "take": take,
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

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_releases_response = cls(
            releases=releases,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_releases_response
