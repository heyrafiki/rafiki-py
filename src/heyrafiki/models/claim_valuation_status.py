from typing import Literal

ClaimValuationStatus = Literal[
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

CLAIM_VALUATION_STATUS_VALUES: set[ClaimValuationStatus] = {
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


def check_claim_valuation_status(value: str) -> ClaimValuationStatus:
    if value in CLAIM_VALUATION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_VALUATION_STATUS_VALUES!r}"
    )
