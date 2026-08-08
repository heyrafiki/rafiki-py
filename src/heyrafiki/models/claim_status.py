from typing import Literal

ClaimStatus = Literal[
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

CLAIM_STATUS_VALUES: set[ClaimStatus] = {
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


def check_claim_status(value: str) -> ClaimStatus:
    if value in CLAIM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLAIM_STATUS_VALUES!r}")
