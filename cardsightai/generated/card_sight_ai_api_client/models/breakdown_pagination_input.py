from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BreakdownPaginationInput")


@_attrs_define
class BreakdownPaginationInput:
    """
    Attributes:
        total_count (float): Total number of groups
        skip (float): Number of groups skipped
        take (float): Number of groups included
        page (float): Current page number
        pages (float): Total number of pages
    """

    total_count: float
    skip: float
    take: float
    page: float
    pages: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        skip = self.skip

        take = self.take

        page = self.page

        pages = self.pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_count": total_count,
                "skip": skip,
                "take": take,
                "page": page,
                "pages": pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        page = d.pop("page")

        pages = d.pop("pages")

        breakdown_pagination_input = cls(
            total_count=total_count,
            skip=skip,
            take=take,
            page=page,
            pages=pages,
        )

        breakdown_pagination_input.additional_properties = d
        return breakdown_pagination_input

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
