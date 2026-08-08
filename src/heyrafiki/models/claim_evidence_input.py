from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimEvidenceInput")


@_attrs_define
class ClaimEvidenceInput:
    information_request_id: str
    evidence_refs: list[str]

    def to_dict(self) -> dict[str, Any]:
        information_request_id = self.information_request_id

        evidence_refs = self.evidence_refs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "information_request_id": information_request_id,
                "evidence_refs": evidence_refs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        information_request_id = d.pop("information_request_id")

        evidence_refs = cast(list[str], d.pop("evidence_refs"))

        claim_evidence_input = cls(
            information_request_id=information_request_id,
            evidence_refs=evidence_refs,
        )

        return claim_evidence_input
