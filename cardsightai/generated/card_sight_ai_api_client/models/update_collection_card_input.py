from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCollectionCardInput")


@_attrs_define
class UpdateCollectionCardInput:
    """
    Attributes:
        parallel_id (Union[None, UUID, Unset]): UUID of the card parallel (null to remove)
        grade_id (Union[None, UUID, Unset]): UUID of the grade (null to remove)
        quantity (Union[Unset, float]): Updated quantity
        buy_price (Union[None, Unset, str]): Purchase price (null to remove)
        buy_date (Union[None, Unset, str]): Purchase date (null to remove)
        sell_price (Union[None, Unset, str]): Listed selling price (null to remove)
        sold_price (Union[None, Unset, str]): Actual sold price (null to remove)
        sold_date (Union[None, Unset, str]): Sale date (null to remove)
    """

    parallel_id: Union[None, UUID, Unset] = UNSET
    grade_id: Union[None, UUID, Unset] = UNSET
    quantity: Union[Unset, float] = UNSET
    buy_price: Union[None, Unset, str] = UNSET
    buy_date: Union[None, Unset, str] = UNSET
    sell_price: Union[None, Unset, str] = UNSET
    sold_price: Union[None, Unset, str] = UNSET
    sold_date: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parallel_id: Union[None, Unset, str]
        if isinstance(self.parallel_id, Unset):
            parallel_id = UNSET
        elif isinstance(self.parallel_id, UUID):
            parallel_id = str(self.parallel_id)
        else:
            parallel_id = self.parallel_id

        grade_id: Union[None, Unset, str]
        if isinstance(self.grade_id, Unset):
            grade_id = UNSET
        elif isinstance(self.grade_id, UUID):
            grade_id = str(self.grade_id)
        else:
            grade_id = self.grade_id

        quantity = self.quantity

        buy_price: Union[None, Unset, str]
        if isinstance(self.buy_price, Unset):
            buy_price = UNSET
        else:
            buy_price = self.buy_price

        buy_date: Union[None, Unset, str]
        if isinstance(self.buy_date, Unset):
            buy_date = UNSET
        else:
            buy_date = self.buy_date

        sell_price: Union[None, Unset, str]
        if isinstance(self.sell_price, Unset):
            sell_price = UNSET
        else:
            sell_price = self.sell_price

        sold_price: Union[None, Unset, str]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        sold_date: Union[None, Unset, str]
        if isinstance(self.sold_date, Unset):
            sold_date = UNSET
        else:
            sold_date = self.sold_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parallel_id is not UNSET:
            field_dict["parallelId"] = parallel_id
        if grade_id is not UNSET:
            field_dict["gradeId"] = grade_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if buy_price is not UNSET:
            field_dict["buyPrice"] = buy_price
        if buy_date is not UNSET:
            field_dict["buyDate"] = buy_date
        if sell_price is not UNSET:
            field_dict["sellPrice"] = sell_price
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_parallel_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parallel_id_type_0 = UUID(data)

                return parallel_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        parallel_id = _parse_parallel_id(d.pop("parallelId", UNSET))

        def _parse_grade_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grade_id_type_0 = UUID(data)

                return grade_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        grade_id = _parse_grade_id(d.pop("gradeId", UNSET))

        quantity = d.pop("quantity", UNSET)

        def _parse_buy_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        buy_price = _parse_buy_price(d.pop("buyPrice", UNSET))

        def _parse_buy_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        buy_date = _parse_buy_date(d.pop("buyDate", UNSET))

        def _parse_sell_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sell_price = _parse_sell_price(d.pop("sellPrice", UNSET))

        def _parse_sold_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))

        def _parse_sold_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sold_date = _parse_sold_date(d.pop("soldDate", UNSET))

        update_collection_card_input = cls(
            parallel_id=parallel_id,
            grade_id=grade_id,
            quantity=quantity,
            buy_price=buy_price,
            buy_date=buy_date,
            sell_price=sell_price,
            sold_price=sold_price,
            sold_date=sold_date,
        )

        update_collection_card_input.additional_properties = d
        return update_collection_card_input

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
