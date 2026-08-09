from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.claim_adjudication_decision import (
    ClaimAdjudicationDecision,
    check_claim_adjudication_decision,
)

if TYPE_CHECKING:
    from ..models.claim_adjudication_amount import ClaimAdjudicationAmount
    from ..models.claim_adjudication_line import ClaimAdjudicationLine
    from ..models.claim_adjudication_policy import ClaimAdjudicationPolicy


T = TypeVar("T", bound="ClaimAdjudication")


@_attrs_define
class ClaimAdjudication:
    id: str
    object_: Literal["claim_adjudication"]
    version: int
    decision: ClaimAdjudicationDecision
    amount: ClaimAdjudicationAmount
    reason_codes: list[str]
    policy: ClaimAdjudicationPolicy
    lines: list[ClaimAdjudicationLine]
    decided_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        version = self.version

        decision: str = self.decision

        amount = self.amount.to_dict()

        reason_codes = self.reason_codes

        policy = self.policy.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        decided_at = self.decided_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "version": version,
                "decision": decision,
                "amount": amount,
                "reason_codes": reason_codes,
                "policy": policy,
                "lines": lines,
                "decided_at": decided_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_adjudication_amount import ClaimAdjudicationAmount
        from ..models.claim_adjudication_line import ClaimAdjudicationLine
        from ..models.claim_adjudication_policy import ClaimAdjudicationPolicy

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["claim_adjudication"], d.pop("object"))
        if object_ != "claim_adjudication":
            raise ValueError(f"object must match const 'claim_adjudication', got '{object_}'")

        version = d.pop("version")

        decision = check_claim_adjudication_decision(d.pop("decision"))

        amount = ClaimAdjudicationAmount.from_dict(d.pop("amount"))

        reason_codes = cast(list[str], d.pop("reason_codes"))

        policy = ClaimAdjudicationPolicy.from_dict(d.pop("policy"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ClaimAdjudicationLine.from_dict(lines_item_data)

            lines.append(lines_item)

        decided_at = parse_datetime(d.pop("decided_at"))

        claim_adjudication = cls(
            id=id,
            object_=object_,
            version=version,
            decision=decision,
            amount=amount,
            reason_codes=reason_codes,
            policy=policy,
            lines=lines,
            decided_at=decided_at,
        )

        return claim_adjudication
