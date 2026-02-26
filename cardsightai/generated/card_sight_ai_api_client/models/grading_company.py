from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="GradingCompany")


@_attrs_define
class GradingCompany:
    """
    Attributes:
        id (UUID): Unique identifier for the grading company
        name (str): Name of the grading company (e.g., PSA, BGS, SGC, CGC)
        description (Union[None, str]): Detailed description of the grading company and its services
    """

    id: UUID
    name: str
    description: Union[None, str]

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: Union[None, str]
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        grading_company = cls(
            id=id,
            name=name,
            description=description,
        )

        return grading_company
