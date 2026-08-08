from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreauthorizationDecisionInputType0")


@_attrs_define
class PreauthorizationDecisionInputType0:
    outcome: Literal["approved"]
    approved_amount: int
    valid_until: datetime.datetime
    reason_codes: list[str]
    policy_reference: str
    policy_version: str
    evidence_references: list[str]

    def to_dict(self) -> dict[str, Any]:
        outcome = self.outcome

        approved_amount = self.approved_amount

        valid_until = self.valid_until.isoformat()

        reason_codes = self.reason_codes

        policy_reference = self.policy_reference

        policy_version = self.policy_version

        evidence_references = self.evidence_references

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "outcome": outcome,
                "approved_amount": approved_amount,
                "valid_until": valid_until,
                "reason_codes": reason_codes,
                "policy_reference": policy_reference,
                "policy_version": policy_version,
                "evidence_references": evidence_references,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        outcome = cast(Literal["approved"], d.pop("outcome"))
        if outcome != "approved":
            raise ValueError(f"outcome must match const 'approved', got '{outcome}'")

        approved_amount = d.pop("approved_amount")

        valid_until = datetime.datetime.fromisoformat(d.pop("valid_until"))

        reason_codes = cast(list[str], d.pop("reason_codes"))

        policy_reference = d.pop("policy_reference")

        policy_version = d.pop("policy_version")

        evidence_references = cast(list[str], d.pop("evidence_references"))

        preauthorization_decision_input_type_0 = cls(
            outcome=outcome,
            approved_amount=approved_amount,
            valid_until=valid_until,
            reason_codes=reason_codes,
            policy_reference=policy_reference,
            policy_version=policy_version,
            evidence_references=evidence_references,
        )

        return preauthorization_decision_input_type_0
