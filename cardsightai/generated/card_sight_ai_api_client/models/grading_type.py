from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="GradingType")


@_attrs_define
class GradingType:
    """
    Attributes:
        id (UUID): Unique identifier for the grading type
        grading_company_id (UUID): ID of the parent grading company offering this grading type
        grading_company_name (str): Name of the parent grading company (denormalized for convenience)
        name (str): Name of the grading type (e.g., Regular, Crossover, Black Label)
        description (Union[None, str]): Detailed description of what this grading type offers or represents
    """

    id: UUID
    grading_company_id: UUID
    grading_company_name: str
    name: str
    description: Union[None, str]

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        grading_company_id = str(self.grading_company_id)

        grading_company_name = self.grading_company_name

        name = self.name

        description: Union[None, str]
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "gradingCompanyId": grading_company_id,
                "gradingCompanyName": grading_company_name,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        grading_company_id = UUID(d.pop("gradingCompanyId"))

        grading_company_name = d.pop("gradingCompanyName")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        grading_type = cls(
            id=id,
            grading_company_id=grading_company_id,
            grading_company_name=grading_company_name,
            name=name,
            description=description,
        )

        return grading_type
