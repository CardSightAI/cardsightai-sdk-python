from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.feedback_response_input_entity_type import FeedbackResponseInputEntityType
from ..models.feedback_response_input_feedback_type_type_0 import FeedbackResponseInputFeedbackTypeType0
from ..models.feedback_response_input_status import FeedbackResponseInputStatus

T = TypeVar("T", bound="FeedbackResponseInput")


@_attrs_define
class FeedbackResponseInput:
    """
    Attributes:
        unique_id (UUID):
        entity_type (FeedbackResponseInputEntityType): EntityType
        entity_id (Union[None, UUID]):
        feedback_type (Union[FeedbackResponseInputFeedbackTypeType0, None]):
        message (str):
        status (FeedbackResponseInputStatus): FeedbackStatus
        created_at (str):
        updated_at (str):
    """

    unique_id: UUID
    entity_type: FeedbackResponseInputEntityType
    entity_id: Union[None, UUID]
    feedback_type: Union[FeedbackResponseInputFeedbackTypeType0, None]
    message: str
    status: FeedbackResponseInputStatus
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unique_id = str(self.unique_id)

        entity_type = self.entity_type.value

        entity_id: Union[None, str]
        if isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        feedback_type: Union[None, str]
        if isinstance(self.feedback_type, FeedbackResponseInputFeedbackTypeType0):
            feedback_type = self.feedback_type.value
        else:
            feedback_type = self.feedback_type

        message = self.message

        status = self.status.value

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unique_id": unique_id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "feedback_type": feedback_type,
                "message": message,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unique_id = UUID(d.pop("unique_id"))

        entity_type = FeedbackResponseInputEntityType(d.pop("entity_type"))

        def _parse_entity_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        entity_id = _parse_entity_id(d.pop("entity_id"))

        def _parse_feedback_type(data: object) -> Union[FeedbackResponseInputFeedbackTypeType0, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feedback_type_type_0 = FeedbackResponseInputFeedbackTypeType0(data)

                return feedback_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FeedbackResponseInputFeedbackTypeType0, None], data)

        feedback_type = _parse_feedback_type(d.pop("feedback_type"))

        message = d.pop("message")

        status = FeedbackResponseInputStatus(d.pop("status"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        feedback_response_input = cls(
            unique_id=unique_id,
            entity_type=entity_type,
            entity_id=entity_id,
            feedback_type=feedback_type,
            message=message,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        feedback_response_input.additional_properties = d
        return feedback_response_input

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
