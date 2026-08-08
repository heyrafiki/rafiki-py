from typing import Literal

ClaimAdjudicationDecision = Literal["approved", "denied", "partially_approved"]

CLAIM_ADJUDICATION_DECISION_VALUES: set[ClaimAdjudicationDecision] = {
    "approved",
    "denied",
    "partially_approved",
}


def check_claim_adjudication_decision(value: str) -> ClaimAdjudicationDecision:
    if value in CLAIM_ADJUDICATION_DECISION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLAIM_ADJUDICATION_DECISION_VALUES!r}"
    )
