from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GradeInput")


@_attrs_define
class GradeInput:
    """
    Attributes:
        id (UUID): Unique identifier for the grade
        grading_type_id (UUID): ID of the parent grading type that this grade belongs to
        grading_type_name (str): Name of the parent grading type (denormalized for convenience)
        grading_company_id (UUID): ID of the grading company (denormalized for convenience)
        grading_company_name (str): Name of the grading company (denormalized for convenience)
        grade (str): The grade value as a string (e.g., "10", "9.5", "8") to support decimal and "Authentic" grades
        condition (Union[None, str]): The condition descriptor for this grade (e.g., "GEM MINT", "MINT", "PRISTINE")
    """

    id: UUID
    grading_type_id: UUID
    grading_type_name: str
    grading_company_id: UUID
    grading_company_name: str
    grade: str
    condition: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        grading_type_id = str(self.grading_type_id)

        grading_type_name = self.grading_type_name

        grading_company_id = str(self.grading_company_id)

        grading_company_name = self.grading_company_name

        grade = self.grade

        condition: Union[None, str]
        condition = self.condition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "gradingTypeId": grading_type_id,
                "gradingTypeName": grading_type_name,
                "gradingCompanyId": grading_company_id,
                "gradingCompanyName": grading_company_name,
                "grade": grade,
                "condition": condition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        grading_type_id = UUID(d.pop("gradingTypeId"))

        grading_type_name = d.pop("gradingTypeName")

        grading_company_id = UUID(d.pop("gradingCompanyId"))

        grading_company_name = d.pop("gradingCompanyName")

        grade = d.pop("grade")

        def _parse_condition(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        condition = _parse_condition(d.pop("condition"))

        grade_input = cls(
            id=id,
            grading_type_id=grading_type_id,
            grading_type_name=grading_type_name,
            grading_company_id=grading_company_id,
            grading_company_name=grading_company_name,
            grade=grade,
            condition=condition,
        )

        grade_input.additional_properties = d
        return grade_input

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
