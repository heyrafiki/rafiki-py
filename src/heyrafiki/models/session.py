from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.session_format import SessionFormat, check_session_format
from ..models.session_payment_source import SessionPaymentSource, check_session_payment_source
from ..models.session_status import SessionStatus, check_session_status

T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    id: str
    object_: Literal["session"]
    practitioner_id: str
    starts_at: datetime.datetime
    ends_at: datetime.datetime
    timezone: str
    format_: SessionFormat
    status: SessionStatus
    payment_source: SessionPaymentSource

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

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

        object_ = cast(Literal["session"], d.pop("object"))
        if object_ != "session":
            raise ValueError(f"object must match const 'session', got '{object_}'")

        practitioner_id = d.pop("practitioner_id")

        starts_at = parse_datetime(d.pop("starts_at"))

        ends_at = parse_datetime(d.pop("ends_at"))

        timezone = d.pop("timezone")

        format_ = check_session_format(d.pop("format"))

        status = check_session_status(d.pop("status"))

        payment_source = check_session_payment_source(d.pop("payment_source"))

        session = cls(
            id=id,
            object_=object_,
            practitioner_id=practitioner_id,
            starts_at=starts_at,
            ends_at=ends_at,
            timezone=timezone,
            format_=format_,
            status=status,
            payment_source=payment_source,
        )

        return session
