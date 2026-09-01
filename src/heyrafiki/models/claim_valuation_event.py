from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.claim_valuation_event_next_status_type_1 import (
    ClaimValuationEventNextStatusType1,
    check_claim_valuation_event_next_status_type_1,
)
from ..models.claim_valuation_event_next_status_type_2_type_1 import (
    ClaimValuationEventNextStatusType2Type1,
    check_claim_valuation_event_next_status_type_2_type_1,
)
from ..models.claim_valuation_event_next_status_type_3_type_1 import (
    ClaimValuationEventNextStatusType3Type1,
    check_claim_valuation_event_next_status_type_3_type_1,
)
from ..models.claim_valuation_event_previous_status_type_1 import (
    ClaimValuationEventPreviousStatusType1,
    check_claim_valuation_event_previous_status_type_1,
)
from ..models.claim_valuation_event_previous_status_type_2_type_1 import (
    ClaimValuationEventPreviousStatusType2Type1,
    check_claim_valuation_event_previous_status_type_2_type_1,
)
from ..models.claim_valuation_event_previous_status_type_3_type_1 import (
    ClaimValuationEventPreviousStatusType3Type1,
    check_claim_valuation_event_previous_status_type_3_type_1,
)
from ..models.claim_valuation_event_type import (
    ClaimValuationEventType,
    check_claim_valuation_event_type,
)

T = TypeVar("T", bound="ClaimValuationEvent")


@_attrs_define
class ClaimValuationEvent:
    sequence: int
    type_: ClaimValuationEventType
    effective_at: datetime.datetime
    """ Business time when the underlying fact took effect. """
    recorded_at: datetime.datetime
    """ Knowledge time when Heyrafiki persisted the fact. """
    previous_status: (
        ClaimValuationEventPreviousStatusType1
        | ClaimValuationEventPreviousStatusType2Type1
        | ClaimValuationEventPreviousStatusType3Type1
        | None
    )
    next_status: (
        ClaimValuationEventNextStatusType1
        | ClaimValuationEventNextStatusType2Type1
        | ClaimValuationEventNextStatusType3Type1
        | None
    )
    reason_code: None | str
    evidence_references: list[str]

    def to_dict(self) -> dict[str, Any]:
        sequence = self.sequence

        type_: str = self.type_

        effective_at = self.effective_at.isoformat()

        recorded_at = self.recorded_at.isoformat()

        previous_status: None | str
        if isinstance(self.previous_status, str):
            previous_status = self.previous_status
        elif isinstance(self.previous_status, str):
            previous_status = self.previous_status
        elif isinstance(self.previous_status, str):
            previous_status = self.previous_status
        else:
            previous_status = self.previous_status

        next_status: None | str
        if isinstance(self.next_status, str):
            next_status = self.next_status
        elif isinstance(self.next_status, str):
            next_status = self.next_status
        elif isinstance(self.next_status, str):
            next_status = self.next_status
        else:
            next_status = self.next_status

        reason_code: None | str
        reason_code = self.reason_code

        evidence_references = self.evidence_references

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sequence": sequence,
                "type": type_,
                "effective_at": effective_at,
                "recorded_at": recorded_at,
                "previous_status": previous_status,
                "next_status": next_status,
                "reason_code": reason_code,
                "evidence_references": evidence_references,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sequence = d.pop("sequence")

        type_ = check_claim_valuation_event_type(d.pop("type"))

        effective_at = parse_datetime(d.pop("effective_at"))

        recorded_at = parse_datetime(d.pop("recorded_at"))

        def _parse_previous_status(
            data: object,
        ) -> (
            ClaimValuationEventPreviousStatusType1
            | ClaimValuationEventPreviousStatusType2Type1
            | ClaimValuationEventPreviousStatusType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_status_type_1 = check_claim_valuation_event_previous_status_type_1(data)

                return previous_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_status_type_2_type_1 = (
                    check_claim_valuation_event_previous_status_type_2_type_1(data)
                )

                return previous_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_status_type_3_type_1 = (
                    check_claim_valuation_event_previous_status_type_3_type_1(data)
                )

                return previous_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ClaimValuationEventPreviousStatusType1
                | ClaimValuationEventPreviousStatusType2Type1
                | ClaimValuationEventPreviousStatusType3Type1
                | None,
                data,
            )

        previous_status = _parse_previous_status(d.pop("previous_status"))

        def _parse_next_status(
            data: object,
        ) -> (
            ClaimValuationEventNextStatusType1
            | ClaimValuationEventNextStatusType2Type1
            | ClaimValuationEventNextStatusType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_status_type_1 = check_claim_valuation_event_next_status_type_1(data)

                return next_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_status_type_2_type_1 = check_claim_valuation_event_next_status_type_2_type_1(
                    data
                )

                return next_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_status_type_3_type_1 = check_claim_valuation_event_next_status_type_3_type_1(
                    data
                )

                return next_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ClaimValuationEventNextStatusType1
                | ClaimValuationEventNextStatusType2Type1
                | ClaimValuationEventNextStatusType3Type1
                | None,
                data,
            )

        next_status = _parse_next_status(d.pop("next_status"))

        def _parse_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason_code = _parse_reason_code(d.pop("reason_code"))

        evidence_references = cast(list[str], d.pop("evidence_references"))

        claim_valuation_event = cls(
            sequence=sequence,
            type_=type_,
            effective_at=effective_at,
            recorded_at=recorded_at,
            previous_status=previous_status,
            next_status=next_status,
            reason_code=reason_code,
            evidence_references=evidence_references,
        )

        return claim_valuation_event
