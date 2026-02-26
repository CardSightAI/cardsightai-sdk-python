from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.release_summary_input import ReleaseSummaryInput


T = TypeVar("T", bound="PaginatedReleasesResponseInput")


@_attrs_define
class PaginatedReleasesResponseInput:
    """
    Attributes:
        releases (list['ReleaseSummaryInput']): Array of release entities with summary information (e.g., "2023 Topps
            Chrome Baseball")
        total_count (float): Total number of releases matching the query filters
        skip (float): Number of results skipped (offset) for pagination
        take (float): Number of results included in this page
    """

    releases: list["ReleaseSummaryInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.release_summary_input import ReleaseSummaryInput

        d = dict(src_dict)
        releases = []
        _releases = d.pop("releases")
        for releases_item_data in _releases:
            releases_item = ReleaseSummaryInput.from_dict(releases_item_data)

            releases.append(releases_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_releases_response_input = cls(
            releases=releases,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_releases_response_input.additional_properties = d
        return paginated_releases_response_input

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
