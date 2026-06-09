from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReleaseCalendarEntryInput")


@_attrs_define
class ReleaseCalendarEntryInput:
    """
    Attributes:
        id (UUID): Unique identifier for the release calendar entry
        name (str): Name of the release
        year (Union[None, str]): Release year
        release_date (Union[None, str]): Expected or actual release date (YYYY-MM-DD)
        pre_order_date (Union[None, str]): Date when pre-orders open (YYYY-MM-DD)
        segment_id (Union[None, UUID]): Unique identifier of the associated market segment
        manufacturer_id (Union[None, UUID]): Unique identifier of the associated manufacturer
    """

    id: UUID
    name: str
    year: Union[None, str]
    release_date: Union[None, str]
    pre_order_date: Union[None, str]
    segment_id: Union[None, UUID]
    manufacturer_id: Union[None, UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        year: Union[None, str]
        year = self.year

        release_date: Union[None, str]
        release_date = self.release_date

        pre_order_date: Union[None, str]
        pre_order_date = self.pre_order_date

        segment_id: Union[None, str]
        if isinstance(self.segment_id, UUID):
            segment_id = str(self.segment_id)
        else:
            segment_id = self.segment_id

        manufacturer_id: Union[None, str]
        if isinstance(self.manufacturer_id, UUID):
            manufacturer_id = str(self.manufacturer_id)
        else:
            manufacturer_id = self.manufacturer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "year": year,
                "release_date": release_date,
                "pre_order_date": pre_order_date,
                "segment_id": segment_id,
                "manufacturer_id": manufacturer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_year(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        year = _parse_year(d.pop("year"))

        def _parse_release_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        release_date = _parse_release_date(d.pop("release_date"))

        def _parse_pre_order_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        pre_order_date = _parse_pre_order_date(d.pop("pre_order_date"))

        def _parse_segment_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                segment_id_type_0 = UUID(data)

                return segment_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        segment_id = _parse_segment_id(d.pop("segment_id"))

        def _parse_manufacturer_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                manufacturer_id_type_0 = UUID(data)

                return manufacturer_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        manufacturer_id = _parse_manufacturer_id(d.pop("manufacturer_id"))

        release_calendar_entry_input = cls(
            id=id,
            name=name,
            year=year,
            release_date=release_date,
            pre_order_date=pre_order_date,
            segment_id=segment_id,
            manufacturer_id=manufacturer_id,
        )

        release_calendar_entry_input.additional_properties = d
        return release_calendar_entry_input

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
