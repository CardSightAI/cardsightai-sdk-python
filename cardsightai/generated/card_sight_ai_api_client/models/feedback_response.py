from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.feedback_response_entity_type import FeedbackResponseEntityType
from ..models.feedback_response_feedback_type_type_0 import FeedbackResponseFeedbackTypeType0
from ..models.feedback_response_status import FeedbackResponseStatus

T = TypeVar("T", bound="FeedbackResponse")


@_attrs_define
class FeedbackResponse:
    """
    Attributes:
        unique_id (UUID): Unique identifier for this feedback submission
        entity_type (FeedbackResponseEntityType): The type of entity this feedback is about
        entity_id (Union[None, UUID]): The unique ID of the entity, or null for general feedback
        feedback_type (Union[FeedbackResponseFeedbackTypeType0, None]): The category of feedback submitted
        message (str): The feedback message
        status (FeedbackResponseStatus): Current review status of the feedback
        created_at (str): ISO 8601 timestamp when the feedback was submitted
        updated_at (str): ISO 8601 timestamp when the feedback was last updated
    """

    unique_id: UUID
    entity_type: FeedbackResponseEntityType
    entity_id: Union[None, UUID]
    feedback_type: Union[FeedbackResponseFeedbackTypeType0, None]
    message: str
    status: FeedbackResponseStatus
    created_at: str
    updated_at: str

    def to_dict(self) -> dict[str, Any]:
        unique_id = str(self.unique_id)

        entity_type = self.entity_type.value

        entity_id: Union[None, str]
        if isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        feedback_type: Union[None, str]
        if isinstance(self.feedback_type, FeedbackResponseFeedbackTypeType0):
            feedback_type = self.feedback_type.value
        else:
            feedback_type = self.feedback_type

        message = self.message

        status = self.status.value

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

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

        entity_type = FeedbackResponseEntityType(d.pop("entity_type"))

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

        def _parse_feedback_type(data: object) -> Union[FeedbackResponseFeedbackTypeType0, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feedback_type_type_0 = FeedbackResponseFeedbackTypeType0(data)

                return feedback_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[FeedbackResponseFeedbackTypeType0, None], data)

        feedback_type = _parse_feedback_type(d.pop("feedback_type"))

        message = d.pop("message")

        status = FeedbackResponseStatus(d.pop("status"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        feedback_response = cls(
            unique_id=unique_id,
            entity_type=entity_type,
            entity_id=entity_id,
            feedback_type=feedback_type,
            message=message,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        return feedback_response
