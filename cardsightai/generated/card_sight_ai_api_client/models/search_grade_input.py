from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchGradeInput")


@_attrs_define
class SearchGradeInput:
    """
    Attributes:
        grade_id (UUID): Grade UUID
        grade_value (str): Grade value (e.g., "10", "9.5")
        company_name (str): Grading company name (e.g., "PSA")
        company_id (UUID): Grading company UUID
    """

    grade_id: UUID
    grade_value: str
    company_name: str
    company_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grade_id = str(self.grade_id)

        grade_value = self.grade_value

        company_name = self.company_name

        company_id = str(self.company_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grade_id": grade_id,
                "grade_value": grade_value,
                "company_name": company_name,
                "company_id": company_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grade_id = UUID(d.pop("grade_id"))

        grade_value = d.pop("grade_value")

        company_name = d.pop("company_name")

        company_id = UUID(d.pop("company_id"))

        search_grade_input = cls(
            grade_id=grade_id,
            grade_value=grade_value,
            company_name=company_name,
            company_id=company_id,
        )

        search_grade_input.additional_properties = d
        return search_grade_input

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
