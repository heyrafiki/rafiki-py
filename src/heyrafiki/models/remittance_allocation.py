from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RemittanceAllocation")


@_attrs_define
class RemittanceAllocation:
    claim_id: str
    paid_amount: int
    reason_codes: list[str]

    def to_dict(self) -> dict[str, Any]:
        claim_id = self.claim_id

        paid_amount = self.paid_amount

        reason_codes = self.reason_codes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "claim_id": claim_id,
                "paid_amount": paid_amount,
                "reason_codes": reason_codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claim_id = d.pop("claim_id")

        paid_amount = d.pop("paid_amount")

        reason_codes = cast(list[str], d.pop("reason_codes"))

        remittance_allocation = cls(
            claim_id=claim_id,
            paid_amount=paid_amount,
            reason_codes=reason_codes,
        )

        return remittance_allocation
