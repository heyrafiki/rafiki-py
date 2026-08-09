from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.booking_input_format import BookingInputFormat, check_booking_input_format
from ..models.booking_input_payment_source import (
    BookingInputPaymentSource,
    check_booking_input_payment_source,
)

T = TypeVar("T", bound="BookingInput")


@_attrs_define
class BookingInput:
    practitioner_id: str
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    format_: BookingInputFormat
    payment_source: BookingInputPaymentSource

    def to_dict(self) -> dict[str, Any]:
        practitioner_id = self.practitioner_id

        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        format_: str = self.format_

        payment_source: str = self.payment_source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "practitioner_id": practitioner_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "format": format_,
                "payment_source": payment_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        practitioner_id = d.pop("practitioner_id")

        starts_at = parse_datetime(d.pop("starts_at"))

        ends_at = parse_datetime(d.pop("ends_at"))

        format_ = check_booking_input_format(d.pop("format"))

        payment_source = check_booking_input_payment_source(d.pop("payment_source"))

        booking_input = cls(
            practitioner_id=practitioner_id,
            starts_at=starts_at,
            ends_at=ends_at,
            format_=format_,
            payment_source=payment_source,
        )

        return booking_input
