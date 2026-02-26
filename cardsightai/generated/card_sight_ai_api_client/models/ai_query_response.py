from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIQueryResponse")


@_attrs_define
class AIQueryResponse:
    """
    Attributes:
        answer (str): AI-generated response to the query
        processing_time (float): Time taken to process the query in milliseconds
        tools_used (Union[Unset, list[str]]): List of MCP tools used to answer the query
    """

    answer: str
    processing_time: float
    tools_used: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        processing_time = self.processing_time

        tools_used: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tools_used, Unset):
            tools_used = self.tools_used

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answer": answer,
                "processingTime": processing_time,
            }
        )
        if tools_used is not UNSET:
            field_dict["toolsUsed"] = tools_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answer = d.pop("answer")

        processing_time = d.pop("processingTime")

        tools_used = cast(list[str], d.pop("toolsUsed", UNSET))

        ai_query_response = cls(
            answer=answer,
            processing_time=processing_time,
            tools_used=tools_used,
        )

        return ai_query_response
