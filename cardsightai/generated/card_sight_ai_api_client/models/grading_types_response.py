from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.grading_company import GradingCompany
    from ..models.grading_type import GradingType


T = TypeVar("T", bound="GradingTypesResponse")


@_attrs_define
class GradingTypesResponse:
    """
    Attributes:
        types (list['GradingType']): List of grading types offered by this company
        total (float): Total number of grading types for this company
        grading_company (GradingCompany):
    """

    types: list["GradingType"]
    total: float
    grading_company: "GradingCompany"

    def to_dict(self) -> dict[str, Any]:
        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        total = self.total

        grading_company = self.grading_company.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "types": types,
                "total": total,
                "gradingCompany": grading_company,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grading_company import GradingCompany
        from ..models.grading_type import GradingType

        d = dict(src_dict)
        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = GradingType.from_dict(types_item_data)

            types.append(types_item)

        total = d.pop("total")

        grading_company = GradingCompany.from_dict(d.pop("gradingCompany"))

        grading_types_response = cls(
            types=types,
            total=total,
            grading_company=grading_company,
        )

        return grading_types_response
