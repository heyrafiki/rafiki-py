from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.claim_adjudication_line_amount import ClaimAdjudicationLineAmount


T = TypeVar("T", bound="ClaimAdjudicationLine")


@_attrs_define
class ClaimAdjudicationLine:
    line_number: int
    amount: ClaimAdjudicationLineAmount
    reason_codes: list[str]

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        amount = self.amount.to_dict()

        reason_codes = self.reason_codes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "line_number": line_number,
                "amount": amount,
                "reason_codes": reason_codes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_adjudication_line_amount import ClaimAdjudicationLineAmount

        d = dict(src_dict)
        line_number = d.pop("line_number")

        amount = ClaimAdjudicationLineAmount.from_dict(d.pop("amount"))

        reason_codes = cast(list[str], d.pop("reason_codes"))

        claim_adjudication_line = cls(
            line_number=line_number,
            amount=amount,
            reason_codes=reason_codes,
        )

        return claim_adjudication_line
