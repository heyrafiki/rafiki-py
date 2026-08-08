from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PractitionerLocation")


@_attrs_define
class PractitionerLocation:
    city: str
    country: str

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "city": city,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city")

        country = d.pop("country")

        practitioner_location = cls(
            city=city,
            country=country,
        )

        return practitioner_location
