from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimValuationAmount")


@_attrs_define
class ClaimValuationAmount:
    billed: int
    payer_liability: int | None
    patient_responsibility: int | None
    adjustment: int | None
    remitted: int
    """ Payer advice known at the cutoff. """
    settled: int
    """ Independently observed money movement known at the cutoff. """
    outstanding: int | None
    """ Payer liability less independently observed settlement. """

    def to_dict(self) -> dict[str, Any]:
        billed = self.billed

        payer_liability: int | None
        payer_liability = self.payer_liability

        patient_responsibility: int | None
        patient_responsibility = self.patient_responsibility

        adjustment: int | None
        adjustment = self.adjustment

        remitted = self.remitted

        settled = self.settled

        outstanding: int | None
        outstanding = self.outstanding

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billed": billed,
                "payer_liability": payer_liability,
                "patient_responsibility": patient_responsibility,
                "adjustment": adjustment,
                "remitted": remitted,
                "settled": settled,
                "outstanding": outstanding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed = d.pop("billed")

        def _parse_payer_liability(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_liability = _parse_payer_liability(d.pop("payer_liability"))

        def _parse_patient_responsibility(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        patient_responsibility = _parse_patient_responsibility(d.pop("patient_responsibility"))

        def _parse_adjustment(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        adjustment = _parse_adjustment(d.pop("adjustment"))

        remitted = d.pop("remitted")

        settled = d.pop("settled")

        def _parse_outstanding(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        outstanding = _parse_outstanding(d.pop("outstanding"))

        claim_valuation_amount = cls(
            billed=billed,
            payer_liability=payer_liability,
            patient_responsibility=patient_responsibility,
            adjustment=adjustment,
            remitted=remitted,
            settled=settled,
            outstanding=outstanding,
        )

        return claim_valuation_amount
