from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.slab_grading_detail_confidence import SlabGradingDetailConfidence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.slab_auto_grade import SlabAutoGrade
    from ..models.slab_company import SlabCompany
    from ..models.slab_grade import SlabGrade
    from ..models.slab_qualifier import SlabQualifier


T = TypeVar("T", bound="SlabGradingDetail")


@_attrs_define
class SlabGradingDetail:
    """
    Attributes:
        confidence (SlabGradingDetailConfidence): Detection confidence level for this slab (High: 90-100%, Medium:
            75-89%, Low: 50-74%)
        company (SlabCompany):
        grade (Union[Unset, SlabGrade]):
        qualifier (Union[Unset, SlabQualifier]):
        auto_grade (Union[Unset, SlabAutoGrade]):
    """

    confidence: SlabGradingDetailConfidence
    company: "SlabCompany"
    grade: Union[Unset, "SlabGrade"] = UNSET
    qualifier: Union[Unset, "SlabQualifier"] = UNSET
    auto_grade: Union[Unset, "SlabAutoGrade"] = UNSET

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
        from ..models.slab_auto_grade import SlabAutoGrade
        from ..models.slab_company import SlabCompany
        from ..models.slab_grade import SlabGrade
        from ..models.slab_qualifier import SlabQualifier

        d = dict(src_dict)
        confidence = SlabGradingDetailConfidence(d.pop("confidence"))

        company = SlabCompany.from_dict(d.pop("company"))

        _grade = d.pop("grade", UNSET)
        grade: Union[Unset, SlabGrade]
        if isinstance(_grade, Unset):
            grade = UNSET
        else:
            grade = SlabGrade.from_dict(_grade)

        _qualifier = d.pop("qualifier", UNSET)
        qualifier: Union[Unset, SlabQualifier]
        if isinstance(_qualifier, Unset):
            qualifier = UNSET
        else:
            qualifier = SlabQualifier.from_dict(_qualifier)

        _auto_grade = d.pop("autoGrade", UNSET)
        auto_grade: Union[Unset, SlabAutoGrade]
        if isinstance(_auto_grade, Unset):
            auto_grade = UNSET
        else:
            auto_grade = SlabAutoGrade.from_dict(_auto_grade)

        slab_grading_detail = cls(
            confidence=confidence,
            company=company,
            grade=grade,
            qualifier=qualifier,
            auto_grade=auto_grade,
        )

        return slab_grading_detail
