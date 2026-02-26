from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_context import AIContext
    from ..models.conversation_message import ConversationMessage


T = TypeVar("T", bound="AIQueryRequest")


@_attrs_define
class AIQueryRequest:
    """
    Attributes:
        query (str): Natural language query
        context (Union[Unset, AIContext]):
        conversation_history (Union[Unset, list['ConversationMessage']]): Optional conversation history (max 50
            messages). Messages should alternate between user and assistant roles.
        max_iterations (Union[Unset, int]): Maximum tool use iterations (default: 5)
    """

    query: str
    context: Union[Unset, "AIContext"] = UNSET
    conversation_history: Union[Unset, list["ConversationMessage"]] = UNSET
    max_iterations: Union[Unset, int] = UNSET

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
        from ..models.ai_context import AIContext
        from ..models.conversation_message import ConversationMessage

        d = dict(src_dict)
        query = d.pop("query")

        _context = d.pop("context", UNSET)
        context: Union[Unset, AIContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = AIContext.from_dict(_context)

        conversation_history = []
        _conversation_history = d.pop("conversationHistory", UNSET)
        for conversation_history_item_data in _conversation_history or []:
            conversation_history_item = ConversationMessage.from_dict(conversation_history_item_data)

            conversation_history.append(conversation_history_item)

        max_iterations = d.pop("maxIterations", UNSET)

        ai_query_request = cls(
            query=query,
            context=context,
            conversation_history=conversation_history,
            max_iterations=max_iterations,
        )

        return ai_query_request
