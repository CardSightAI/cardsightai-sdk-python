from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_context_input import AIContextInput
    from ..models.conversation_message_input import ConversationMessageInput


T = TypeVar("T", bound="AIQueryRequestInput")


@_attrs_define
class AIQueryRequestInput:
    """
    Attributes:
        query (str): Natural language query
        context (Union[Unset, AIContextInput]):
        conversation_history (Union[Unset, list['ConversationMessageInput']]): Optional conversation history (max 50
            messages). Messages should alternate between user and assistant roles.
        max_iterations (Union[Unset, int]): Maximum tool use iterations (default: 5)
    """

    query: str
    context: Union[Unset, "AIContextInput"] = UNSET
    conversation_history: Union[Unset, list["ConversationMessageInput"]] = UNSET
    max_iterations: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        conversation_history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conversation_history, Unset):
            conversation_history = []
            for conversation_history_item_data in self.conversation_history:
                conversation_history_item = conversation_history_item_data.to_dict()
                conversation_history.append(conversation_history_item)

        max_iterations = self.max_iterations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if conversation_history is not UNSET:
            field_dict["conversationHistory"] = conversation_history
        if max_iterations is not UNSET:
            field_dict["maxIterations"] = max_iterations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_context_input import AIContextInput
        from ..models.conversation_message_input import ConversationMessageInput

        d = dict(src_dict)
        query = d.pop("query")

        _context = d.pop("context", UNSET)
        context: Union[Unset, AIContextInput]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = AIContextInput.from_dict(_context)

        conversation_history = []
        _conversation_history = d.pop("conversationHistory", UNSET)
        for conversation_history_item_data in _conversation_history or []:
            conversation_history_item = ConversationMessageInput.from_dict(conversation_history_item_data)

            conversation_history.append(conversation_history_item)

        max_iterations = d.pop("maxIterations", UNSET)

        ai_query_request_input = cls(
            query=query,
            context=context,
            conversation_history=conversation_history,
            max_iterations=max_iterations,
        )

        ai_query_request_input.additional_properties = d
        return ai_query_request_input

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
