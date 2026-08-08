from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimAdjudicationAmount")


@_attrs_define
class ClaimAdjudicationAmount:
    currency: str
    billed: int
    payer: int
    patient_responsibility: int
    adjustment: int

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        billed = self.billed

        payer = self.payer

        patient_responsibility = self.patient_responsibility

        adjustment = self.adjustment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "billed": billed,
                "payer": payer,
                "patient_responsibility": patient_responsibility,
                "adjustment": adjustment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        billed = d.pop("billed")

        payer = d.pop("payer")

        patient_responsibility = d.pop("patient_responsibility")

        adjustment = d.pop("adjustment")

        claim_adjudication_amount = cls(
            currency=currency,
            billed=billed,
            payer=payer,
            patient_responsibility=patient_responsibility,
            adjustment=adjustment,
        )

        return claim_adjudication_amount
