from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BreakdownPagination")


@_attrs_define
class BreakdownPagination:
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

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        skip = self.skip

        take = self.take

        page = self.page

        pages = self.pages

        field_dict: dict[str, Any] = {}

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

        breakdown_pagination = cls(
            total_count=total_count,
            skip=skip,
            take=take,
            page=page,
            pages=pages,
        )

        return breakdown_pagination
