from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_adjudication_line import ClaimAdjudicationLine


T = TypeVar("T", bound="ClaimAdjudicationInput")


@_attrs_define
class ClaimAdjudicationInput:
    policy_reference: str
    policy_version: str
    reason_codes: list[str]
    lines: list[ClaimAdjudicationLine]
    evidence_refs: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_reference = self.policy_reference

        policy_version = self.policy_version

        reason_codes = self.reason_codes

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        evidence_refs: list[str] | Unset = UNSET
        if not isinstance(self.evidence_refs, Unset):
            evidence_refs = self.evidence_refs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "policy_reference": policy_reference,
                "policy_version": policy_version,
                "reason_codes": reason_codes,
                "lines": lines,
            }
        )
        if evidence_refs is not UNSET:
            field_dict["evidence_refs"] = evidence_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_adjudication_line import ClaimAdjudicationLine

        d = dict(src_dict)
        policy_reference = d.pop("policy_reference")

        policy_version = d.pop("policy_version")

        reason_codes = cast(list[str], d.pop("reason_codes"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ClaimAdjudicationLine.from_dict(lines_item_data)

            lines.append(lines_item)

        evidence_refs = cast(list[str], d.pop("evidence_refs", UNSET))

        claim_adjudication_input = cls(
            policy_reference=policy_reference,
            policy_version=policy_version,
            reason_codes=reason_codes,
            lines=lines,
            evidence_refs=evidence_refs,
        )

        return claim_adjudication_input
