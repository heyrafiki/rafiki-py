from typing import Literal

PreauthorizationDecisionOutcome = Literal["approved", "denied"]

PREAUTHORIZATION_DECISION_OUTCOME_VALUES: set[PreauthorizationDecisionOutcome] = {
    "approved",
    "denied",
}


def check_preauthorization_decision_outcome(value: str) -> PreauthorizationDecisionOutcome:
    if value in PREAUTHORIZATION_DECISION_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREAUTHORIZATION_DECISION_OUTCOME_VALUES!r}"
    )
