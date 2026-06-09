from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SourceBreakdownItem")


@_attrs_define
class SourceBreakdownItem:
    """
    Attributes:
        source (str): Source name
        count (int): Number of records from this source
    """

    source: str
    count: int

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        count = d.pop("count")

        source_breakdown_item = cls(
            source=source,
            count=count,
        )

        return source_breakdown_item
