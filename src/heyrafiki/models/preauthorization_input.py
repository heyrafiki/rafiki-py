from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreauthorizationInput")


@_attrs_define
class PreauthorizationInput:
    eligibility_check_id: str
    booking_id: str

    def to_dict(self) -> dict[str, Any]:
        eligibility_check_id = self.eligibility_check_id

        booking_id = self.booking_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eligibility_check_id": eligibility_check_id,
                "booking_id": booking_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        eligibility_check_id = d.pop("eligibility_check_id")

        booking_id = d.pop("booking_id")

        preauthorization_input = cls(
            eligibility_check_id=eligibility_check_id,
            booking_id=booking_id,
        )

        return preauthorization_input
