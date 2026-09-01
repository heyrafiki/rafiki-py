from typing import Literal

ClaimValuationEventPreviousStatusType1 = Literal[
    "approved",
    "cancelled",
    "denied",
    "draft",
    "partially_approved",
    "queried",
    "reversed",
    "settled",
    "submitted",
]

CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_1_VALUES: set[ClaimValuationEventPreviousStatusType1] = {
    "approved",
    "cancelled",
    "denied",
    "draft",
    "partially_approved",
    "queried",
    "reversed",
    "settled",
    "submitted",
}


def check_claim_valuation_event_previous_status_type_1(
    value: str,
) -> ClaimValuationEventPreviousStatusType1:
    if value in CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_1_VALUES!r}"
    )
