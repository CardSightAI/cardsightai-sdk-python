from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AIQueryResponseInput")


@_attrs_define
class AIQueryResponseInput:
    """
    Attributes:
        answer (str): AI-generated response to the query
        processing_time (float): Time taken to process the query in milliseconds
        tools_used (Union[Unset, list[str]]): List of MCP tools used to answer the query
    """

    answer: str
    processing_time: float
    tools_used: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        processing_time = self.processing_time

        tools_used: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tools_used, Unset):
            tools_used = self.tools_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        ai_query_response_input = cls(
            answer=answer,
            processing_time=processing_time,
            tools_used=tools_used,
        )

        ai_query_response_input.additional_properties = d
        return ai_query_response_input

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
