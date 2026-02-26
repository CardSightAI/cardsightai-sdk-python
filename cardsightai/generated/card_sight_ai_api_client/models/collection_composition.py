from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CollectionComposition")


@_attrs_define
class CollectionComposition:
    """
    Attributes:
        graded_count (float): Number of graded cards
        raw_count (float): Number of raw (ungraded) cards
        graded_percentage (float): Percentage of collection that is graded
        for_sale_count (float): Number of cards listed for sale
        sold_count (float): Number of cards that have been sold
    """

    graded_count: float
    raw_count: float
    graded_percentage: float
    for_sale_count: float
    sold_count: float

    def to_dict(self) -> dict[str, Any]:
        graded_count = self.graded_count

        raw_count = self.raw_count

        graded_percentage = self.graded_percentage

        for_sale_count = self.for_sale_count

        sold_count = self.sold_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gradedCount": graded_count,
                "rawCount": raw_count,
                "gradedPercentage": graded_percentage,
                "forSaleCount": for_sale_count,
                "soldCount": sold_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        graded_count = d.pop("gradedCount")

        raw_count = d.pop("rawCount")

        graded_percentage = d.pop("gradedPercentage")

        for_sale_count = d.pop("forSaleCount")

        sold_count = d.pop("soldCount")

        collection_composition = cls(
            graded_count=graded_count,
            raw_count=raw_count,
            graded_percentage=graded_percentage,
            for_sale_count=for_sale_count,
            sold_count=sold_count,
        )

        return collection_composition
