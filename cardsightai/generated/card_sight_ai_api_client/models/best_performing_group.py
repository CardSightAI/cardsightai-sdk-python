from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BestPerformingGroup")


@_attrs_define
class BestPerformingGroup:
    """
    Attributes:
        name (str): Name of best performing group
        roi (float): ROI percentage
    """

    name: str
    roi: float

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        roi = self.roi

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "roi": roi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        roi = d.pop("roi")

        best_performing_group = cls(
            name=name,
            roi=roi,
        )

        return best_performing_group
