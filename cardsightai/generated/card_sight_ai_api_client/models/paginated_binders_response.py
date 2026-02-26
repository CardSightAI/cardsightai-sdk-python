from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.binder import Binder


T = TypeVar("T", bound="PaginatedBindersResponse")


@_attrs_define
class PaginatedBindersResponse:
    """
    Attributes:
        binders (list['Binder']):
        total_count (float):
        skip (float):
        take (float):
    """

    binders: list["Binder"]
    total_count: float
    skip: float
    take: float

    def to_dict(self) -> dict[str, Any]:
        binders = []
        for binders_item_data in self.binders:
            binders_item = binders_item_data.to_dict()
            binders.append(binders_item)

        total_count = self.total_count

        skip = self.skip

        take = self.take

        field_dict: dict[str, Any] = {}

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
        from ..models.binder import Binder

        d = dict(src_dict)
        binders = []
        _binders = d.pop("binders")
        for binders_item_data in _binders:
            binders_item = Binder.from_dict(binders_item_data)

            binders.append(binders_item)

        total_count = d.pop("total_count")

        skip = d.pop("skip")

        take = d.pop("take")

        paginated_binders_response = cls(
            binders=binders,
            total_count=total_count,
            skip=skip,
            take=take,
        )

        return paginated_binders_response
