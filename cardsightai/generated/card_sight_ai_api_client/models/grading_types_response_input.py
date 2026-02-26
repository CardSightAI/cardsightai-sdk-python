from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grading_company_input import GradingCompanyInput
    from ..models.grading_type_input import GradingTypeInput


T = TypeVar("T", bound="GradingTypesResponseInput")


@_attrs_define
class GradingTypesResponseInput:
    """
    Attributes:
        types (list['GradingTypeInput']): List of grading types offered by this company
        total (float): Total number of grading types for this company
        grading_company (GradingCompanyInput):
    """

    types: list["GradingTypeInput"]
    total: float
    grading_company: "GradingCompanyInput"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        total = self.total

        grading_company = self.grading_company.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.grading_company_input import GradingCompanyInput
        from ..models.grading_type_input import GradingTypeInput

        d = dict(src_dict)
        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = GradingTypeInput.from_dict(types_item_data)

            types.append(types_item)

        total = d.pop("total")

        grading_company = GradingCompanyInput.from_dict(d.pop("gradingCompany"))

        grading_types_response_input = cls(
            types=types,
            total=total,
            grading_company=grading_company,
        )

        grading_types_response_input.additional_properties = d
        return grading_types_response_input

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
