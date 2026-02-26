from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.release_summary_input import ReleaseSummaryInput


T = TypeVar("T", bound="RandomReleasesResponseInput")


@_attrs_define
class RandomReleasesResponseInput:
    """
    Attributes:
        releases (list['ReleaseSummaryInput']): Array of random releases matching the specified filters
        count (float): Actual number of releases returned. May be less than requested count if insufficient matches.
    """

    releases: list["ReleaseSummaryInput"]
    count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        releases = []
        for releases_item_data in self.releases:
            releases_item = releases_item_data.to_dict()
            releases.append(releases_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "releases": releases,
                "count": count,
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

        count = d.pop("count")

        random_releases_response_input = cls(
            releases=releases,
            count=count,
        )

        random_releases_response_input.additional_properties = d
        return random_releases_response_input

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
