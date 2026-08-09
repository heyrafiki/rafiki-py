from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.eligibility_check_input_currency import (
    EligibilityCheckInputCurrency,
    check_eligibility_check_input_currency,
)

T = TypeVar("T", bound="EligibilityCheckInput")


@_attrs_define
class EligibilityCheckInput:
    member_reference: str
    service_code: str
    scheduled_at: datetime.datetime
    amount: int
    """ Requested amount in the currency's minor unit. """
    currency: EligibilityCheckInputCurrency

    def to_dict(self) -> dict[str, Any]:
        member_reference = self.member_reference

        service_code = self.service_code

        scheduled_at = self.scheduled_at.isoformat()

        amount = self.amount

        currency: str = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "member_reference": member_reference,
                "service_code": service_code,
                "scheduled_at": scheduled_at,
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_reference = d.pop("member_reference")

        service_code = d.pop("service_code")

        scheduled_at = parse_datetime(d.pop("scheduled_at"))

        amount = d.pop("amount")

        currency = check_eligibility_check_input_currency(d.pop("currency"))

        eligibility_check_input = cls(
            member_reference=member_reference,
            service_code=service_code,
            scheduled_at=scheduled_at,
            amount=amount,
            currency=currency,
        )

        return eligibility_check_input
