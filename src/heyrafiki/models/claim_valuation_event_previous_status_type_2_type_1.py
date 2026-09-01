from typing import Literal

ClaimValuationEventPreviousStatusType2Type1 = Literal[
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

CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_2_TYPE_1_VALUES: set[
    ClaimValuationEventPreviousStatusType2Type1
] = {
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


def check_claim_valuation_event_previous_status_type_2_type_1(
    value: str,
) -> ClaimValuationEventPreviousStatusType2Type1:
    if value in CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_VALUATION_EVENT_PREVIOUS_STATUS_TYPE_2_TYPE_1_VALUES!r}"
    )
