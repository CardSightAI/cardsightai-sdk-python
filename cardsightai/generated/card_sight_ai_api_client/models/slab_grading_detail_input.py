from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slab_grading_detail_input_confidence import SlabGradingDetailInputConfidence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slab_auto_grade_input import SlabAutoGradeInput
    from ..models.slab_company_input import SlabCompanyInput
    from ..models.slab_grade_input import SlabGradeInput
    from ..models.slab_qualifier_input import SlabQualifierInput


T = TypeVar("T", bound="SlabGradingDetailInput")


@_attrs_define
class SlabGradingDetailInput:
    """
    Attributes:
        confidence (SlabGradingDetailInputConfidence): Detection confidence level for this slab (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        company (SlabCompanyInput):
        grade (Union[Unset, SlabGradeInput]):
        qualifier (Union[Unset, SlabQualifierInput]):
        auto_grade (Union[Unset, SlabAutoGradeInput]):
    """

    confidence: SlabGradingDetailInputConfidence
    company: "SlabCompanyInput"
    grade: Union[Unset, "SlabGradeInput"] = UNSET
    qualifier: Union[Unset, "SlabQualifierInput"] = UNSET
    auto_grade: Union[Unset, "SlabAutoGradeInput"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence.value

        company = self.company.to_dict()

        grade: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grade, Unset):
            grade = self.grade.to_dict()

        qualifier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.qualifier, Unset):
            qualifier = self.qualifier.to_dict()

        auto_grade: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto_grade, Unset):
            auto_grade = self.auto_grade.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "company": company,
            }
        )
        if grade is not UNSET:
            field_dict["grade"] = grade
        if qualifier is not UNSET:
            field_dict["qualifier"] = qualifier
        if auto_grade is not UNSET:
            field_dict["autoGrade"] = auto_grade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slab_auto_grade_input import SlabAutoGradeInput
        from ..models.slab_company_input import SlabCompanyInput
        from ..models.slab_grade_input import SlabGradeInput
        from ..models.slab_qualifier_input import SlabQualifierInput

        d = dict(src_dict)
        confidence = SlabGradingDetailInputConfidence(d.pop("confidence"))

        company = SlabCompanyInput.from_dict(d.pop("company"))

        _grade = d.pop("grade", UNSET)
        grade: Union[Unset, SlabGradeInput]
        if isinstance(_grade, Unset):
            grade = UNSET
        else:
            grade = SlabGradeInput.from_dict(_grade)

        _qualifier = d.pop("qualifier", UNSET)
        qualifier: Union[Unset, SlabQualifierInput]
        if isinstance(_qualifier, Unset):
            qualifier = UNSET
        else:
            qualifier = SlabQualifierInput.from_dict(_qualifier)

        _auto_grade = d.pop("autoGrade", UNSET)
        auto_grade: Union[Unset, SlabAutoGradeInput]
        if isinstance(_auto_grade, Unset):
            auto_grade = UNSET
        else:
            auto_grade = SlabAutoGradeInput.from_dict(_auto_grade)

        slab_grading_detail_input = cls(
            confidence=confidence,
            company=company,
            grade=grade,
            qualifier=qualifier,
            auto_grade=auto_grade,
        )

        slab_grading_detail_input.additional_properties = d
        return slab_grading_detail_input

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
