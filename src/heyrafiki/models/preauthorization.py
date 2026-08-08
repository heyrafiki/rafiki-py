from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.preauthorization_status import PreauthorizationStatus, check_preauthorization_status

if TYPE_CHECKING:
    from ..models.preauthorization_amount import PreauthorizationAmount
    from ..models.preauthorization_decision import PreauthorizationDecision


T = TypeVar("T", bound="Preauthorization")


@_attrs_define
class Preauthorization:
    id: str
    object_: Literal["preauthorization"]
    eligibility_check_id: str
    booking_id: str
    status: PreauthorizationStatus
    reason_codes: list[str]
    amount: PreauthorizationAmount
    valid_until: datetime.datetime | None
    created_at: datetime.datetime
    decision: None | PreauthorizationDecision

    def to_dict(self) -> dict[str, Any]:
        from ..models.preauthorization_decision import PreauthorizationDecision

        id = self.id

        object_ = self.object_

        eligibility_check_id = self.eligibility_check_id

        booking_id = self.booking_id

        status: str = self.status

        reason_codes = self.reason_codes

        amount = self.amount.to_dict()

        valid_until: None | str
        if isinstance(self.valid_until, datetime.datetime):
            valid_until = self.valid_until.isoformat()
        else:
            valid_until = self.valid_until

        created_at = self.created_at.isoformat()

        decision: dict[str, Any] | None
        if isinstance(self.decision, PreauthorizationDecision):
            decision = self.decision.to_dict()
        else:
            decision = self.decision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "eligibility_check_id": eligibility_check_id,
                "booking_id": booking_id,
                "status": status,
                "reason_codes": reason_codes,
                "amount": amount,
                "valid_until": valid_until,
                "created_at": created_at,
                "decision": decision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preauthorization_amount import PreauthorizationAmount
        from ..models.preauthorization_decision import PreauthorizationDecision

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["preauthorization"], d.pop("object"))
        if object_ != "preauthorization":
            raise ValueError(f"object must match const 'preauthorization', got '{object_}'")

        eligibility_check_id = d.pop("eligibility_check_id")

        booking_id = d.pop("booking_id")

        status = check_preauthorization_status(d.pop("status"))

        reason_codes = cast(list[str], d.pop("reason_codes"))

        amount = PreauthorizationAmount.from_dict(d.pop("amount"))

        def _parse_valid_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_until_type_0 = datetime.datetime.fromisoformat(data)

                return valid_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        valid_until = _parse_valid_until(d.pop("valid_until"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_decision(data: object) -> None | PreauthorizationDecision:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                decision_type_0 = PreauthorizationDecision.from_dict(data)

                return decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PreauthorizationDecision, data)

        decision = _parse_decision(d.pop("decision"))

        preauthorization = cls(
            id=id,
            object_=object_,
            eligibility_check_id=eligibility_check_id,
            booking_id=booking_id,
            status=status,
            reason_codes=reason_codes,
            amount=amount,
            valid_until=valid_until,
            created_at=created_at,
            decision=decision,
        )

        return preauthorization
