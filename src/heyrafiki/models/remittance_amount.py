from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RemittanceAmount")


@_attrs_define
class RemittanceAmount:
    currency: str
    paid: int

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        paid = self.paid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "paid": paid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        paid = d.pop("paid")

        remittance_amount = cls(
            currency=currency,
            paid=paid,
        )

        return remittance_amount
