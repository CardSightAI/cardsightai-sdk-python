from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CollectionCompositionInput")


@_attrs_define
class CollectionCompositionInput:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graded_count = self.graded_count

        raw_count = self.raw_count

        graded_percentage = self.graded_percentage

        for_sale_count = self.for_sale_count

        sold_count = self.sold_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        collection_composition_input = cls(
            graded_count=graded_count,
            raw_count=raw_count,
            graded_percentage=graded_percentage,
            for_sale_count=for_sale_count,
            sold_count=sold_count,
        )

        collection_composition_input.additional_properties = d
        return collection_composition_input

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
