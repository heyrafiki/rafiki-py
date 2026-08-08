from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PractitionerSessionFee")


@_attrs_define
class PractitionerSessionFee:
    amount: int
    """ Amount in the currency's minor unit. """
    currency: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        practitioner_session_fee = cls(
            amount=amount,
            currency=currency,
        )

        return practitioner_session_fee
