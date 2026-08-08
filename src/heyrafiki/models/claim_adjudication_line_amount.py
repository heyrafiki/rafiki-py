from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimAdjudicationLineAmount")


@_attrs_define
class ClaimAdjudicationLineAmount:
    billed: int
    allowed: int
    payer: int
    patient_responsibility: int
    adjustment: int

    def to_dict(self) -> dict[str, Any]:
        billed = self.billed

        allowed = self.allowed

        payer = self.payer

        patient_responsibility = self.patient_responsibility

        adjustment = self.adjustment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billed": billed,
                "allowed": allowed,
                "payer": payer,
                "patient_responsibility": patient_responsibility,
                "adjustment": adjustment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed = d.pop("billed")

        allowed = d.pop("allowed")

        payer = d.pop("payer")

        patient_responsibility = d.pop("patient_responsibility")

        adjustment = d.pop("adjustment")

        claim_adjudication_line_amount = cls(
            billed=billed,
            allowed=allowed,
            payer=payer,
            patient_responsibility=patient_responsibility,
            adjustment=adjustment,
        )

        return claim_adjudication_line_amount
