from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.binder_input import BinderInput


T = TypeVar("T", bound="PaginatedBindersResponseInput")


@_attrs_define
class PaginatedBindersResponseInput:
    """
    Attributes:
        binders (list['BinderInput']):
        total_count (float):
        skip (float):
        take (float):
    """

    binders: list["BinderInput"]
    total_count: float
    skip: float
    take: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binders = []
        for binders_item_data in self.binders:
            binders_item = binders_item_data.to_dict()
            binders.append(binders_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binders": binders,
                "total_count": total_count,
                "skip": skip,
                "take": take,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binder_input import BinderInput

        d = dict(src_dict)
        binders = []
        _binders = d.pop("binders")
        for binders_item_data in _binders:
            binders_item = BinderInput.from_dict(binders_item_data)

            binders.append(binders_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_binders_response_input = cls(
            binders=binders,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        paginated_binders_response_input.additional_properties = d
        return paginated_binders_response_input

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
