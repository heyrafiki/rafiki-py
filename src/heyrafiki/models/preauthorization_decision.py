from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.preauthorization_decision_outcome import (
    PreauthorizationDecisionOutcome,
    check_preauthorization_decision_outcome,
)

if TYPE_CHECKING:
    from ..models.preauthorization_decision_policy import PreauthorizationDecisionPolicy


T = TypeVar("T", bound="PreauthorizationDecision")


@_attrs_define
class PreauthorizationDecision:
    id: str
    object_: Literal["preauthorization_decision"]
    version: int
    outcome: PreauthorizationDecisionOutcome
    reason_codes: list[str]
    policy: PreauthorizationDecisionPolicy
    authority_reference: str
    evidence_references: list[str]
    decided_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        version = self.version

        outcome: str = self.outcome

        reason_codes = self.reason_codes

        policy = self.policy.to_dict()

        authority_reference = self.authority_reference

        evidence_references = self.evidence_references

        decided_at = self.decided_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "version": version,
                "outcome": outcome,
                "reason_codes": reason_codes,
                "policy": policy,
                "authority_reference": authority_reference,
                "evidence_references": evidence_references,
                "decided_at": decided_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preauthorization_decision_policy import PreauthorizationDecisionPolicy

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["preauthorization_decision"], d.pop("object"))
        if object_ != "preauthorization_decision":
            raise ValueError(
                f"object must match const 'preauthorization_decision', got '{object_}'"
            )

        version = d.pop("version")

        outcome = check_preauthorization_decision_outcome(d.pop("outcome"))

        reason_codes = cast(list[str], d.pop("reason_codes"))

        policy = PreauthorizationDecisionPolicy.from_dict(d.pop("policy"))

        authority_reference = d.pop("authority_reference")

        evidence_references = cast(list[str], d.pop("evidence_references"))

        decided_at = datetime.datetime.fromisoformat(d.pop("decided_at"))

        preauthorization_decision = cls(
            id=id,
            object_=object_,
            version=version,
            outcome=outcome,
            reason_codes=reason_codes,
            policy=policy,
            authority_reference=authority_reference,
            evidence_references=evidence_references,
            decided_at=decided_at,
        )

        return preauthorization_decision
