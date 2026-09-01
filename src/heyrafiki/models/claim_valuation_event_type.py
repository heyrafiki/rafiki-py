from typing import Literal

ClaimValuationEventType = Literal[
    "approved",
    "cancelled",
    "created",
    "denied",
    "evidence_added",
    "partially_approved",
    "queried",
    "reconciled",
    "remittance_recorded",
    "resubmitted",
    "reversed",
    "settled",
    "submitted",
    "validated",
]

CLAIM_VALUATION_EVENT_TYPE_VALUES: set[ClaimValuationEventType] = {
    "approved",
    "cancelled",
    "created",
    "denied",
    "evidence_added",
    "partially_approved",
    "queried",
    "reconciled",
    "remittance_recorded",
    "resubmitted",
    "reversed",
    "settled",
    "submitted",
    "validated",
}


def check_claim_valuation_event_type(value: str) -> ClaimValuationEventType:
    if value in CLAIM_VALUATION_EVENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_VALUATION_EVENT_TYPE_VALUES!r}"
    )
