from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.booking_format import BookingFormat, check_booking_format
from ..models.booking_payment_source import BookingPaymentSource, check_booking_payment_source
from ..models.booking_status import BookingStatus, check_booking_status

T = TypeVar("T", bound="Booking")


@_attrs_define
class Booking:
    id: str
    object_: Literal["booking"]
    session_id: str
    practitioner_id: str
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    timezone: str
    format_: BookingFormat
    status: BookingStatus
    payment_source: BookingPaymentSource

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        session_id = self.session_id

        practitioner_id = self.practitioner_id

        starts_at = self.starts_at.isoformat()

        ends_at = self.ends_at.isoformat()

        timezone = self.timezone

        format_: str = self.format_

        status: str = self.status

        payment_source: str = self.payment_source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "session_id": session_id,
                "practitioner_id": practitioner_id,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "timezone": timezone,
                "format": format_,
                "status": status,
                "payment_source": payment_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["booking"], d.pop("object"))
        if object_ != "booking":
            raise ValueError(f"object must match const 'booking', got '{object_}'")

        session_id = d.pop("session_id")

        practitioner_id = d.pop("practitioner_id")

        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        timezone = d.pop("timezone")

        format_ = check_booking_format(d.pop("format"))

        status = check_booking_status(d.pop("status"))

        payment_source = check_booking_payment_source(d.pop("payment_source"))

        booking = cls(
            id=id,
            object_=object_,
            session_id=session_id,
            practitioner_id=practitioner_id,
            starts_at=starts_at,
            ends_at=ends_at,
            timezone=timezone,
            format_=format_,
            status=status,
            payment_source=payment_source,
        )

        return booking
