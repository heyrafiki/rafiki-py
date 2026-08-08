from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_input_lines_item import ClaimInputLinesItem


T = TypeVar("T", bound="ClaimInput")


@_attrs_define
class ClaimInput:
    eligibility_check_id: str
    session_id: str
    provider_claim_reference: str
    lines: list[ClaimInputLinesItem]
    preauthorization_id: None | str | Unset = UNSET
    evidence_refs: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        eligibility_check_id = self.eligibility_check_id

        session_id = self.session_id

        provider_claim_reference = self.provider_claim_reference

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        preauthorization_id: None | str | Unset
        if isinstance(self.preauthorization_id, Unset):
            preauthorization_id = UNSET
        else:
            preauthorization_id = self.preauthorization_id

        evidence_refs: list[str] | Unset = UNSET
        if not isinstance(self.evidence_refs, Unset):
            evidence_refs = self.evidence_refs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eligibility_check_id": eligibility_check_id,
                "session_id": session_id,
                "provider_claim_reference": provider_claim_reference,
                "lines": lines,
            }
        )
        if preauthorization_id is not UNSET:
            field_dict["preauthorization_id"] = preauthorization_id
        if evidence_refs is not UNSET:
            field_dict["evidence_refs"] = evidence_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_input_lines_item import ClaimInputLinesItem

        d = dict(src_dict)
        eligibility_check_id = d.pop("eligibility_check_id")

        session_id = d.pop("session_id")

        provider_claim_reference = d.pop("provider_claim_reference")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ClaimInputLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        def _parse_preauthorization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preauthorization_id = _parse_preauthorization_id(d.pop("preauthorization_id", UNSET))

        evidence_refs = cast(list[str], d.pop("evidence_refs", UNSET))

        claim_input = cls(
            eligibility_check_id=eligibility_check_id,
            session_id=session_id,
            provider_claim_reference=provider_claim_reference,
            lines=lines,
            preauthorization_id=preauthorization_id,
            evidence_refs=evidence_refs,
        )

        return claim_input
